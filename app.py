import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Configuración de la página
st.set_page_config(page_title="The Smiths - Análisis", layout="wide")
st.title("🎸 Análisis de Audio y Letras: The Smiths")
st.markdown("Esta web app explora las características de los álbumes de estudio de The Smiths y analiza sus letras en tiempo real.")

# 1. Cargar los datos pre-filtrados
@st.cache_data
def load_data():
    # Leemos el archivo pequeñito que exportamos de Colab
    return pd.read_csv('the_smiths_studio.csv')

df = load_data()

st.subheader("1. Álbumes de Estudio")
st.write(f"Se han cargado {len(df)} canciones únicas de estudio.")
st.dataframe(df[['name', 'album', 'release_date', 'danceability', 'energy']])

# 2. Explorador de Letras y Nube de Palabras
st.subheader("2. Explorador de Letras (API LRCLIB)")

# Selector de canciones
cancion_seleccionada = st.selectbox("Selecciona una canción para analizar:", df['name'].tolist())

if cancion_seleccionada:
    # Limpiamos el nombre
    clean_song_name = cancion_seleccionada.split('-')[0].strip()
    
    # Hacemos la petición a la API
    url = "https://lrclib.net/api/search"
    params = {"q": f"The Smiths {clean_song_name}"}
    headers = {"User-Agent": "StreamlitApp_Proyecto/1.0"}
    
    letra = ""
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                for result in data:
                    if 'plainLyrics' in result and result['plainLyrics']:
                        letra = result['plainLyrics']
                        break
    except:
        pass

    # Mostrar resultados en dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Letra de: {clean_song_name}**")
        if letra:
            st.text_area("Letra original", letra, height=350)
        else:
            st.warning("Letra no encontrada en la API.")
            
    with col2:
        st.markdown("**Nube de palabras de la canción**")
        texto_para_nube = letra if letra else clean_song_name # Fallback
        
        stopwords_en = set(STOPWORDS)
        stopwords_en.update(["Chorus", "Verse", "oh", "la", "ah"])
        
        fig, ax = plt.subplots(figsize=(6, 4))
        wordcloud = WordCloud(width=600, height=400, background_color='white', 
                              stopwords=stopwords_en, colormap='plasma').generate(texto_para_nube)
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)