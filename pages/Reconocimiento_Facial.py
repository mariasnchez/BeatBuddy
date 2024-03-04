import streamlit as st
import numpy as np
from PIL import Image
import joblib
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from streamlit.components.v1 import components
from funciones import *
import os

st.set_page_config(
    page_title="Reconocimiento Facial",
    layout="wide"
)

## Estilos
styles("./src/css/style.css")
styles("./src/css/bootstrap.min.css")
fuentes()

## Body
header = header2()
reconocimiento = reconocimiento()


st.markdown(header, unsafe_allow_html=True)
st.markdown(reconocimiento, unsafe_allow_html=True)

## Configuración

clf = joblib.load("model/modelo_reconocimiento.pkl")

# Función para procesar la imagen
def procImg(image):
    resized_image = image.resize((48, 48))
    grayscale_image = resized_image.convert('L')  # Convertir la imagen en escala de grises si es a color
    pixels = np.array(grayscale_image)
    pixels = np.expand_dims(pixels, axis=0)
    return pixels

# Función para predecir la emoción
def predict_emotion(image):
    pixels = procImg(image)
    prediction = clf.predict(pixels)[0]
    predicted_class = np.argmax(prediction)
    emotions = {0: 'Feliz', 1: 'Triste', 2: 'Neutral'}
    return emotions[predicted_class]


# Autenticación API Spotify
client_credentials_manager = SpotifyClientCredentials(st.secrets["client_id"], st.secrets["client_secret"])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtener canción aleatoria
def cancion_aleatoria(sp, playlist_id):
    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id))')['items']
    random_track = random.choice(playlist_tracks)
    random_song_id = random_track['track']['id']
    return random_song_id

# Playlist feliz
playlist_feliz_id = '3ck7KjH34H20a48Ew37roz'
random_feliz = cancion_aleatoria(sp, playlist_feliz_id)

# Playlist triste
playlist_triste_id = '37i9dQZF1DXdZjf8WgcTKM'
random_triste = cancion_aleatoria(sp, playlist_triste_id)

# Playlist neutral
playlist_neutral_id = '4ZQgepEgN2rO6eFUPNZf2l'
random_neutral = cancion_aleatoria(sp, playlist_neutral_id)

# Incorporar la canción
def cancion(predicted_emotion, random_feliz, random_triste, random_neutral):
    if predicted_emotion == 'Feliz':
        song_id = random_feliz
    elif predicted_emotion == 'Triste':
        song_id = random_triste
    elif predicted_emotion == 'Neutral':
        song_id = random_neutral
    iframe_code = f"""
        <div style="display: flex; justify-content: center;">
            <iframe id="iframeRecog" style="border-radius:12px; background-color: transparent;" 
            src="https://open.spotify.com/embed/track/{song_id}?utm_source=generator" 
             frameborder="0" allowfullscreen="" 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
            loading="lazy"></iframe>
        </div>
    """
    return iframe_code


# Streamlit
camara = None
subida = None

subida = st.file_uploader("", type=["jpg", "jpeg", "png"])

if subida is None:
    camara = st.camera_input("")
else:
    image = Image.open(subida)
    st.image(image)
    predicted_emotion = predict_emotion(image)
    st.markdown(prediccion(predicted_emotion), unsafe_allow_html=True)
    iframe_code = cancion(predicted_emotion, random_feliz, random_triste, random_neutral)
    st.markdown(iframe_code, unsafe_allow_html=True)

if camara is not None:
    image = Image.open(camara)
    predicted_emotion = predict_emotion(image)
    st.markdown(prediccion(predicted_emotion), unsafe_allow_html=True)
    iframe_code = cancion(predicted_emotion, random_feliz, random_triste, random_neutral)
    st.markdown(iframe_code, unsafe_allow_html=True)
