# 🎸 Análisis de Audio y Letras: The Smiths

Este proyecto es una aplicación web interactiva desarrollada en Python con **Streamlit**. Analiza las características de audio y las letras de los álbumes de estudio de la banda británica *The Smiths*.

## 🚀 Características del Proyecto
Este trabajo cubre las siguientes funcionalidades:
1. **Filtrado de Datos (Spotify Dataset):** A partir de un dataset de más de 1.2M de canciones, se ha filtrado la discografía del artista para aislar únicamente las canciones pertenecientes a sus 4 álbumes de estudio originales.
2. **Extracción de Letras (API REST):** Conexión en tiempo real a la API pública de **LRCLIB** para buscar y extraer la letra exacta de la canción seleccionada.
3. **Análisis Textual y Visual:** Generación dinámica de una Nube de Palabras (WordCloud) basada en la frecuencia de los términos utilizados en la letra de la canción (excluyendo "stopwords" comunes).

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python
* **Web Framework:** Streamlit
* **Análisis de Datos:** Pandas
* **Visualización:** Matplotlib, WordCloud
* **Peticiones HTTP:** Requests

## 🔗 Enlace a la Web App
Puedes probar la aplicación en el siguiente enlace:
[Ver Aplicación en Streamlit](https://smiths-analysis-app-oevyd4rsouhh92vlt27r47.streamlit.app/)