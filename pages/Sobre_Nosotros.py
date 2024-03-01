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

header = header2()
sobre_nosotros = sobre_nosotros()

st.markdown(header, unsafe_allow_html=True)
st.markdown(sobre_nosotros, unsafe_allow_html=True)

linkedin = st.image("img/linkedin.png")
github = st.image("img/github.png")

linkedin.empty()
github.empty()