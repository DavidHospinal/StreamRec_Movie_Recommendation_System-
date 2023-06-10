
import pickle
import pandas as pd
import gradio as gr


def generar_recomendacion(svd_model, user_id, df, genres, top=5):
    # Filtrar las películas que correspondan a los géneros de interés
    df_filtered = df[df[genres].any(axis=1)]

    # Crear un mapeo de id de película a título de película para una búsqueda más eficiente
    id_to_title = df_filtered.set_index('id')['title'].to_dict()

    # Obtener las recomendaciones utilizando la función `apply` de pandas
    predicted_ratings = df_filtered['id'].apply(lambda movie_id: svd_model.predict(int(user_id), movie_id).est)

    # Ordenar las películas según su predicción de rating
    movie_rating = list(zip(df_filtered['id'], predicted_ratings))
    movie_rating.sort(key=lambda x: x[1], reverse=True)

    # Obtener los títulos de las películas recomendadas
    recommended_movies = movie_rating[:top]
    recommended_titles = [id_to_title[movie_id] for movie_id, _ in recommended_movies]

    # Devolver la lista de títulos como una cadena
    return ', '.join(recommended_titles)

# Leer los datos
dfmerge = pd.read_csv('merged_data6.csv')

# Cargar el modelo
with open('fc_model_svd_v1.pkl', 'rb') as file:
    svd_model = pickle.load(file)

def wrap_generar_recomendacion(user_id, drama, comedy, horror, romance, top=5):
    # Crear la lista de géneros de interés a partir de las casillas de verificación
    genres = []
    if drama: genres.append('Drama')
    if comedy: genres.append('Comedy')
    if horror: genres.append('Horror')
    if romance: genres.append('Romance')
    
    # Llamar a la función de recomendación y devolver los resultados como una cadena
    return generar_recomendacion(svd_model, user_id, dfmerge, genres, int(top))

# Definir la interfaz de Gradio
demo = gr.Interface(
    fn=wrap_generar_recomendacion,
    inputs=["text", gr.inputs.Checkbox(label="Drama"), gr.inputs.Checkbox(label="Comedy"), gr.inputs.Checkbox(label="Horror"), gr.inputs.Checkbox(label="Romance"), "text"], 
    outputs="text",
    title="Sistema de recomendación de películas basado en filtro colaborativo",
    description="Ingresa el ID del usuario (user_id), selecciona los géneros de interés y la cantidad de recomendaciones que te gustaría generar. Te mostraremos algunas películas que le pueden gustar.",
    allow_flagging='auto'
)

# Lanzar la interfaz
demo.launch()