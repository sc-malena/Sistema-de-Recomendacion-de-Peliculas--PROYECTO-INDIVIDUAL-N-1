# Sistema de Recomendación de Películas

Este proyecto implementa un sistema de recomendación de películas basado en la similitud de contenido utilizando FastAPI y Cosine Similarity. La aplicación permite obtener recomendaciones de películas en función de las preferencias del usuario y de los datos agregados de diversas plataformas de streaming.

## Tecnologías utilizadas

- **Python**: Para el desarrollo de la lógica del sistema y el procesamiento de datos.
- **Pandas**: Para la manipulación y transformación de datos.
- **FastAPI**: Para crear una API REST eficiente y rápida.
- **Render**: Para el despliegue de la aplicación en la web.
- **Cosine Similarity**: Para calcular la similitud entre películas y recomendar títulos similares.

## Estructura de Datos

Los datos procesados están almacenados en un archivo CSV llamado `df_combinado.csv`, el cual contiene información unificada de películas y créditos de producción, optimizado en tamaño para mejorar el rendimiento del sistema.

### DataFrames utilizados

1. **df_movies**: Contiene la información principal de las películas.
2. **df_credits**: Incluye información sobre los créditos de producción.
3. **df_movies_limpio**: DataFrame limpio y reducido en tamaño, usado para las recomendaciones.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/sc-malena/Sistema-de-Recomendacion-de-Peliculas--PROYECTO-INDIVIDUAL-N-1.git
   cd Sistema-de-Recomendacion-de-Peliculas--PROYECTO-INDIVIDUAL-N-1
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
1. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000

## Autores
Malena Sosa





