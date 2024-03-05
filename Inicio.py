import streamlit as st
import streamlit.components.v1 as components
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
st.markdown("""
    <style>
        iframe[data-testid="stIFrame"] {
            height: 86vh !important;
        }
    </style>
""", unsafe_allow_html=True)

## Body
header = header()
home = home()

st.markdown(header, unsafe_allow_html=True)
components.html(home)

logo_png = st.image("img/LogoPNG.png")
logo_png.empty()