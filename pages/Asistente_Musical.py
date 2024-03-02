import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib
from funciones import *

## Configuración
st.set_page_config(
    page_title="BeatBuddy",
    layout="wide"
)

## Estilos
styles("./src/css/style.css")
styles("./src/css/bootstrap.min.css")
fuentes()

## Body
header = header2()
asistente = asistente_musical()

st.markdown(header, unsafe_allow_html=True)
st.markdown(asistente, unsafe_allow_html=True)


lr_model = joblib.load('model/modelo_lr_mood.pkl')

LinearSVC_model = joblib.load('model/modelo_linearSVC_motivation.pkl')

processed_songs = pd.read_csv('model/processed_songs_full.csv')

st.title("¡Sorpréndeme con una canción!")

# Selección de ánimo (mood)
mood_options = {'Tristeza': 0, 'Felicidad': 1}
selected_mood = st.radio("¿Qué ánimo te representa más hoy?", list(mood_options.keys()))

# Selección de motivación (motivation)
motivation_options = {'Relax': 0, 'Energía': 1}
selected_motivation = st.radio("¿Prefieres motivarte o estar más tranquilo?", list(motivation_options.keys()))

# Selección de década (release_decade)
decade_options = ['1980s', '1990s', '2000s', '2010s', '2020s']
selected_decade = st.selectbox("¿Con qué década te encuentras más familiarizado?", decade_options)

# Botón submit
if st.button("¡Sorpréndeme!"):
    # Filtramos el DataFrame con las selecciones del usuario
    filtered_songs = processed_songs[
        (processed_songs['mood'] == mood_options[selected_mood]) &
        (processed_songs['motivation'] == motivation_options[selected_motivation]) &
        (processed_songs['release_decade'] == selected_decade)
    ]

    # Mostramos 3 canciones aleatorias que cumplen con las características seleccionadas por el usuario
    if len(filtered_songs) >= 3:
        selected_songs = filtered_songs.sample(3)
        st.write("¡Aquí tienes tres canciones que podrían sorprenderte!")
        # Generar iframes de Spotify con los ID de las canciones
        for index, song in selected_songs.iterrows():
            iframe_code = f"""
            <iframe style="border-radius:12px; background-color: transparent;" 
            src="https://open.spotify.com/embed/track/{song['id']}?utm_source=generator" 
            width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay"; clipboard-write; 
            encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
            st.write(iframe_code, unsafe_allow_html=True)
    else:
        st.write("Lo siento, no hay suficientes canciones que cumplan con esas características.")