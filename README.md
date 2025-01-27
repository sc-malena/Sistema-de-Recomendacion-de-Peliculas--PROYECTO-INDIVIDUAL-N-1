# Sistema de Recomendación de Películas

Este proyecto implementa un **sistema de recomendación de películas** basado en **similitud de contenido** utilizando **FastAPI** y **Cosine Similarity**. La aplicación proporciona recomendaciones personalizadas de películas en función de las preferencias del usuario, utilizando datos agregados de diversas plataformas de streaming.

## Tecnologías utilizadas

- **Python**: Lenguaje principal para el desarrollo de la lógica del sistema y el procesamiento de datos.
- **Pandas**: Librería para la manipulación, limpieza y transformación de datos.
- **FastAPI**: Framework para crear una API REST eficiente y rápida.
- **Render**: Plataforma de despliegue para alojar la aplicación web.
- **Cosine Similarity**: Métrica para calcular la similitud entre películas y generar recomendaciones precisas.

## Estructura de Datos

Los datos procesados se almacenan en el archivo `df_combinado.csv`, que contiene información consolidada de películas y créditos de producción. Este archivo ha sido optimizado en tamaño para mejorar el rendimiento del sistema.

### DataFrames utilizados

- **df_movies**: Contiene información principal de las películas (títulos, géneros, etc.).
- **df_credits**: Incluye los créditos de producción (actores, directores, etc.).
- **df_movies_limpio**: DataFrame limpio y optimizado para las recomendaciones, con menor tamaño y mayor rendimiento.

## Instalación

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/sc-malena/Sistema-de-Recomendacion-de-Peliculas--PROYECTO-INDIVIDUAL-N-1.git
   cd Sistema-de-Recomendacion-de-Peliculas--PROYECTO-INDIVIDUAL-N-1

2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt

3. **Ejecuta la aplicación**:

   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000

## Estructura de Datos

- Malena Sosa
- https://www.linkedin.com/in/malena-sosa-0224ab13a/



