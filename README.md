
 
 # <h1 align="center"> StreamRec Movie Recommendation System</h1>

El proyecto "StreamRec" es un sistema de recomendación de películas y series diseñado para plataformas de streaming. El objetivo principal es proporcionar recomendaciones personalizadas a los usuarios, ayudándoles a descubrir contenido relevante y aumentar su satisfacción con el servicio.


![GIFF](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/76eb291c-77fe-44b5-b0c4-a47129a108b9) 




            


# <h2 align='left'> 0. Roadmap</h2>

En esta Parte mostraremos el  roadmap  que proporciona una visión general del proyecto, permitiendo a los miembros del equipo y a las partes interesadas comprender el plan general, identificar las tareas prioritarias y coordinar los esfuerzos. También nos ayudará a mantener el enfoque en los objetivos del proyecto y facilitará la toma de decisiones estratégicas.
![graph (1)](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/19f87ca0-4605-4c00-a108-4c80f93b9e4e)




# <h2 align='left'> 1. Descripción del Proyecto</h2>

![preview](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/c80f9b1b-92af-4f14-87cb-d84aed6bc123)



<p align="justify">
El proyecto aborda el desafío de trabajar con datos poco maduros, donde se requiere un trabajo rápido de Data Engineering para transformar los datos anidados y establecer procesos automatizados de actualización para incorporar nuevas películas y series. Este enfoque permitirá ofrecer recomendaciones actualizadas y precisas a medida que se agregue contenido nuevo a la plataforma.
El sistema utilizará técnicas de Machine Learning, en particular el modelo de recomendación basado en el algoritmo SVD (Singular Value Decomposition), que permitirá analizar el historial de visualización de los usuarios y encontrar patrones para generar recomendaciones personalizadas. Además, se implementará una interfaz de usuario amigable donde los usuarios podrán explorar recomendaciones, calificar películas y series, y recibir nuevas sugerencias en función de sus preferencias.
El proyecto busca proporcionar un MVP (Minimum Viable Product) en un plazo de tiempo acelerado, permitiendo a la start-up lanzar su sistema de recomendación y ofrecer una experiencia mejorada a sus usuarios. Con el tiempo, se espera ampliar y mejorar el sistema, incorporando nuevos algoritmos de recomendación y funciones adicionales para enriquecer la experiencia del usuario.
</p>

# <h2 align='left'> 2. Background</h2>
![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/b728f437-2f5a-4e73-abaa-5f22e02d7570)

<p align="justify">
El proyecto surge en el contexto de una start-up que ofrece servicios de agregación de plataformas de streaming. La empresa se enfrenta al desafío de proporcionar recomendaciones personalizadas a sus usuarios, con el objetivo de mejorar la experiencia de usuario y aumentar la retención.
Anteriormente, la empresa no contaba con un sistema de recomendación implementado y los datos disponibles para este fin eran escasos y poco estructurados. La falta de procesos automatizados para la actualización de nuevas películas o series y la falta de transformación de los datos dificultaban la tarea de crear un modelo de recomendación efectivo.
Ante esta situación, el equipo de Data Science se propone desarrollar un sistema de recomendación desde cero, realizando tareas de Data Engineering para transformar y organizar los datos, así como desarrollar una API para interactuar con el modelo de recomendación. El objetivo es crear un MVP (Minimum Viable Product) en un plazo de tiempo reducido para poner en marcha el sistema de recomendación y comenzar a obtener retroalimentación de los usuarios.
El proyecto busca superar los desafíos de madurez de los datos, implementar procesos automatizados para la actualización de información y aprovechar técnicas de aprendizaje automático para generar recomendaciones personalizadas y precisas. Con esto, la empresa espera mejorar la satisfacción de los usuarios y fortalecer su posición en el mercado de servicios de streaming.
</p>
# <h2 align='left'> 3. Problemática</h2>

 ![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/e90ccafb-3f55-4efa-8473-e78ba2afbd1e)

