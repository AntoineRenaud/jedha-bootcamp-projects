import pandas as pd
import numpy as np
import soundfile as sf
import io
import tensorflow as tf
import tensorflow_hub as hub


import uvicorn
from pydantic import BaseModel, Field
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

yamnet_model = hub.load('https://www.kaggle.com/models/google/yamnet/TensorFlow2/yamnet/1')
restored_model = tf.keras.models.load_model("audio_classifier.keras")

target_map = pd.read_csv('target_map.csv')

app = FastAPI()
    
@app.post("/prediction")
async def prediction(file: UploadFile = File(...)):
    try:
        # Load the audio file into memory using librosa
        audio_bytes = await file.read()
        audio_data, samplerate = sf.read(io.BytesIO(audio_bytes))
        
        # Extract Embeddings Using YAMNet
        def extract_embedding(audio_data):
            # Run YAMNet to get embeddings
            # waveform = audio_data / tf.int16.max
            scores, embeddings, spectrogram = yamnet_model(audio_data)
            # Average embeddings over time frames
            embedding = tf.reduce_mean(embeddings, axis=0)
            return embedding.numpy()
            # return embeddings
            
        embeddings = extract_embedding(audio_data)

        prediction = restored_model.predict(np.reshape(embeddings, (1,1024)))
        
        max_index = np.argmax(prediction)
        
        predicted_class = target_map.loc[target_map['target'] == max_index, 'category'].values[0]
        
        response = predicted_class


        # Clean up the memory by closing the file
        await file.close()

        # Return the analysis result (you can customize this response)
        
        return JSONResponse(content={"message": "Analysis successful", "result": response}, status_code=200)

    except Exception as e:
        # Handle any exceptions and return an error message
        return JSONResponse(content={"message": "Error analyzing the audio file.", "details": str(e)}, status_code=500)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=4000)