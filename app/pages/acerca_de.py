import streamlit as st # type: ignore

def acerca_de():
    st.markdown("""
    <style>
    .fadein {
        opacity: 0;
        animation: fadeInAnim 1.2s ease-in forwards;
    }
    @keyframes fadeInAnim {
        to { opacity: 1; }
    }
    .spacer { height: 24px; }
    </style>
    <script>
    window.addEventListener('DOMContentLoaded', (event) => {
        document.querySelectorAll('.fadein').forEach(el => {
            el.style.opacity = 1;
        });
    });
    </script>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="fadein" style="animation-delay:0.1s">👨‍💻 Acerca del Proyecto</h1>', unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.2s">
    Ésta <b>interfaz</b> fue desarrollada por estudiantes de Ingeniería de Datos e Inteligencia Artificial:
    <ul>
        <li><b>Juan Camilo Burbano</b></li>
        <li><b>Samuel Escalante</b></li>
        <li><b>Emmanuel Quintero</b></li>
    </ul>
    Universidad Autónoma de Occidente<br>
    Cali, Colombia – 2025
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.3s">
    <b>Nota:</b><br>
    La herramienta <b>LTX Video</b> no fue creada por nosotros. Todos los créditos y derechos pertenecen a sus autores originales.<br>
    Repositorio oficial de LTX Video en GitHub: <a href="https://github.com/Lightricks/LTX-Video">LTX Video in GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.4s">
    <b>Importante:</b><br>
    Para ejecutar el modelo <b>LTX Video</b>, se utilizó la plataforma <a href="https://replicate.com/">Replicate</a> como API, debido a la alta complejidad computacional que requiere este modelo.
    </div>
    """, unsafe_allow_html=True)