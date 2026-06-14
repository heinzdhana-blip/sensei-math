import streamlit as st
from openai import OpenAI

# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="SENSEI MATH",
    page_icon="📚",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f8fbff;
}

.titulo{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#3a6ea5;
}

.subtitulo{
    text-align:center;
    color:#666;
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    '<p class="titulo">📚 SENSEI MATH</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitulo">Tutor Inteligente de Matemáticas con IA</p>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=120
    )

    st.title("Perfil")

    nombre = st.text_input(
        "Nombre",
        "Estudiante"
    )

    nivel = st.selectbox(
        "Nivel",
        [
            "Básico",
            "Intermedio",
            "Avanzado"
        ]
    )

# ---------------- DASHBOARD ----------------

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Racha", "5 días")

with c2:
    st.metric("Problemas resueltos", "42")

with c3:
    st.metric("Nivel", nivel)

st.divider()

# ---------------- CHAT ----------------

st.header("🤖 Tutor Matemático")

api_key = st.text_input(
    "DeepSeek API Key",
    type="password"
)

pregunta = st.text_area(
    "Pregunta de Matemáticas"
)

if st.button("Preguntar"):

    if api_key and pregunta:

        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role":"system",
                    "content":
                    """
                    Eres SENSEI MATH.

                    Tutor experto en matemáticas.

                    Explica paso a paso.

                    Usa ejemplos.

                    Enseña de forma amigable.
                    """
                },
                {
                    "role":"user",
                    "content":pregunta
                }
            ]
        )

        st.success(
            respuesta.choices[0].message.content
        )
