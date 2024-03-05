import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib
from funciones import *
from streamlit_image_select import image_select

## Configuración
st.set_page_config(
    page_title="BeatBuddy",
    layout="wide"
)

## Estilos
styles("./src/css/style.css")
styles("./src/css/bootstrap.min.css")
fuentes()
st.markdown("""
    <style>
        [data-testid="stButton"] {
            margin-bottom: 5vh;
        }
    </style>
""", unsafe_allow_html=True)

## Body
logo_png = st.image("img/LogoPNG.png")
logo_png.empty()
header = header2()
asistente = asistente_musical()
pregunta2 = pregunta2()
pregunta3 = pregunta3()
textofinal = textofinal()

st.markdown(header, unsafe_allow_html=True)
st.markdown(asistente, unsafe_allow_html=True)


lr_model = joblib.load('model/modelo_lr_mood.pkl')

LinearSVC_model = joblib.load('model/modelo_linearSVC_motivation.pkl')

processed_songs = pd.read_csv('model/processed_songs_full.csv')



# Selección de ánimo (mood)
preg1 = image_select(
    label="",
    images=[
        "https://cdn-icons-png.flaticon.com/512/1001/1001214.png",
        "https://cdn-icons-png.flaticon.com/512/7457/7457314.png"
    ],
    captions=["Tristeza", "Felicidad"],
    return_value="index", 
    key="0"
)
selected_mood = preg1

# Selección de motivación (motivation)
st.markdown(pregunta2, unsafe_allow_html=True)
preg2 = image_select(
    label="",
    images=[
        "https://cdn-icons-png.flaticon.com/512/1142/1142699.png",
        "https://cdn-icons-png.flaticon.com/512/3221/3221947.png"
    ],
    captions=["Relax", "Energía"],
    return_value="index", 
    key="1"
)
selected_motivation = preg2

# Selección de década (release_decade)
st.markdown(pregunta3, unsafe_allow_html=True)
decade_options = ['1980s', '1990s', '2000s', '2010s', '2020s']
selected_decade = st.selectbox("", decade_options)

# Botón submit
if st.button("¡Sorpréndeme!"):
    # Filtramos el DataFrame con las selecciones del usuario
    filtered_songs = processed_songs[
        (processed_songs['mood'] == selected_mood) &
        (processed_songs['motivation'] == selected_motivation) &
        (processed_songs['release_decade'] == selected_decade)
    ]

    # Mostramos 3 canciones aleatorias que cumplen con las características seleccionadas por el usuario
    if len(filtered_songs) >= 3:
        selected_songs = filtered_songs.sample(3)
        st.markdown(textofinal, unsafe_allow_html=True)
        # Generar iframes de Spotify con los ID de las canciones
        for index, song in selected_songs.iterrows():
            iframe_code = f"""
            <iframe id="cancionesAsis" style="border-radius:12px; background-color: transparent;" 
            src="https://open.spotify.com/embed/track/{song['id']}?utm_source=generator" 
            width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay"; clipboard-write; 
            encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
            st.write(iframe_code, unsafe_allow_html=True)
    else:
        st.write("Lo siento, no hay suficientes canciones que cumplan con esas características.")