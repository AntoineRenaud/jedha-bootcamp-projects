from neo4j import GraphDatabase, basic_auth

import pandas as pd

import uvicorn
from pydantic import BaseModel, Field
from fastapi import FastAPI

from confluent_kafka import Consumer
import json
import ccloud_lib

CONF = ccloud_lib.read_ccloud_config("python.config")
TOPIC = "netflix-producer"

class Movie(BaseModel):
    movie_title: str = Field(example='Man on Fire')

app = FastAPI()
    
@app.post("/recommandations")
async def recommandations(movie: Movie):

    #this is the adress to use when the connection comes from inside a docker container
    #FOR LOCAL USE ONLY
    driver = GraphDatabase.driver(
        "bolt://host.docker.internal:7687", auth=basic_auth("neo4j", "netflixdb")
    ) 

    movie_title = movie.movie_title

    cypher_query = '''
    MATCH (m:Movie {title: $title})

    WITH m.louvain_community AS community

    MATCH (other:Movie)
    WHERE other.louvain_community = community AND other.title <> {title: $title}
    WITH other
    ORDER BY rand()
    RETURN other.title AS movieTitle
    LIMIT 3'''
    
    def get_result(tx, movie_title):
        result = tx.run(
            cypher_query,
            title = movie_title
        ).data()  # .data() allows to retrieve the result as a list of dictionaries
        return result

    with driver.session(database="neo4j") as session:
        res = session.execute_read(get_result, movie_title)  # here it's a read-only transaction

    return res

@app.get("/movie_watched")
async def movieWatched():
    
    consumer_conf = ccloud_lib.pop_schema_registry_params_from_config(CONF)
    consumer_conf['group.id'] = 'my_weather_consumer'
    consumer_conf['auto.offset.reset'] = 'earliest' # Start from earliest message if no offset is present
    consumer = Consumer(consumer_conf)
    
    consumer.subscribe([TOPIC])
    
    message = None
    max_attempts = 5  # Maximum number of polling attempts before timing out
    attempts = 0

    while attempts < max_attempts:
        msg = consumer.poll(1.0)  # Poll with a 1-second timeout
        if msg is None:
            attempts += 1  # Increment the attempt counter when no message is found
            continue
        if msg.error():
            consumer.close()
            return {"error": msg.error().str()}  # Handle errors

        # Successfully received the first message
        message = msg.value().decode('utf-8')
        break  # Stop polling once the first message is received

    # Close the consumer after receiving the first message or after timeout
    consumer.close()

    if message:
        return {"message": message}
    else:
        return {"message": "No messages found after polling."}
    

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=4000)