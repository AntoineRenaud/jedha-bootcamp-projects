import streamlit as st
import pandas as pd
import os
import requests
import json

from st_files_connection import FilesConnection

# conn = st.connection('s3', type=FilesConnection)
# df = conn.read("getaround-data/get_around_pricing_project.csv", input_format="csv", ttl=600)

df = pd.read_csv('src/get_around_pricing_project.csv')

# car_model_counts = df['model_key'].value_counts()
# car_model_selected = car_model_counts[car_model_counts.values > 50]
# df['model_key']=df['model_key'].apply(lambda x: x if x in car_model_selected.index else 'Other')

#create a list of all categorical features in the dataset
cat_feature_list = [col for col in df.columns if not pd.api.types.is_numeric_dtype(df[col])]

for feature in cat_feature_list:
    feature_count = df[feature].value_counts()
    feature_percent = feature_count / feature_count.sum() * 100
    df[feature] = df[feature].apply(lambda x: x if x in feature_count.index[feature_percent > 1] else 'other')

col1, col2 = st.columns(2)

def api_predict():
    request_form = {
            "model_key": feature_0,
            "mileage": feature_1,
            "engine_power": feature_2,
            "fuel": feature_3,
            "paint_color": feature_4,
            "car_type": feature_5,
            "private_parking_available": feature_6,
            "has_gps": feature_7,
            "has_air_conditioning": feature_8,
            "automatic_car": feature_9,
            "has_getaround_connect": feature_10,
            "has_speed_regulator": feature_11,
            "winter_tires": feature_12
    }
        
    api_url = os.environ.get('MODEL_PREDICT_ENDPOINT_URL')
    
    response = requests.post(api_url, json=request_form)
    return response.text
      
with col1:
    st.header('Fill the form to have a rental price estimation')
    
    with st.form("my_form"):
        feature_0 = st.selectbox(
            'Car brand', df['model_key'].sort_values().unique()
        )
        feature_1 = st.number_input('Mileage',
                                    min_value=0,
                                    max_value=1000000,
                                    step=1,
                                    format="%d")
        feature_2 = st.number_input('Engine power',
                                    min_value=75,
                                    max_value=300,
                                    step=1,
                                    format="%d")
        feature_3 = st.selectbox(
            'Fuel', df['fuel'].sort_values().unique()
        )
        feature_4 = st.selectbox(
            'Paint color', df['paint_color'].sort_values().unique()
        )
        feature_5 = st.selectbox(
            'Car type', df['car_type'].sort_values().unique()
        )    
        feature_6 = st.toggle(
            'Private parking'
        )
        feature_7= st.toggle(
            'GPS'
        )
        feature_8 = st.toggle(
            'Air conditioning'
        )
        feature_9 = st.toggle(
            'Automatic car'
        )
        feature_10 = st.toggle(
            'GetAround Connect'
        ) 
        feature_11 = st.toggle(
            'Speed regulator'
        ) 
        feature_12 = st.toggle(
            'Winter tires'
        )
        
        submit_button = st.form_submit_button() 


with col2:
        if submit_button:
            response = json.loads(api_predict())
            estimation = response['prediction']
            st.markdown(f'#### The estimated price for your car is: :red[{estimation:0.2f} €]')
            

