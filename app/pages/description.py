import streamlit as st # type: ignore

def descripcion():
    st.markdown("""
        <style>
        .fadein {
            opacity: 0;
            animation: fadeInAnim 1.2s ease-in forwards;
        }
        @keyframes fadeInAnim {
            to { opacity: 1; }
        }
        .spacer {
            height: 24px;
        }
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
    st.markdown('<h1 class="fadein">📽️ Descripción de la Aplicación</h1>', unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.2s">
    Esta aplicación genera videos a partir de descripciones de texto utilizando el modelo <b>LTX Video</b> de Replicate.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.25s">
    <h3>¿Qué puedes hacer?</h3>
    <ul>
      <li>Escribir un <i>prompt</i> para describir lo que quieres ver en el video.</li>
      <li>Configurar aspectos como la relación de aspecto y duración.</li>
      <li>Generar automáticamente un video basado en tu descripción.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.3s">
    <h3>Requisitos</h3>
    <ul>
      <li>Tener configurado el API Token de Replicate en tu archivo <code>.env</code>.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.35s">
    <h3>Ejemplo de Prompt</h3>
    <code>"A man in a dimly lit room talks on a vintage telephone..."</code>
    <hr>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fadein" style="animation-delay:0.4s">
            <img src="https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00006.gif" 
                 alt="Ejemplo visual" style="width:500px;height:auto;display:block;margin:auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-top: 8px;">
            <span style="font-size: 0.9em; color: gray;">
                © Ejemplo visual extraído del <a href="https://github.com/Lightricks/LTX-Video" target="_blank">repositorio oficial de LTX Video en GitHub</a>
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
