# Sistema de Recomendación de Películas

Este proyecto implementa un **sistema de recomendación de películas** utilizando técnicas de **similitud de contenido**, con el objetivo de proporcionar recomendaciones personalizadas basadas en las preferencias del usuario. La aplicación emplea **FastAPI** para construir una API REST rápida y eficiente, y utiliza **Cosine Similarity** para calcular la similitud entre películas. Los datos utilizados provienen de diversas plataformas de streaming, lo que permite hacer recomendaciones precisas y relevantes.

Los usuarios pueden interactuar con la API para recibir sugerencias de películas similares a las que ya han visto o que podrían interesarles según sus gustos. La recomendación se basa en los atributos de las películas, como los géneros, actores y directores, para ofrecer una experiencia personalizada.

El sistema está diseñado para ser escalable y fácil de integrar con otras plataformas de streaming en el futuro. Además, el uso de **FastAPI** permite que la API maneje múltiples solicitudes de manera eficiente, ofreciendo tiempos de respuesta rápidos y bajos costos de ejecución.


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



