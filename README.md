# BeatBuddy 🤖
<p align="center">
  <img src="/img/Logo.jpg" width=250/>
</p>

Proyecto realizado por [Christian Martín Díaz](https://github.com/chrismartindiaz), [Pablo Martín Trujillo](https://github.com/martintpablo) y [María Eugenia Sánchez Sánchez](https://github.com/mariasnchez).


Página web: 

## Índice

* [1. Descripción del proyecto ](#1)
* [2. Obtención de los datos](#2)
  * [Asistente musical](#a2)
  * [Reconocimiento facial](#r2)
* [3. Exploración y visualización de los datos](#3)
  * [Asistente musical](#a3)
  * [Reconocimiento facial](#r3)
* [4. Preparación de los datos](#4)
  * [Asistente musical](#a4)
  * [Reconocimiento facial](#r4)
* [5. Entrenamiento del modelo](#5)
  * [Asistente musical](#a5)
  * [Reconocimiento facial](#r5)
* [6. Procesamiento Lenguaje Natural (Voicebot)](#6)
* [7. Aplicación web](#7)
* [8. Porcentaje trabajo realizado](#8)



## 1. Descripción del proyecto <a name="1"></a>
BeatBuddy tratará de una aplicación de música personalizada, que servirá como un asistente musical capaz de proporcionar recomendaciones precisas en base a preguntas en un pequeño **formulario** como lo son el estado de ánimo, la actividad o el año, entre otros parámetros. También tendrá una parte en la que se recomendará una canción respecto a la emoción predicha en un **reconocimiento facial** y otra parte de un **Chat de Voz** similar a *Siri* o *Alexa* con el que se podrá tener una experiencia más completa.

Hemos empleado un gran número de tecnologías para la realización del proyecto, en la siguiente imagen se muestran todas las tecnologías utilizadas:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/1213b8c6-2b6d-4ff2-8486-d2a4c41b97ef)

## 2. Obtención de datos <a name="2"></a>
### ASISTENTE MUSICAL <a name="a2"></a>
Los datos los hemos recogido mediante **scrapping** ([Ver desarrollo scrapping](/archivos/Spotipy_Scrapping.ipynb)) con la función de la [API de Spotify](https://developer.spotify.com/documentation/web-api/reference/get-audio-features) `audio-features` y tienen el siguiente significado:
- **loudness**: Se trata de un campo **float** que mide de **0,0 a 1,0** el nivel de **acústica** de la canción. 1,0 representa una confianza alta en que la pista es acústica.

- **analysis_url**: Se trata de un campo **string** que proporciona la **URL** con los detalles de la canción.

- **danceability**: Se trata de un campo **float** que mide de **0,0 a 1,0** el nivel de **bailabilidad** de una canción en base a una serie de elementos como el tempo, ritmo, potencia del beat... 1,0 representa una confianza alta en que la pista es súper bailable.

- **duration_ms**: Campo **entero** que muestra la **duración de la canción** en **milisegundos**.

- **energy**: Se trata de un campo **float** que mide de **0,0 a 1,0** el nivel de **intensidad o actividad** de la canción. Generalmente las canciones con más volumen o rápidas son más energéticas. 1,0 representa una confianza alta en que la pista es enérgica.

- **id**: ID de la canción en **string**.

- **instrumentalness**: Se trata de un campo **float** que mide de **0,0 a 1,0** la **cantidad** de veces que aparecen  **melodías** frente a las palabras en la canción. 1,0 representa una confianza alta en que la pista es instrumental.

- **key**: Se trata de un campo de tipo **entero** que se refiere a la **clave de la pista**.

- **liveness**: Se trata de un campo **float** que mide de **0,0 a 1,0** el nivel de **audiencia** de la canción. 1,0 representa una confianza alta en que la pista contiene mucha audiencia.

- **loudness**: Se trata de un campo **float** que mide el nivel de **decibelios** de la canción.

- **mode**: Es un campo **entero** que puede ser 1 o 0 que mide la modalidad de la escala en menor o mayor.

- **speechiness**: Se trata de un campo **float** que mide de **0,0 a 1,0** la **cantidad** de veces que aparecen  **palabras** en la canción. 1,0 representa una confianza alta en que la pista es totalmente hablada.

- **tempo**: Se trata de un campo **float** que mide de el tempo estimado de una canción en BPM (beats per minute).

- **time_signature**: Se trata de un campo de tipo **entero** que muestra la cantidad de beats hay en cada línea de canción.

- **track_href**: Un **enlace** directamente a la **API** de Spotify con los detalles de la canción.

- **type**: **String** que mide el **tipo** del objeto.

- **uri**: **String** que muestra la **URI** de la canción.

- **valence**: Se trata de un campo **float** que mide de **0,0 a 1,0** la **positividad** de las **letras** de cada  canción. 1,0 representa una confianza alta en que la canción es positiva al 100%.
- **release_date**: Es un campo tipo **string** que simplemente indica la **fecha de salida** de la canción.

### RECONOCIMIENTO FACIAL <a name="r2"></a>
Los datos del dataset de kaggle *fer2013.csv* del siguiente enlace: https://www.kaggle.com/datasets/ashishpatel26/facial-expression-recognitionferchallenge

En el dataset se encuentran imágenes de 7 expresiones diferentes: enfado, disgusto, miedo, feliz, triste, sorpresa y neutral. Para el reconocimiento nos centraremos en las imágenes de:
- **Tristeza**
- **Felicidad**
- **Neutrales**

## 3. Exploración y visualización de los datos <a name="3"></a>
### ASISTENTE MUSICAL <a name="a3"></a>
[Ver desarrollo](/archivos/Asistente_exploracion_visualizacion.ipynb)

Hemos leído el dataset, visto que no hay valores nulos, hay 137 columnas duplicadas y visualizado las correlaciones.

Gráfica correlación: 

<img src="/img/correlaciones_exploracion.png" width=/>


### RECONOCIMIENTO FACIAL <a name="r3"></a>
[Ver desarrollo](/archivos/Reconocimiento_exploracion_visualizacion.ipynb)

Hemos leído el dataset, visto las claves del diccionario (`emotion`, `pixels`, `Usage`), los tipos de emociones hay (7), el número de imágenes que en cada emoción, y la distribución de emociones.

<img src="/img/distribucion_emociones.png" width=/>

## 4. Preparación de los datos <a name="4"></a>
### ASISTENTE MUSICAL <a name="a4"></a>
[Ver desarrollo](/archivos/Asistente_preparacion_datos.ipynb)

Hemos eliminado los duplicados; utilizado técnicas de *Featuring Engineering* para la **eliminación de columnas innecesarias**, **distingir columnas**, **cambiar nombres**, **eliminación de outliers** y **eliminación de datos vacíos/nulos**; y mostrado las correlaciones tras el tratamiento. 

Gráfica correlaciones **tras el tratamiento de datos**:

<img src="/img/correlaciones_preparacion.png" width=/>


### RECONOCIMIENTO FACIAL <a name="r4"></a>
[Ver desarrollo](/archivos/Reconocimiento_preparacion_datos.ipynb)

Hemos borrado la columna `Usage` ya que no la necesitamos, elegido las imágenes con emociones `feliz`, `triste` y `neutral` y eliminado los duplicados.

## 5. Entrenamiento del modelo <a name="5"></a>
### ASISTENTE MUSICAL <a name="a5"></a>
[Ver desarrollo](/archivos/Asistente_entrenamiento.ipynb)

#### Entrenamiento para el target `mood`
Probamos con:
- SVClassifier (58% precisión)
- KneighborsClassifier (79% precisión)
- Regresión Logística (98,75% precisión) **Modelo elegido**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/1a159cf5-e6ae-457b-98eb-b40c91dca72a)

#### Entrenamiento para el target `motivation`
Probamos con:
- SVClassifier (80% precisión)
- LinearSVC (98% precisión) **Modelo elegido**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/987c532d-95eb-4578-975f-31985c9795b2)


Hemos añadido 100 canciones más por década musical y los unimos a los modelos. 

### RECONOCIMIENTO FACIAL <a name="r5"></a>
[Ver desarrollo](/archivos/Reconocimiento_preparacion_datos.ipynb)

Hemos entrenado el modelo con **redes neuronales** utilizando tensorflow y keras. Ha dado aproximadamente un 73% de precisión, pero nos quedamos con el modelo ya que las predicciones que ha fallado son las que no se identifica bien la cara que han puesto. Mientras se muestre claramente la cara, el modelo lo predice correctamente.

![73_Porciento_Reconocimiento](https://github.com/mariasnchez/BeatBuddy/assets/146923531/26c5060f-3f26-4ad2-b745-fcb7ff6bad05)


Aquí un ejemplo con las primeras 64 imágenes (las negras son las predicciones correctas y las naranjas las falladas): 

<img src="/img/entrenamiento.png" width=/>

## 6. Procesamiento Lenguaje Natural (Voicebot) <a name="6"></a>
Para el NPL hemos decidido hacer un **voicebot**, pero no un voicebot cualquiera, sino un **asistente de voz** similares a los de **Siri** de *Apple* o a **Alexa** de *Amazon*. Para su realización hemos usado las siguientes **librerías**:

* **Google Generative AI**: Es el **motor** del voicebot, aporta la funcionalidad de realizar y responder preguntas de forma interactiva con un **prompt adecuado** para que trabaje de forma correcta.
* **TempFile**: Se va a encargar de **almacenar temporalmente** las **grabaciones de voz** durante la ejecución del asistente para a posteriori, **reproducirlas al usuario**.
* **audiorecorder**: Facilita la **grabación de audios** en **Streamlit**, ésta librería se encargará de **capturar y procesar** las **grabaciones de voz** de **entrada** del usuario. 
* **Whisper**: Es el encargado de una vez se ha **realizado y almacenado temporalmente el audio**, **transcribirlo** convirtiéndolo en **texto** para que lo **entienda** el **asistente** y **genere** el **prompt**.
* **gTTS**: Una vez **generado el prompt**, lo **último** que queda es **convertir la respuesta proporcionada** de texto **en audio**, éste audio será **reproducible y pausable** cuando usuario quiera. Además, podrá **cambiar la velocidad de reproducción**.

**¿Cómo hemos realizado el Voicebot?**
1. En primer lugar, hemos llamado a nuestra **API Key de Google Gemini-Pro**.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/aa5527ee-874b-42d1-bc22-c790174694ea)

2. A continuación, deberemos de **inicializar** el Voicebot, para ello, crearemos un **prompt inicial** que moldeará la **estructura** del asistente y crearemos un **historial** que irá **almacenando respuestas**.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/43b5e45a-32d1-4ee2-8721-e4b99fb85c39)

3. Creamos el **botón** para **grabar** el **audio** de entrada del usuario y un **selector** para el **idioma** que desee **realizar la consulta** del **usuario**. Por último, establecemos el modelo de **Whisper Base** puesto que es **el más completo** para enviar audios de unos 10 segundos. 

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/7d6f7ac0-bba3-483b-b5c6-ca1da8275e28)

4. En caso de que el **audio** se grabe de forma **correcta** y su duración sea mayor a 0 milisegundos se **guardará temporalmente** para por último **reproducir la respuesta** generada del **prompt** con **gTTS** y **reproducirla automáticamente**.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/d33b1b17-5f7d-455a-adfb-8c8ec2ac96e8)

## 7. Aplicación web <a name="7"></a>
El prototipo de la web lo diseñamos en Figma que se puede ver [aquí](https://www.figma.com/file/R5yJphUSRoNuWchBIt2ZaH/TFM?type=design&node-id=0-1&mode=design&t=aop7T6jbd598DzHx-0).

Nuestra página ha sido desarrollada en Streamlit.

Se han usado tecnologías como `HTML`, `CSS`, `JavaScript` y `Bootstrap`. También hemos usado `components.html()` que nos permite crear componentes de Streamlit, donde podemos utilizar `Animejs`, una librería de JavaScript para realizar animaciones. 

Junto a todo esto, encontramos componentes de Streamlit como `streamlit-image-select`, que nos permite crear una galería de imágenes donde seleccionar una, como si de un checkbox se tratase, y `streamlit-audiorecorder`, que nos ayuda a comunicarnos con nuestro VoiceBot mediante voz.

A la hora de aplicar estilos, podemos hacerlo mediante `st.markdown(<html>, unsafe_allow_html=True)`. Para no llenar los archivos de las páginas con mucho código, hemos creado un archivo llamado `funciones.py`, que importamos en las páginas, donde tenemos funciones que devuelven un código `html` en un string, que luego metemos en `st.markdown()` para que las cargue en la página.

He aquí algunos ejemplos para:
* Cargar los estilos:
  
  `funciones.py`
  
  <img src="/img/style_function.png"/>
  
  `Inicio.py` o otras páginas
  
  <img src="/img/cargar_style.png"/>
  
* Cargar las fuentes:
  
  `funciones.py`
  
  <img src="/img/fuentes_function.png"/>
  
  `Inicio.py` o otras páginas
  
  <img src="/img/cargar_fuentes.png"/>

* Cargar partes de la página, como por ejemplo el header:
  
  `funciones.py`
  
  <img src="/img/header_function.png"/>
  
  `Inicio.py` o otras páginas
  
  <img src="/img/cargar_header.png"/>

Así es como estructuramos la página web BeatBuddy. 

Éste es el resultado final de la página de inicio de la web en Streamlit:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/2748e54b-877f-4278-86a3-cc44e564cd1d)

## 8. Porcentaje trabajo realizado <a name="8"></a>

Hemos trabajado todos por igual, no hay ninguna queja por parte de ninguno de los integrantes del grupo.

Christian: 33%  
María: 33%  
Pablo: 33%  
