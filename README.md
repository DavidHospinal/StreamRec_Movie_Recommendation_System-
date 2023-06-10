 # <h1 align="center"> StreamRec Movie_Recommendation System</h1>
El proyecto "StreamRec" es un sistema de recomendación de películas y series diseñado para plataformas de streaming. El objetivo principal es proporcionar recomendaciones personalizadas a los usuarios, ayudándoles a descubrir contenido relevante y aumentar su satisfacción con el servicio.


# <h2 align='left'> 1. Descripción del Proyecto</h2>

<p align="justify">
El proyecto aborda el desafío de trabajar con datos poco maduros, donde se requiere un trabajo rápido de Data Engineering para transformar los datos anidados y establecer procesos automatizados de actualización para incorporar nuevas películas y series. Este enfoque permitirá ofrecer recomendaciones actualizadas y precisas a medida que se agregue contenido nuevo a la plataforma.
El sistema utilizará técnicas de Machine Learning, en particular el modelo de recomendación basado en el algoritmo SVD (Singular Value Decomposition), que permitirá analizar el historial de visualización de los usuarios y encontrar patrones para generar recomendaciones personalizadas. Además, se implementará una interfaz de usuario amigable donde los usuarios podrán explorar recomendaciones, calificar películas y series, y recibir nuevas sugerencias en función de sus preferencias.
El proyecto busca proporcionar un MVP (Minimum Viable Product) en un plazo de tiempo acelerado, permitiendo a la start-up lanzar su sistema de recomendación y ofrecer una experiencia mejorada a sus usuarios. Con el tiempo, se espera ampliar y mejorar el sistema, incorporando nuevos algoritmos de recomendación y funciones adicionales para enriquecer la experiencia del usuario.
</p>

# <h2 align='left'> 2. Background</h2>

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/00cc87f9-c045-4aa8-b4e1-21dd91c16468)


<p align="justify">
El proyecto surge en el contexto de una start-up que ofrece servicios de agregación de plataformas de streaming. La empresa se enfrenta al desafío de proporcionar recomendaciones personalizadas a sus usuarios, con el objetivo de mejorar la experiencia de usuario y aumentar la retención.
Anteriormente, la empresa no contaba con un sistema de recomendación implementado y los datos disponibles para este fin eran escasos y poco estructurados. La falta de procesos automatizados para la actualización de nuevas películas o series y la falta de transformación de los datos dificultaban la tarea de crear un modelo de recomendación efectivo.
Ante esta situación, el equipo de Data Science se propone desarrollar un sistema de recomendación desde cero, realizando tareas de Data Engineering para transformar y organizar los datos, así como desarrollar una API para interactuar con el modelo de recomendación. El objetivo es crear un MVP (Minimum Viable Product) en un plazo de tiempo reducido para poner en marcha el sistema de recomendación y comenzar a obtener retroalimentación de los usuarios.
El proyecto busca superar los desafíos de madurez de los datos, implementar procesos automatizados para la actualización de información y aprovechar técnicas de aprendizaje automático para generar recomendaciones personalizadas y precisas. Con esto, la empresa espera mejorar la satisfacción de los usuarios y fortalecer su posición en el mercado de servicios de streaming.
</p>
# <h2 align='left'> 3. Problemática</h2>

<p align="justify">
La problemática en el proyecto es la falta de madurez y estructura en los datos de plataformas de streaming, lo que dificulta la creación de un sistema de recomendación efectivo. Los datos están desorganizados, no hay procesos automatizados para la actualización de nuevos contenidos y se requiere un trabajo rápido de Data Engineering para transformar los datos y crear un MVP funcional. Esta falta de estructura y procesos eficientes dificulta el desarrollo y despliegue de un sistema de recomendación eficaz, lo que representa un desafío para el equipo de Data Science.
</p>
# <h2 align='left'> 4. Pipeline Del Proyecto "StreamRec"</h2>

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/54424acd-0da0-4a2e-8adc-e7ac93e1d8e6)

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

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/eda54f38-5699-4675-88bb-3646a53120a2)

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

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/f623f0af-ce5c-4777-ad95-612fffcaca3f)


<p align="justify">
Los procedimientos de limpieza que se realizaron a los dos archivos CSV (movies_dataset.csv y credits.csv) antes de unirlos incluyeron varias etapas:

.Extracción de datos relevantes: Se seleccionaron las columnas necesarias de cada archivo que eran relevantes para el análisis conjunto. En el archivo movies_dataset.csv, se extrajeron las columnas: 'id', 'original_title', 'genres', 'popularity', 'vote_average', y 'vote_count'. En el archivo credits.csv, se extrajeron las columnas: 'id', 'cast', y 'crew'.

.Tratamiento de valores faltantes: Se verificó si había valores faltantes en las columnas seleccionadas y se decidió cómo manejarlos. Por ejemplo, si había valores faltantes en la columna 'cast' o 'crew' del archivo credits.csv, se podrían reemplazar por valores nulos o eliminar las filas correspondientes.

.Conversión de datos: Se verificó el tipo de datos de cada columna y se realizó cualquier conversión necesaria para asegurar la coherencia de los datos. Por ejemplo, las columnas 'popularity', 'vote_average' y 'vote_count' se convirtieron en números decimales o enteros según corresponda.

.Limpieza de texto: Se aplicaron técnicas de limpieza de texto para eliminar caracteres no deseados, espacios en blanco adicionales o formato incorrecto en las columnas de texto, como 'original_title', 'genres' y 'cast'. Esto podría incluir eliminar puntuación, convertir a minúsculas, eliminar espacios adicionales, etc.

.Unión de datos: Una vez que los dos archivos CSV se limpiaron y se seleccionaron las columnas relevantes, se realizó la unión de los datos utilizando la columna 'id' como clave de unión. Esto permitió combinar la información de actores y equipos de producción del archivo credits.csv con los detalles de la película del archivo movies_dataset.csv. y esto dio lugar al dataset final para nuestro modelo merged_data6.csv.
 
 .Versionamiento de los datasets: En este link encontrarás los versionamientos trabajados de los datasets a lo largo del proyecto [![Open In Kaggle](https://www.kaggle.com/static/images/site-logo.svg)](https://www.kaggle.com/datasets/davidhspinal/streamrec-movie?select=movies_dataset.csv)
</p>

 

