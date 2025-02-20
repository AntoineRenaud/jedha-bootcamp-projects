# Code inspired from Confluent Cloud official examples library
# https://github.com/confluentinc/examples/blob/7.1.1-post/clients/cloud/python/producer.py

from confluent_kafka import Producer
import json
import ccloud_lib # Library not installed with pip but imported from ccloud_lib.py
import numpy as np
import pandas as pd
import requests
import time

# Initialize configurations from "python.config" file
CONF = ccloud_lib.read_ccloud_config("python.config")
TOPIC = "netflix-producer"

# Create Producer instance
producer_conf = ccloud_lib.pop_schema_registry_params_from_config(CONF)
producer = Producer(producer_conf)

# Create topic if it doesn't already exist
ccloud_lib.create_topic(CONF, TOPIC)


delivered_records = 0

# Callback called acked (triggered by poll() or flush())
# when a message has been successfully delivered or
# permanently failed delivery (after retries).
def acked(err, msg):
    global delivered_records
    # Delivery report handler called on successful or failed delivery of message
    if err is not None:
        print("Failed to deliver message: {}".format(err))
    else:
        delivered_records += 1
        print("Produced record to topic {} partition [{}] @ offset {}"
                .format(msg.topic(), msg.partition(), msg.offset()))


url = 'https://jedha-netflix-real-time-api.herokuapp.com/users-currently-watching-movie'
df_movie = pd.read_csv('list_title.csv')

#Function that adapt the API result to the filtered database
def requestJedhaApi(url, df_movie):
    movie_found = False
    while not movie_found:
        r = requests.get(url)
        data_dict = json.loads(r.json())

        df = pd.DataFrame(data=data_dict['data'], columns=data_dict['columns'], index=data_dict['index'])
        df = df[df['Name'].isin(df_movie['Title'])]
        df = df[df['YearRelease'] > 2000]
        df['YearRelease'] = df['YearRelease'].astype(int)
        df = df[:1]
        if df.empty:
            print('not found')
        else:
            movie_found=True
            
    return  df[['customerID','Name']].to_dict()


try:
    record_key = "netflix_user"  
    record_value = requestJedhaApi(url, df_movie)


    print("Producing record: {}\t{}".format(record_key, record_value))

    # This will actually send data to your topic
    producer.produce(
        TOPIC,
        key=record_key,
        value=json.dumps(record_value),
        on_delivery=acked
    )
    # p.poll() serves delivery reports (on_delivery)
    # from previous produce() calls thanks to acked callback
    producer.poll(0)

except KeyboardInterrupt:
    pass
finally:
    producer.flush() # Finish producing the latest event before stopping the whole script