<p align="justify">
La problemática en el proyecto es la falta de madurez y estructura en los datos de plataformas de streaming, lo que dificulta la creación de un sistema de recomendación efectivo. Los datos están desorganizados, no hay procesos automatizados para la actualización de nuevos contenidos y se requiere un trabajo rápido de Data Engineering para transformar los datos y crear un MVP funcional. Esta falta de estructura y procesos eficientes dificulta el desarrollo y despliegue de un sistema de recomendación eficaz, lo que representa un desafío para el equipo de Data Science.
Los datos presentados son una lista de diccionarios en formato JSON. Cada diccionario representa a una persona involucrada en un proyecto de Data Science, con información como su identificador, nombre, género, departamento, trabajo y ruta de perfil.La estructura de los datos es una lista, donde cada elemento de la lista es un diccionario con campos específicos que representan diferentes atributos de una persona.Un posible problema con esta estructura de datos es que puede resultar difícil de manejar y analizar, especialmente si se deseamos realizar consultas específicas o aplicar algoritmos de procesamiento de datos. Por ejemplo, si se desea filtrar las personas por su departamento o género, puede requerir iterar sobre la lista y realizar operaciones de búsqueda. Además, la falta de un esquema estructurado puede dificultar la validación y la consistencia de los datos.En general, para un análisis más eficiente y una manipulación más sencilla de los datos, se tuvo que convertirlos en una estructura tabular, como un dataframe, donde cada columna represente un atributo y cada fila represente una persona. Esto permitirá realizar consultas y operaciones más fácilmente, utilizando herramientas y bibliotecas específicas para el análisis de datos en lugar de tener que escribir código personalizado.
</p>
# <h2 align='left'> 4. Pipeline Del Proyecto "StreamRec"</h2>

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/8dca094d-b5f8-4c2b-9188-fb235221699d)


# <h5 align='left'> a.Extracción y preprocesamiento de datos (ETL)</h5>
 
.Extracción de datos de fuentes de streaming.
 
.Limpieza y transformación de datos.
 
# <h5 align='left'> b.Análisis exploratorio de datos (EDA)</h5>
 
.Exploración de la estructura y distribución de los datos.
 
.Identificación de patrones y tendencias.

# <h5 align='left'> c.Desarrollo de la API</h5>
 
.Diseño de los endpoints de la API.
 
.Implementación de la lógica de recomendación.
 
.Exposición de la API para acceso externo.
 
# <h5 align='left'> d.Entrenamiento del modelo</h5>
 
.Selección del algoritmo de recomendación
 
.Ajuste de parámetros del modelo
 
.Validación cruzada y evaluación de rendimiento
 
# <h5 align='left'> e.Evaluación y ajuste del modelo</h5>
 
.Cálculo de métricas de evaluación (RMSE, MAE)
 
.Ajuste de hiperparámetros para mejorar la precisión
 
# <h5 align='left'> f.Implementación y despliegue</h5>
 
.Configuración de servidores y recursos
 
.Integración con otros componentes del sistema

# <h2 align='left'> 5. Elección del Stack tecnológico </h2>

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/d60436aa-18fd-4047-991d-5c98a061d22b)

<p align="justify">
Este trabajo se basó en tener un desarrollo suficientemente ágil para tener rápidamente  un prototipo, pero lo suficientemente robusto para escalar.
En base a esto se decidió utilizar las siguientes tecnologías: Tensorflow, Python, Google Colab y la nube de HuggingFace.
Esto dio como resultado una página web y una API, desarrollando la infraestructura que nos permite  reentrenar o modificar  modelos y desplegarlos rápidamente a bajo costo.
 
 El stack tecnológico para el proyecto incluye las siguientes herramientas y tecnologías:

.Visual Studio Code: Un potente editor de código que proporciona una interfaz amigable y funcionalidades avanzadas para el desarrollo de software.

