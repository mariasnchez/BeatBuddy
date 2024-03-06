# BeatBuddy 🤖
<p align="center">
  <img src="/img/Logo.jpg" width=250/>
</p>

Proyecto realizado por [Christian Martín Díaz](https://github.com/chrismartindiaz), [Pablo Martín Trujillo](https://github.com/martintpablo) y [María Eugenia Sánchez Sánchez](https://github.com/mariasnchez).


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
* [8. Vídeo](#8)
* [9. Presentación](#9)
* [10. Porcentaje trabajo realizado](#10)



## 1. Descripción del proyecto <a name="1"></a>
BeatBuddy trata de una aplicación de música personalizada, que servirá como un asistente musical capaz de proporcionar recomendaciones precisas en base a preguntas en un pequeño **formulario** como lo son el estado de ánimo, la actividad o el año. También tendrá una parte en la que se recomendará una canción respecto a la emoción predicha en un **reconocimiento facial** y otra parte de un **Chat de Voz** similar a *Siri* o *Alexa* con el que se podrá tener una experiencia más completa.

Hemos empleado un gran número de tecnologías para la realización del proyecto, en la siguiente imagen se muestran todas las tecnologías utilizadas:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/1213b8c6-2b6d-4ff2-8486-d2a4c41b97ef)

## 2. Obtención de datos <a name="2"></a>
### ASISTENTE MUSICAL <a name="a2"></a>
Los datos los hemos recogido mediante **Scraping** ([Ver desarrollo scraping](/archivos/Spotipy_Scrapping.ipynb)) con la función de la [API de Spotify](https://developer.spotify.com/documentation/web-api/reference/get-audio-features) `audio-features`.

En primer lugar, hemos importado las librerías:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/7c6d54b1-b3ff-48b7-9b35-66075b69eab1)

Luego, sacamos los **metadatos** de las canciones de una playlist.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/578fe6c9-f367-4eb5-b5e6-f0e0b28d0a9f)

Guardamos en un array valores que nos pueden ser interesantes para listar las canciones como lo son el ID, el nombre(meramente informativo) y la fecha de salida de la canción.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/33fbd103-1c1a-44c4-b4e4-f97203560fe3)

En este caso, vamos a sacar los **datos objetivos** de la canción y los guardamos en un DataFrame de Pandas

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/f922f879-4ded-45ba-85b0-e8e5a24013d0)

Hemos **repetido éste proceso 12** para **12 playlists** distintas:

- 3 Playlists de canciones tristes (278 canciones)

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/32db9b43-68ab-42a9-a7aa-f0498b950562)


- 3 Playlists de canciones felices (283 canciones)

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/3218fd44-e3bf-4958-8dcb-8164a028c95c)

- 3 Playlists de canciones para estar relajado (300 canciones)

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/58275d02-80af-4815-be96-a1c36021c11b)

- 3 Playlists de canciones para motivarte (277 canciones)

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/9c4ed2ab-35ad-4e0a-b088-b7583477ac83)

Adicionalmente a éstas, hemos sacado 500 canciones más de distintas décadas músicales que no contendrán emoción pero sí que serán etiquetadas a posteriori con el modelo que entrenaremos.

- 100 canciones de los años 80:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/86816cbf-e666-487f-a5c9-1f5b089be54c)

- 100 canciones de los años 90:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/c7d61e65-a9fc-4280-9f08-326e0e9147f4)

- 100 canciones de los 2000s:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/ba20d668-74d8-4556-8ab8-b52449cb961f)

- 100 canciones de los 2010s:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/520317b8-ca05-421a-9f4b-f21c2ae47d09)

- 100 canciones de los 2020s:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/3b04fe0e-1d95-4dbd-ab23-c38354307da7)

En **total** se han scrapeado unas ***1800 canciones*** de distintos estados de ánimo, energías y décadas musicales. Al rededor de unas **20 playlists de 90 canciones** cada una.
Los valores que Spotify da a cada una de las canciones se muestra en las columnas que hemos recogido en el DataFrame, que contienen el siguiente **significado**:

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
Los datos para el reconocimiento facial lo hemos sacado de un dataset bastante conocido en el mundo del reconocimiento facial. Se trata del dataset de kaggle *fer2013.csv* del siguiente enlace: https://www.kaggle.com/datasets/ashishpatel26/facial-expression-recognitionferchallenge
Éste dataset se lleva utilizando bastante tiempo para reconocimiento facial en otros ámbitos, nosotros vamos a implementarlo en el mundo de la música.

