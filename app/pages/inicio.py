import streamlit as st  # type: ignore

def inicio():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');

    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        min-height: 70vh;
        margin-top: 130px;
        position: relative;
        z-index: 1;
    }

    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2em;
        color: #fff;
        letter-spacing: 2px;
        font-weight: bold;
        opacity: 0;
        animation: fadeIn 2.5s ease-in forwards;
        animation-delay: 0.6s;
    }

    .subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5em;
        text-align: center;
        color: #fff;
        margin-bottom: 0.5em;
        opacity: 0;
        animation: fadeIn 2.5s ease-in forwards;
        animation-delay: 0.3s;
    }

    .color-bar {
        margin-top: 30px;
        width: 300px;
        height: 6px;
        border-radius: 10px;
        background: linear-gradient(270deg, #00ff00, #00ffff, #ff00ff, #ffff00, #00ff00);
        background-size: 600% 600%;
        opacity: 0;
        animation: fadeIn 2.5s ease-in forwards 0.9s, rgbBar 5s ease infinite;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes rgbBar {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .custom-button {
        display: block;
        margin: 40px auto 0;
        padding: 0.8em 2em;
        font-size: 1.2em;
        font-family: 'Poppins', sans-serif;
        color: #fff;
        background: #007bff;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s, background 0.3s;
    }

    .custom-button:hover {
        transform: scale(1.05);
        background: #0056b3;
    }

    .fadein-img {
        opacity: 0;
        animation: fadeIn 2.5s ease-in forwards;
        animation-delay: 0.5s;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # Contenido central
    st.markdown("""
    <div class="center-container">
        <div class="subtitle">Welcome to</div>
        <div class="main-title"><b>LTX VIDEO</b></div>
        <div class="color-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    # CSS personalizado para el expander y el texto interno
    # Ajusta el margen superior del expander para que se vea más arriba
    st.markdown("""
    <style>
    /* Expander container */
    .streamlit-expanderHeader {
        font-family: 'Poppins', sans-serif;
        font-size: 2.2em !important;
        font-weight: bold !important;
        color: #fff !important;
        background: linear-gradient(90deg, #007bff 0%, #00c6ff 100%);
        border-radius: 12px 12px 0 0;
        padding: 20px 32px !important;
        margin-top: -300px !important;  /* Más negativo para subir el expander */
    }
    /* Expander body */
    .streamlit-expanderContent {
        background: rgba(30, 30, 60, 0.95);
        border-radius: 0 0 12px 12px;
        padding: 28px 24px 24px 24px !important;
        margin-top: -2px;
    }
    /* Texto dentro del expander */
    .expander-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8em;
        font-weight: bold;
        color: #fff;
        margin-bottom: 20px;
        text-align: center;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

    espacio = st.container()
    espacio.markdown("<br>", unsafe_allow_html=True)

    # Expander con efecto fade-in para ejemplos
    with st.expander("📽️ Ver Ejemplos Generados con LTX Video"):
        st.markdown("""
            <div class="expander-title">
                Ejemplos generados con LTX Video
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                '<img src="https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00001.gif" class="fadein-img" style="width:100%;" alt="Ejemplo 1"/>',
                unsafe_allow_html=True)
            st.caption("Ejemplo 1")

        with col2:
            st.markdown(
                '<img src="https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00010.gif" class="fadein-img" style="width:100%;" alt="Ejemplo 2"/>',
                unsafe_allow_html=True)
            st.caption("Ejemplo 2")

        with col3:
            st.markdown(
                '<img src="https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00015.gif" class="fadein-img" style="width:100%;" alt="Ejemplo 3"/>',
                unsafe_allow_html=True)
            st.caption("Ejemplo 3")
