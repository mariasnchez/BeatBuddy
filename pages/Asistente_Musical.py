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

## Body
header = header2()
asistente = asistente_musical()

st.markdown(header, unsafe_allow_html=True)
st.markdown(asistente, unsafe_allow_html=True)

#