En el dataset se encuentran imágenes de 7 expresiones diferentes: enfado, disgusto, miedo, feliz, triste, sorpresa y neutral. Para el reconocimiento nos centraremos en las imágenes de:
- **Tristeza**
- **Felicidad**
- **Neutrales**

## 3. Exploración y visualización de los datos <a name="3"></a>
### ASISTENTE MUSICAL <a name="a3"></a>
[Ver desarrollo](/archivos/Asistente_exploracion_visualizacion.ipynb)

En primer lugar, veremos el conjunto de datos que tenemos en el DataFrame con las canciones que Spotify considera que van relacionadas a una emoción.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/5b8ab209-a83e-4a20-bd4b-badb6979d7a1)

Comprobamos que no haya valores nulos

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/5d0392c6-b7e0-4059-9973-4c1dda5bb069)

**No hay valores nulos** en el DataFrame por lo tanto continuamos con la visualización de valores duplicados.

Vemos que hay 137 columnas duplicadas y visualizado las correlaciones.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/4fbc4899-95e1-45df-b6b7-d57b41e9f137)

Vamos a observar en una **tabla** las correlaciones entre los valores de las columnas antes de ser tratadas.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/9d4c5855-484e-4782-9ece-e3ae06273204)

Gráfica correlación: 

<img src="/img/correlaciones_exploracion.png" width=/>

Podemos sacar los siguientes datos que pueden ser interesantes a la hora de sacar **conclusiones** para el entrenamiento del modelo.

Destacamos la correlación que existe entre las columnas:

- **loudness + energy** (81%): Con estos valores tenemos claro que existe **mucha complicidad** con los valores, cuando una canción tiene un **mayor volumen** existe **mayor posibilidad** de que esa canción se considere **enérgica**, éste dato es **fundamental** puesto que elegirá cuando una **canción es enérgica o** por lo contrario, es más **relajada**.

- **acousticness + energy** (-83%): Existe una correlación **fuerte negativa del 83%** entre `acousticness` y `energy`. Esto indica que, en general, cuando la **probabilidad** de que una canción sea **acústica** **aumenta**, la **intensidad y actividad** percibida de la **canción (energy)** tiende a **disminuir**. Resumiendo, hay una **tendencia** de que las **canciones más acústicas** tiendan a ser **menos energéticas**, y viceversa.

- **acousticness + loudness** (-67%): Sucede algo parecido a la anterior pues la probabilidad de que una canción sea **acústica** y al mismo tiempo tuviera **mucho volumen** es muy baja. Podemos decir que las canciones **más acústicas** tienen menor **volumen**.

- **valence + danceability** (53%): Como podemos ver, hay cierta complicidad en éstos valores, podemos decir que una canción más bailable, por lo general tendrá letras más positivas, éstos datos serán más interesantes a la hora de entrenando el modelo para decidir cuando una canción es feliz o triste.

### RECONOCIMIENTO FACIAL <a name="r3"></a>
[Ver desarrollo](/archivos/Reconocimiento_exploracion_visualizacion.ipynb)

Hemos leído el dataset, visto las claves del diccionario (`emotion`, `pixels`, `Usage`), los tipos de emociones hay (7), el número de imágenes que en cada emoción, y la distribución de emociones.

<img src="/img/distribucion_emociones.png" width=/>

## 4. Preparación de los datos <a name="4"></a>
### ASISTENTE MUSICAL <a name="a4"></a>
[Ver desarrollo](/archivos/Asistente_preparacion_datos.ipynb)

En cuanto a la preparación de los datos del asistente musical hemos empleado un gran número de técnicas para que el modelo sea lo más eficaz posible y los datos se muestren de forma intuitiva para los usuarios.

- **Eliminación de los duplicados.**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/aea39c94-4daf-4e34-b748-e750dfa67364)

- **Eliminación de columnas innecesarias.**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/46bc93a1-b861-47bc-9a7e-513076517197)

- **Distinción de columnas y cambios en el nombre.**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/12a65e59-88f7-4ba8-bf4e-9598c2e74d94)

