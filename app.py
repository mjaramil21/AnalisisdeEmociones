import streamlit as st
from textblob import TextBlob
from googletrans import Translator

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    html, body, [class*="css"] {
        background-color: #0f1117;
        color: #c7f0db;
        font-family: 'Share Tech Mono', monospace;
    }

    h1, h2, h3 {
        color: #7fffd4;
        text-shadow: 1px 1px 2px #000000;
    }

    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #1a1c22;
        color: #00ffcc;
        border: 1px solid #00ffcc;
    }

    .stButton > button {
        background-color: #262a35;
        color: #7fffd4;
        border: none;
        border-radius: 4px;
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #00ffcc;
        color: #000;
    }

    .sidebar .sidebar-content {
        background-color: rgba(15, 17, 23, 0.9);
        border-right: 2px solid #00ffcc;
    }

    .recuadro {
        background-color: rgba(0, 255, 204, 0.05);
        border-left: 3px solid #00ffcc;
        padding: 0.5em;
        margin-bottom: 0.5em;
        font-size: 0.95em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

translator = Translator()

st.title("Laboratorio de Emociones")
st.subheader("Adquiere información y datos emocionales sobre lo que escribas")

# Sidebar sin imágenes
with st.sidebar:
    st.subheader("Indicadores emocionales")
    st.markdown("""
    <div style='color:#005f73'>
    <b>Polaridad:</b> Representa si el texto tiene un tono negativo (-1), neutro (0) o positivo (1).
    <br><br>
    <b>Subjetividad:</b> Señala si el contenido es objetivo (0) o subjetivo (1), útil para saber si se basa en hechos o emociones.
    </div>
    """, unsafe_allow_html=True)

# Área de análisis
with st.expander('Interpretar emociones a partir del texto'):
    text1 = st.text_area('Escribe algo (preferiblemente si puedes hacerlo en inglés) para analizar su tono emocional:')
    if text1:
        translation = translator.translate(text1, src="auto", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('**Polaridad:**', polarity)
        st.write('**Subjetividad:**', subjectivity)

        if polarity >= 0.5:
            st.success("Mensaje con carga positiva.")
        elif polarity <= -0.5:
            st.error("Mensaje con carga negativa.")
        else:
            st.info("Mensaje con tono neutral.")
