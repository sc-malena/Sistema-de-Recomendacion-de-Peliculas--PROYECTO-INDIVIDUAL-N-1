import os
import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()


# Cargar el archivo CSV usando una ruta relativa
df = pd.read_csv("df_combinado.csv")


try:
    # Intentar cargar el archivo CSV
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    
    # Verificar que el DataFrame no esté vacío y que 'release_date' sea válida
    if df.empty:
        raise ValueError("El DataFrame está vacío. Revisa el archivo fuente.")
    if df['release_date'].isnull().all():
        raise ValueError("La columna 'release_date' contiene valores nulos o no válidos.")
    print("Archivo cargado y verificado correctamente.")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    df = pd.DataFrame()

# Ruta de prueba para verificar la carga de datos
@app.get("/prueba_carga")
def prueba_carga():
    if df.empty:
        return {"error": "El DataFrame no contiene datos. Revisa la carga del archivo."}
    return {"message": "El archivo se ha cargado correctamente y contiene datos."}

# Diccionarios de traducción para meses y días
meses = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
    'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
    'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}
dias_semana = {
    'lunes': 0, 'martes': 1, 'miércoles': 2, 'jueves': 3,
    'viernes': 4, 'sábado': 5, 'domingo': 6
}

# cantidad_filmaciones_mes: Cuenta las películas lanzadas en un mes específico
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    mes_num = meses.get(mes.lower())
    if mes_num is None:
        raise HTTPException(status_code=400, detail="Mes no válido")

    cantidad = df[df['release_date'].dt.month == mes_num].shape[0]
    return {"message": f"{cantidad} películas fueron estrenadas en el mes de {mes.capitalize()}"}

# cantidad_filmaciones_dia: Cuenta las películas lanzadas en un día específico de la semana
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    dia_num = dias_semana.get(dia.lower())
    if dia_num is None:
        raise HTTPException(status_code=400, detail="Día no válido")
    
    cantidad = df[df['release_date'].dt.dayofweek == dia_num].shape[0]
    return {"message": f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"}

# score_titulo: Devuelve título, año y score de una película
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    pelicula = df[df['title'].str.lower() == titulo.lower()]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    titulo = pelicula['title'].values[0]
    anio = pelicula['release_year'].values[0]
    score = pelicula['vote_average'].values[0]
    return {"message": f"La película {titulo} fue estrenada en el año {anio} con un score de {score}"}

# votos_titulo: Devuelve título, cantidad de votos y promedio de votación
@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    pelicula = df[df['title'].str.lower() == titulo.lower()]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    titulo = pelicula['title'].values[0]
    anio = pelicula['release_year'].values[0]
    votos = pelicula['vote_count'].values[0]
    promedio = pelicula['vote_average'].values[0]
    
    if votos < 2000:
        return {"message": f"La película {titulo} no cumple con la cantidad mínima de valoraciones (2000)"}
    
    return {"message": f"La película {titulo} fue estrenada en el año {anio}. Tiene un total de {votos} valoraciones, con un promedio de {promedio}"}

# get_actor: Calcula el éxito del actor en función del retorno
@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    participaciones = df[df['cast_procesado'].str.contains(nombre_actor, case=False, na=False)]
    if participaciones.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado")
    
    cantidad_peliculas = participaciones.shape[0]
    retorno_total = participaciones['revenue'].sum() / participaciones['budget'].sum() if participaciones['budget'].sum() > 0 else 0
    retorno_promedio = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0
    return {"message": f"El actor {nombre_actor} ha participado de {cantidad_peliculas} filmaciones, con un retorno total de {retorno_total} y un promedio de {retorno_promedio:.2f} por filmación"}

# get_director: Devuelve éxito del director con detalles de cada película
@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    # Filtramos las películas que contienen al director
    direcciones = df[df['crew_procesado'].str.contains(f"'nombre': '{nombre_director}'", case=False, na=False)]
    
    if direcciones.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    
    peliculas = []
    
    # Asegurarnos de que las columnas 'revenue' y 'budget' sean numéricas
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
    
    for _, row in direcciones.iterrows():
        # Verificar que 'budget' y 'revenue' no sean NaN
        print(f"Procesando película: {row['title']}")
        print(f"Revenue: {row['revenue']}, Budget: {row['budget']}")
        
        # Asegurarse de que el 'budget' es mayor que 0 para el cálculo
        if row['budget'] > 0:
            retorno_individual = row['revenue'] / row['budget']
        else:
            retorno_individual = 0
        
        print(f"Retorno individual: {retorno_individual}")
        
        # Crear el diccionario de la película
        pelicula_info = {
            "titulo": row['title'],
            "fecha_lanzamiento": row['release_date'],
            "retorno": retorno_individual,
            "costo": row['budget'],
            "ganancia": row['revenue'] - row['budget']
        }
        peliculas.append(pelicula_info)
    
    # Calcular retorno total
    retorno_total = direcciones['revenue'].sum() / direcciones['budget'].sum() if direcciones['budget'].sum() > 0 else 0
    return {
        "message": f"El director {nombre_director} tiene un retorno total de {retorno_total}",
        "peliculas": peliculas
    }


import random
import ast
from pydantic import BaseModel
from typing import List

# Limpiar los nombres de las columnas
df.columns = df.columns.str.strip()

# Verificar si 'genres_names' está presente
if 'genres_names' not in df.columns:
    raise HTTPException(status_code=500, detail="La columna 'genres_names' no está presente en el CSV")

# Definir el modelo de la película
class Movie(BaseModel):
    id: int
    title: str
    genre: List[str]  # Ahora acepta una lista de géneros

# Convertir la columna 'genres_names' de cadenas a listas
df['genres_names'] = df['genres_names'].apply(ast.literal_eval)

# Convertir el DataFrame a una lista de objetos Movie, manteniendo la lista de géneros
movies = [Movie(id=row['id'], title=row['title'], genre=row['genres_names']) for index, row in df.iterrows()]

@app.get("/recommendation", response_model=Movie)
def recommend_movie(genre: str = None):
    try:
        if genre:
            # Filtrar películas por género, buscando el género en la lista
            filtered_movies = [movie for movie in movies if genre.lower() in [g.lower() for g in movie.genre]]
            if filtered_movies:
                return random.choice(filtered_movies)
            else:
                raise HTTPException(status_code=404, detail=f"No se encontraron películas para el género '{genre}'")
        else:
            # Si no se pasa el género, devolver una película aleatoria
            return random.choice(movies)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