.FastAPI: Un framework de desarrollo de API rápido y moderno, construido sobre el estándar de tipado de Python. Permite construir API eficientes y escalables utilizando Python de forma sencilla.

.Google Colab: Un entorno de desarrollo basado en la nube que permite la ejecución de código en notebooks de Jupyter. Colab proporciona recursos computacionales y acceso a bibliotecas populares para el entrenamiento y desarrollo de modelos de machine learning.

.Hugging Face: Una plataforma que ofrece herramientas y bibliotecas para el desarrollo y despliegue de modelos de lenguaje natural. Permite el entrenamiento, evaluación y despliegue de modelos de manera sencilla.

.GitHub: Una plataforma de control de versiones que facilita la colaboración y el seguimiento de cambios en el código fuente del proyecto. Permite el almacenamiento y compartición de repositorios de código, así como la gestión de ramas, problemas y solicitudes de extracción.
 
.Pandas: Una librería de análisis de datos en Python que proporciona estructuras de datos flexibles y eficientes para trabajar con datos tabulares.

.NumPy: Una librería fundamental para la computación numérica en Python. Proporciona un soporte eficiente para operaciones matemáticas en matrices y arreglos multidimensionales.

.Matplotlib: Una librería de visualización de datos en Python que permite crear gráficos y visualizaciones estáticas, como gráficos de líneas, barras, dispersión, histogramas, entre otros.

.Seaborn: Una librería de visualización de datos basada en Matplotlib, que proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos y informativos.

.Scikit-learn: Una librería de aprendizaje automático en Python que proporciona una amplia gama de algoritmos y herramientas para el preprocesamiento de datos, la selección de características, el entrenamiento de modelos y la evaluación del rendimiento.

.Surprise: Una librería de Python diseñada para construir y evaluar sistemas de recomendación. Proporciona una amplia gama de algoritmos y utilidades para trabajar con datos de recomendación.

Estas herramientas proporcionan un conjunto sólido de tecnologías para abordar los distintos aspectos del proyecto, desde el desarrollo de la API con FastAPI, el entrenamiento y desarrollo del modelo en Colab, hasta el despliegue del modelo en Hugging Face y el control de versiones del código en GitHub.
</p>

# <h2 align='left'> 6. Conjunto De Datos</h2>
![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/23baa831-4ea4-4a5a-9cbc-c9545dcc1045)



<p align="justify">
Los procedimientos de limpieza que se realizaron a los dos archivos CSV (movies_dataset.csv y credits.csv) antes de unirlos incluyeron varias etapas:

.Extracción de datos relevantes: Se seleccionaron las columnas necesarias de cada archivo que eran relevantes para el análisis conjunto. En el archivo movies_dataset.csv, se extrajeron las columnas: 'id', 'original_title', 'genres', 'popularity', 'vote_average', y 'vote_count'. En el archivo credits.csv, se extrajeron las columnas: 'id', 'cast', y 'crew'.

.Tratamiento de valores faltantes: Se verificó si había valores faltantes en las columnas seleccionadas y se decidió cómo manejarlos. Por ejemplo, si había valores faltantes en la columna 'cast' o 'crew' del archivo credits.csv, se podrían reemplazar por valores nulos o eliminar las filas correspondientes.

.Conversión de datos: Se verificó el tipo de datos de cada columna y se realizó cualquier conversión necesaria para asegurar la coherencia de los datos. Por ejemplo, las columnas 'popularity', 'vote_average' y 'vote_count' se convirtieron en números decimales o enteros según corresponda.

.Limpieza de texto: Se aplicaron técnicas de limpieza de texto para eliminar caracteres no deseados, espacios en blanco adicionales o formato incorrecto en las columnas de texto, como 'original_title', 'genres' y 'cast'. Esto podría incluir eliminar puntuación, convertir a minúsculas, eliminar espacios adicionales, etc.

