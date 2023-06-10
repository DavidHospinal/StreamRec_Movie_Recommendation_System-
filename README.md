 # <h1 align="center"> StreamRec Movie_Recommendation System</h1>
El proyecto "StreamRec" es un sistema de recomendación de películas y series diseñado para plataformas de streaming. El objetivo principal es proporcionar recomendaciones personalizadas a los usuarios, ayudándoles a descubrir contenido relevante y aumentar su satisfacción con el servicio.


# <h2 align='left'> 1. Descripción del Proyecto</h2>

<p align="justify">
El proyecto aborda el desafío de trabajar con datos poco maduros, donde se requiere un trabajo rápido de Data Engineering para transformar los datos anidados y establecer procesos automatizados de actualización para incorporar nuevas películas y series. Este enfoque permitirá ofrecer recomendaciones actualizadas y precisas a medida que se agregue contenido nuevo a la plataforma.
El sistema utilizará técnicas de Machine Learning, en particular el modelo de recomendación basado en el algoritmo SVD (Singular Value Decomposition), que permitirá analizar el historial de visualización de los usuarios y encontrar patrones para generar recomendaciones personalizadas. Además, se implementará una interfaz de usuario amigable donde los usuarios podrán explorar recomendaciones, calificar películas y series, y recibir nuevas sugerencias en función de sus preferencias.
El proyecto busca proporcionar un MVP (Minimum Viable Product) en un plazo de tiempo acelerado, permitiendo a la start-up lanzar su sistema de recomendación y ofrecer una experiencia mejorada a sus usuarios. Con el tiempo, se espera ampliar y mejorar el sistema, incorporando nuevos algoritmos de recomendación y funciones adicionales para enriquecer la experiencia del usuario.
</p>

# <h2 align='left'> 2. Problemática</h2>

<p align="justify">
La problemática en el proyecto es la falta de madurez y estructura en los datos de plataformas de streaming, lo que dificulta la creación de un sistema de recomendación efectivo. Los datos están desorganizados, no hay procesos automatizados para la actualización de nuevos contenidos y se requiere un trabajo rápido de Data Engineering para transformar los datos y crear un MVP funcional. Esta falta de estructura y procesos eficientes dificulta el desarrollo y despliegue de un sistema de recomendación eficaz, lo que representa un desafío para el equipo de Data Science.
</p>
# <h2 align='left'> 3. Pipeline Del Proyecto "StreamRec"</h2>

![image](https://github.com/DavidHospinal/StreamRec_Movie_Recommendation_System-/assets/73408508/54424acd-0da0-4a2e-8adc-e7ac93e1d8e6)

<p align="justify">
 
a.Extracción y preprocesamiento de datos (ETL)
.Extracción de datos de fuentes de streaming.
.Limpieza y transformación de datos.
 
b.Análisis exploratorio de datos (EDA)
.Exploración de la estructura y distribución de los datos.
.Identificación de patrones y tendencias.

 c.Desarrollo de la API
.Diseño de los endpoints de la API.
.Implementación de la lógica de recomendación.
.Exposición de la API para acceso externo.
 
d.Entrenamiento del modelo
.Selección del algoritmo de recomendación
.Ajuste de parámetros del modelo
.Validación cruzada y evaluación de rendimiento
 
e.Evaluación y ajuste del modelo
.Cálculo de métricas de evaluación (RMSE, MAE)
.Ajuste de hiperparámetros para mejorar la precisión
 
f.Implementación y despliegue
.Configuración de servidores y recursos
.Integración con otros componentes del sistema
</p>
