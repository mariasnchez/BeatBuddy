import streamlit as st
from streamlit.components.v1 import html

with open("./src/css/style.css") as css:
    css_file = css.read()

with open("./src/css/bootstrap.min.css") as css:
    bootstrap = css.read()
# ./node_modules/bootstrap/dist/css/bootstrap.min.css

inicio = f"""
    <head>
        <style>{css_file}</style>
        <style>{bootstrap}</style>
    </head>
    <body>
        <div id="body-container"></div>
    </body>
"""