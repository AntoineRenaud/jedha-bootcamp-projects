import streamlit as st
import pandas as pd
import json
import requests

OMDB_API_KEY = 'f7299f37'
movie_watched_url='http://localhost:4000/movie_watched'
recommandations_url ='http://localhost:4000/recommandations'

st.title("Netflix recommendation engine")
st.image('https://cdn.magzter.com/1406567956/1674686579/articles/_QGfGLoBx1674814938724/NETFLIX.jpg', width=700)

def posterRequest(name):
    url_poster = f'http://www.omdbapi.com/?t={name}&apikey={OMDB_API_KEY}'  
    response = requests.get(url_poster).json()
    poster_url = response.get('Poster')
    return poster_url

col1, col2, col3 = st.columns([1,1,1])



if col1.button('I just watch a movie !'):
    r = requests.get(movie_watched_url).text
    r_dict = json.loads(r)
    message_dict = json.loads(r_dict['message'])
    name = list(message_dict['Name'].values())[0]
    col1.write(name)
    # st.image(posterRequest(name))
    
    col2.markdown('### **You may also like...**')
    
    reco_r = requests.post(recommandations_url, json={"movie_title": name})
    reco = json.loads(reco_r.text)

    for movie in reco:
        col2.markdown(movie['movieTitle'])