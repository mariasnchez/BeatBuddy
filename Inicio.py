import streamlit as st
from streamlit.components.v1 import components
from funciones import *

## Configuración
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.set_page_config(
        page_title="BeatBuddy",
        layout="wide"
    )

## Estilos
estilos("./src/css/style.css")
estilos("./src/css/bootstrap.min.css")

## Body
header = header()
inicio = inicio()

st.markdown(header, unsafe_allow_html=True)
st.markdown(inicio, unsafe_allow_html=True)

logo_png = st.image("img/LogoPNG.png")
logo_png.empty()