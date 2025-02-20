import streamlit as st
import numpy as np
import requests
import librosa
import io
import soundfile as sf
import time

api_url = 'https://audioclassification-api-ffdfa20a8c66.herokuapp.com/prediction'

col1, col2, col3 = st.columns([1,1,1])

st.title("Urban sound classification engine")
st.image('https://images.ctfassets.net/3viuren4us1n/7MmrorOl3fJ8QhDi6jxrpW/1bd31debd4111a143bd48e2d75e394f8/audio_classification.jpg?fm=webp&w=1920', width=700)


audio_file = st.file_uploader("Upload an audio file", type=["wav"], accept_multiple_files=False)

def convert_to_wav_bytes(y_segment, sr):
    # Ensure the audio is in float32 format
    if y_segment.dtype != np.float32:
        y_segment = y_segment.astype(np.float32)

    # Create an in-memory file (BytesIO) and write the audio data as WAV
    buffer = io.BytesIO()
    sf.write(buffer, y_segment, sr, format='WAV')
    buffer.seek(0)  # Rewind the buffer to the beginning
    return buffer
    
    # Initialize session state for loop control
if 'stop_loop' not in st.session_state:
    st.session_state.stop_loop = False

# Function to stop the loop
def stop_loop():
    st.session_state.stop_loop = True  
        
# Initialize real-time analysis button
if st.button("Start Real-Time Analysis"):
    
    if audio_file is not None:
        y, sr = librosa.load(audio_file, sr=16000)
        st.audio(audio_file, format='audio/wav', autoplay=True)  # Play audio file
    
    
    window_size = sr * 5  # 5 seconds window
    hop_size = sr // 2  # half-second hop size for real-time smooth analysis
    
    st.write("Analyzing in real-time...")       
   
           # Button to stop the loop
    if st.button("Stop Analysis"):
        stop_loop()
        
    with st.empty():    
        for i in range(0, len(y), hop_size):
            # Extract a 5-second window            
            y_segment = y[i:i+window_size]    
    
            if len(y_segment) < window_size:  # Stop if we have less than a full segment
                break
                                          
            wav_file = convert_to_wav_bytes(y_segment, sr)
            files = {"file": wav_file}  # Get the raw data of the audio file

            response = requests.post(api_url, files=files)

            if response.status_code == 200:
                pred = response.text
            else:
                pred = response.text                                              

            st.write(f"Analyzing block {(i+1)/sr*2:.0f} : {pred}")
            
            if st.session_state.stop_loop:
                st.write('Analysis stopped')   
                break    
            # Simulate real-time processing speed by sleeping for half the window duration
            time.sleep(5)  # Simulating real-time analysis delay
        st.write("Real-time analysis complete.")
        
        