.Unión de datos: Una vez que los dos archivos CSV se limpiaron y se seleccionaron las columnas relevantes, se realizó la unión de los datos utilizando la columna 'id' como clave de unión. Esto permitió combinar la información de actores y equipos de producción del archivo credits.csv con los detalles de la película del archivo movies_dataset.csv. y esto dio lugar al dataset final para nuestro modelo merged_data6.csv.
 
 .Versionamiento de los datasets: En este link encontrarás los versionamientos trabajados de los datasets a lo largo del proyecto[Click para su descarga--->]
 [![Open In Kaggle](https://cdn.icon-icons.com/icons2/2699/PNG/96/kaggle_logo_icon_168474.png)](https://www.kaggle.com/datasets/davidhspinal/streamrec-movie?select=movies_dataset.csv)
</p>


# <h2 align='left'> 7. EDA</h2>
<p align="justify">
.Carga de datos: Se importaron los conjuntos de datos relevantes para su proyecto.

.Exploración inicial: Se examinaron las dimensiones de los conjuntos de datos y se inspeccionaron algunas filas para comprender la estructura y el contenido de los datos.

.Limpieza de datos: Se llevaron a cabo acciones de limpieza, como el manejo de valores faltantes, duplicados o inconsistentes en los conjuntos de datos.

.Análisis de variables: Se realizó un análisis detallado de las variables relevantes, centrándose en el género de las películas. Se identificó el género con el mayor puntaje final y se seleccionaron los cuatro géneros principales: 'Drama', 'Comedy', 'Horror' y 'Romance'. Estos géneros se utilizaron para un análisis más profundo.
![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/ab4db31e-ac89-4cf3-920d-36f2f77061ac)


.Conversión de género en variables dummy: La columna de género se convirtió en variables dummy para representar si a los usuarios les gusta o no un género específico. Se asignó el valor 1 si les gusta el género y 0 si no les gusta.
 
 ![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/72f79b25-4d6a-4373-a142-c11d998498c4)


.Trabajo con las columnas "vote_average", "vote_count" y "popularity": Estas tres columnas se utilizaron para calcular el puntaje combinado de las películas. Se asignaron pesos a cada columna, lo que permitió enfocarse en diferentes aspectos. Por ejemplo, se podría asignar un peso mayor a "vote_count" y "popularity" para destacar la popularidad de las películas, y un peso menor a "vote_average" para considerar la calificación promedio.

.Cálculo del puntaje final: Se sumaron o promediaron las puntuaciones ponderadas de las columnas mencionadas anteriormente para obtener un puntaje final. Este puntaje final se asignó a una nueva columna llamada "score_final".
![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/79e20eca-597a-4819-b78d-bc65a263716c)

 
 </p>
 
 
# <h2 align='left'> 8. Training </h2>

<p align="justify">
El algoritmo elegido para nuestro modelo fue SVD (Descomposición de Valores Singulares) en la biblioteca Surprise. A continuación, se explica los detalles y justificación del uso del algoritmo y el proceso de entrenamiento:

Carga de datos: El conjunto de datos se carga desde el archivo CSV ('merged_data6.csv') en un DataFrame de pandas llamado dfmerge.

Creación de un objeto Reader: Se crea un objeto Reader especificando la escala de calificación de las películas. En este caso, se utiliza el puntaje final como escala, que se obtuvo previamente en el análisis exploratorio de datos (EDA). El rango de la escala se define utilizando el valor mínimo y máximo del puntaje final en el DataFrame dfmerge.

Carga de datos en el formato Surprise: Se carga el conjunto de datos en el formato requerido por la biblioteca Surprise utilizando el método load_from_df() de la clase Dataset. Se proporciona el DataFrame dfmerge y se seleccionan las columnas 'id', 'id', y 'score_final', que corresponden al identificador del usuario, identificador de la película y puntaje final, respectivamente.

División de los datos: Los datos se dividen en un conjunto de entrenamiento y prueba utilizando el método train_test_split() de la biblioteca Surprise. Se especifica un tamaño de prueba del 25% (test_size=0.25).

Creación e implementación del modelo SVD: Se crea una instancia del modelo SVD utilizando la clase SVD() de Surprise. Luego, se entrena el modelo utilizando el método fit() y el conjunto de entrenamiento (trainset).

Guardado del modelo: El modelo entrenado se guarda en un archivo utilizando la biblioteca pickle en formato de archivo binario ('.pkl').
 [Click aquí para la descarga del Modelo--->][![Open In Kaggle](https://cdn.icon-icons.com/icons2/2699/PNG/96/kaggle_logo_icon_168474.png)](https://www.kaggle.com/datasets/davidhspinal/streamrec-movie?select=fc_model_svd_v1.pkl)

Carga del modelo: Se carga el modelo entrenado desde el archivo guardado utilizando pickle y se almacena en la variable svd_loaded.

Predicción de una calificación: Se utiliza el modelo cargado para predecir la calificación de una película específica para un usuario específico. Se proporciona el identificador del usuario (user_id) y el identificador de la película (movie_id) en el método predict() del modelo svd_loaded. El valor estimado de la calificación se almacena en la variable predicted_rating y se imprime en pantalla.

El algoritmo SVD (Descomposición de Valores Singulares) se utiliza en el filtrado colaborativo debido a su eficacia en la recomendación de elementos basada en la similitud entre usuarios o elementos. SVD se basa en la matriz de calificaciones de usuarios y elementos para descomponerla en matrices de valores singulares, lo que permite reducir la dimensionalidad y capturar relaciones latentes entre usuarios y elementos. Esto ayuda a predecir las calificaciones faltantes o recomendar elementos nuevos basados en las preferencias de usuarios similares.

En este caso, el uso de SVD es justificado porque es uno de los algoritmos más populares y efectivos en el filtrado colaborativo. Además, Surprise es una biblioteca especializada en recomendaciones y proporciona implementaciones eficientes de varios algoritmos de filtrado colaborativo, incluido SVD.

El modelo entrenado puede ser utilizado para predecir calificaciones de películas para usuarios específicos y ofrecer recomendaciones personalizadas en función de las preferencias de cada usuario.
 
 
 Prestar Atención!!! Si desea explorar el código a detalle tiene que descargar el archivo desarrollado Aquí--->> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lGVeqlIPEE9Ph8up_77qksx6d_FU0VcF?hl=es#scrollTo=_tif5ugNRhq6)
 </p>
 
 # <h2 align='left'> 9. Deploy </h2>
 <p align="justify">
Nuestro sistema de recomendación de películas basado en filtro colaborativo hemos  utilizando Gradio. Aquí un resumen del proceso de despliegue:

.Lectura de los datos: Se lee el conjunto de datos desde el archivo CSV ('merged_data6.csv') en un DataFrame de pandas llamado dfmerge.

.Carga del modelo: Se carga el modelo entrenado previamente desde el archivo guardado ('fc_model_svd_v1.pkl') utilizando la biblioteca pickle. El modelo cargado se almacena en la variable svd_model.

.Definición de la función de recomendación: Se define la función generar_recomendacion() que toma como argumentos el modelo SVD, el ID del usuario, el DataFrame de películas y los géneros de interés. Esta función filtra las películas que corresponden a los géneros de interés, realiza predicciones de rating para esas películas utilizando el modelo y devuelve una lista de títulos de películas recomendadas.

.Envoltura de la función de recomendación: Se define la función wrap_generar_recomendacion() que se utilizará como función de entrada para Gradio. Esta función toma los valores ingresados por el usuario, crea la lista de géneros de interés y llama a la función generar_recomendacion() con los argumentos correspondientes.

.Definición de la interfaz de Gradio: Se utiliza la clase Interface de Gradio para definir la interfaz de usuario. Se especifican los elementos de entrada (ID de usuario, casillas de verificación para los géneros de interés y la cantidad de recomendaciones) y el elemento de salida (texto que muestra los títulos de las películas recomendadas). También se proporciona un título y una descripción para la interfaz.

.Lanzamiento de la interfaz: Se utiliza el método launch() para iniciar la interfaz de Gradio y hacerla accesible para su uso.

Cuando se lanza la interfaz, los usuarios pueden ingresar su ID de usuario, seleccionar los géneros de interés y la cantidad de recomendaciones que desean obtener. Luego, la función wrap_generar_recomendacion() se llama con los valores ingresados y se muestra el resultado en la interfaz.
 </p>
# <h5 align='left'> 9.1 Google Colab: </h5>
Para hacer un puesta en producción rápido ofrecemos Google Colab!!! Si desea explorar el código a detalle tiene que descargar el archivo desarrollado Aquí
[Open in Colab](https://colab.research.google.com/drive/1ca5bSqtBeaBBVMwqrYN45X54_T5YsNUq?hl=es#scrollTo=JC1onUIrxD-E)
previamente hay que subir la red entrenada, que obtuvimos en el paso anterior.

Nota: este producto solo durará unas horas ya que esta limitado por el uso de Google colab.

# <h5 align='left'> 9.2 HugginFace:</h5>
Si se desea tener un modelo en la nube de manera permanente y gratuita le ofrecemos una versión en HuggingFace, el código se encuentra libre en la misma plataforma [Link Deploy](https://davidhosp-movie-recommendation-system.hf.space/)

 # <h2 align='left'> 10. Project Organization </h2>
 
    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description
    │   └── models              <- Notebooks of Machine learning or Deep Learning models.
    │   └── feature_engineering <- Notebooks of cleaning, transforming data, export final dataset.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so src can be imported.
    │
    └── src               <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

 # <h2 align='left'> 11. Conclusiones Finales </h2>

<p align="justify">
El proyecto logró desarrollar un sistema de recomendación de películas basado en filtrado colaborativo, utilizando el algoritmo SVD. El uso de SVD permitió realizar predicciones precisas y personalizadas para cada usuario. El sistema demostró ser útil y eficaz en la generación de recomendaciones de películas basadas en los géneros de interés del usuario.
 
 En general, el proyecto combinó técnicas de preprocesamiento de datos, construcción de modelos y despliegue de una interfaz interactiva para crear un sistema de recomendación de películas completo y funcional. El enfoque basado en filtrado colaborativo resultó efectivo y proporcionó recomendaciones relevantes a los usuarios. El proyecto puede servir como base para el desarrollo de sistemas de recomendación más avanzados y aplicaciones similares en el ámbito del entretenimiento y la personalización de contenido.
 
 </p>
 
  # Documentación-Paper
En este apartado econtraras el paper del proyecto resumido según el roadmap.

Click aquí para la descarga: [Link](https://docs.google.com/presentation/d/1Vo7-5wFiL5m_S0moL6NruJgOoBMNc0EQ/edit?usp=sharing&ouid=105962371803757766436&rtpof=true&sd=true)

# Diccionario de Datos

Aquí te brindamos nuestro diccionario de datos ya que  es esencial para garantizar la comprensión, consistencia, colaboración y evolución de los datos en nuestro  proyecto.Este Proporciona una base sólida para el diseño, desarrollo y mantenimiento efectivo de los datos, y será una herramienta fundamental para mejorar la calidad y la confiabilidad de la información utilizada en nuestra solución.

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/b39816c4-4745-4e25-8f57-e23b86c8f52d)


![graph (3)](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/2c30c85f-51b4-4061-b458-e4db5248fdc4)



 
# Citación
Por favor si usas la base de datos o el código, realizar la citación respectiva al autor. 
```
@article{StreamRec -Sistema de Recomendaciones Personalizadas De Películas y Series},
  Title = {StreamRec Movie Recommendation System},
  Authors = {Hospinal Roman, Oscar David },
  Year = {2023}
  University={HENRY}
}
```
# Contacto 
Para mas información por favor contactarse a:

u202021214@upc.edu.pe(David Hospinal).