- **Reajuste de valores para las columnas.**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/0c812626-60c2-4a62-8eae-0ea02a542d80)

- **Eliminación de datos outliers.**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/c2ba86d4-8c36-48b8-a4d3-09582db74896)
  
- **Eliminación de datos vacíos/nulos.**

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/36fb828f-149c-49d4-b22c-69e4ea5f5a3a)

- **Muestra de las nuevas correlaciones tras el tratamiento de los datos.** 

Gráfica de las correlaciones **tras la preparación de los datos**:

<img src="/img/correlaciones_preparacion.png" width=/>

Como podemos observar, han aparecido nuevas correlaciones que aportarán mucha precisión al modelo.

**motivation + energy** (94%): Con estos valores tenemos claro que existe **mucha complicidad** con los valores, cuando una canción tiene un **mayor índice de energía** existe **mayor posibilidad** de que esa canción se considere **enérgica o motivadora**, éste dato es **fundamental** puesto que elegirá cuando una **canción es enérgica o** por lo contrario, es más **relajada**.

**motivation + loudness** (78%): Con estos valores tenemos claro que existe **buena complicidad** con los valores, cuando una canción tiene un **mayor volumen** existe **mayor posibilidad** de que esa canción se considere **enérgica o motivadora**, éste dato es **fundamental** puesto que elegirá cuando una **canción es enérgica o** por lo contrario, es más **relajada**.

**mood + valence** (93%): Con estos valores tenemos claro que existe **bastante complicidad** con los valores, cuando una canción tiene una **letra más positiva** existe **mayor posibilidad** de que esa canción se considere **happy (feliz)**, éste dato es **fundamental** puesto que elegirá cuando una **canción es feliz o** por lo contrario, es más **triste**.

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


Hemos añadido las 100 canciones más por década musical y las hemos unido al DataFrame con los modelos previamente entrenados.

- Entrenamos y etiquetamos:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/e5cca66b-461e-4925-80a4-0f90a83ba109)

- Unimos ambos DataFrame:

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/5f0b6804-64e0-4dfa-9b2d-b3cc8cb2e44b)

- Tras unirlos hemos eliminado los duplicados.

- **Más gráficas** interesantes tras el tratamiento final de los de datos:

En primer lugar, crearemos una gráfica con la comparativa del número de canciones que hay por década musical

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/56729b87-625b-4c73-8a45-4482bd2c1d54)

En segundo lugar, vamos a crear una gráfica que muestre la cantidad de canciones felices que hay por década musical y así poder comparar cuál es la que más canciones felices tiene.

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/7ffc5d65-7374-4cad-ba31-1e430bf65928)

Como vemos no existe especial correlación entre el número de canciones motivadoras con las felices, que una canción se considere "feliz" no hace automáticamente que se considere "motivadora".

En tercer, lugar puede ser interesante mostrar una gráfica que indique el número total de canciones por clasificación de etiquetas diferenciándolas por las 2 categorías principales (sin contar el año de salida), **mood y motivation**.  

![image](https://github.com/mariasnchez/BeatBuddy/assets/146923531/4ba3e35a-a90f-414e-bd8c-d92c4a14bf42)

Observando la gráfica podemos sacar las siguiente conclusiones:

- La **mayoría** de las canciones son **felices y motivadoras** con un **42,7%** del número total de las canciones del dataset.
- La categoría con **menos canciones** son las **felices y relajadas** con un **2,4%**, lo que vienen a ser **28 canciones en todo el dataset**.
- Las canciones **tristes**, ya sean motivadoras o más tranquilas **mantienen la proporción** en cierta medida puesto que **varían en un 10%** (**32,2% y 22,7%**).

Podemos concluir esta gráfica afirmando que si una canción es feliz existen muchas más posibilidades de que la canción sea motivadora, sin embargo, una canción que tenga una letra triste, no tiene porqué asimilarse a ser más relajada puesto que sus proporciones son más equilibradas.


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
**Página web:**  

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

## 8. Vídeo <a name="8"></a>

## 9. Presentación <a name="9"></a>

## 10. Porcentaje trabajo realizado <a name="10"></a>

Hemos trabajado todos por igual, no hay ninguna queja por parte de ninguno de los integrantes del grupo.

Christian: 33%  
María: 33%  
Pablo: 33%  
