import streamlit as st

def header():
    return """
        <div id="header" class="d-flex justify-content-end align-items-center pe-2 pt-2">
            <div class="link-div fs-4 me-3"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Asistente_Musical" target="_self">Asistente Musical</a></div>
            <div class="link-div fs-4 me-3"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Reconocimiento_Facial" target="_self">Reconocimiento facial</a></div>
            <div class="link-div fs-4 me-3"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Chatbot" target="_self">Chatbot</a></div>
            <div class="link-div fs-4"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Sobre_nosotros" target="_self">Sobre nosotros</a></div>
        </div>
    """

def header2():
    return """
        <div id="header" class="d-flex justify-content-end align-items-center pe-2 pt-2">
            <div class="logo">
                <a href="https://beatbuddyapp.streamlit.app"><img src="https://beatbuddyapp.streamlit.app:443/~/+/media/cdf0488c738115d7f79bedc0dbba33fcddaf432f3e57a3d5eea75553.png" alt="Logo"></a>
            </div>
            <div class="link-div fs-4 me-3"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Asistente_Musical" target="_self">Asistente Musical</a></div>
            <div class="link-div fs-4 me-3"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Reconocimiento_Facial" target="_self">Reconocimiento facial</a></div>
            <div class="link-div fs-4 me-3"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Chatbot" target="_self">Chatbot</a></div>
            <div class="link-div fs-4"><a class="header-link" href="https://beatbuddyapp.streamlit.app/Sobre_nosotros" target="_self">Sobre nosotros</a></div>
        </div>
    """



def inicio():
    return f"""
        <div id="inicio-body" class="d-flex justify-content-evenly align-items-center mt-5 px-5">
            <div class="w-50 h-75 d-flex justify-content-center align-items-center">
                <img id="inicio-img" src="https://beatbuddyapp.streamlit.app:443/~/+/media/cdf0488c738115d7f79bedc0dbba33fcddaf432f3e57a3d5eea75553.png" alt="BeatBuddy" draggable="false"/>
            </div>
            <div id="inicio-beatbuddy" class="w-50 h-75 d-flex flex-column justify-content-evenly align-items-center">
                <div id="inicio-titulo" class="w-75 fs-1 text-center text-white">Lorem Ipsum dolor</div>
                <div id="inicio-texto" class="w-75 fs-3 text-center text-white">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper, felis et elementum efficitur, velit ipsum congue tellus, sit amet placerat massa tellus at sem. </div>
                <a id="btn-empezar" class="px-5 py-3 rounded fs-5 text-center shadow" target="_self" href="https://beatbuddyapp.streamlit.app/Asistente_Musical">¡Empieza aquí!</a>
            </div>
        </div>
    """
    
def reconocimiento():
    return f"""
        <div id="recog-body" class="d-flex justify-content-evenly align-items-center mt-5 px-5">
            <div id="inicio-beatbuddy" class="w-75 h-25 d-flex flex-column justify-content-evenly align-items-center">
                <div class="w-200 fs-2 text-center text-white"><b>Reconocimiento facial</b></div>
                <div id="inicio-texto" class="w-75 fs-5 text-center text-white">Sube una imagen o toma una foto con tu cámara para que el programa identifique tu emoción y escoja una canción acorde a tu sentimiento.</div>
            </div>
        </div>
    """

def prediccion(predicted_emotion):
    return f"""
        <div id="inicio-beatbuddy" class="w-200 h-3 d-flex flex-column justify-content-evenly align-items-center">
            <div class="w-200 fs-5 text-center text-white">Parece ser que estás:<b> {predicted_emotion.upper()}</b></div>
            <div class="w-200 fs-2 text-center text-white">TU CANCIÓN IDEAL ES...</div>
        </div>
    """

def estilos(ruta):
    with open(ruta) as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html = True)
