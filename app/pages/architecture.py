import streamlit as st  # type: ignore
import base64

def arquitectura():
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    # Carga la imagen y conviértela a base64 para incrustarla en HTML
    with open("docs/_static/arquitectura.png", "rb") as img_file:
        img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="fadein" style="animation-delay:0.1s">🏗️ Arquitectura del Modelo LTX Video</h1>', unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.2s">
    El modelo <b>LTX Video</b>, desarrollado por <a href="https://github.com/Lightricks/LTX-Video">Lightricks</a>, es un sistema de generación de video condicional a texto que se basa en una arquitectura de tipo <b>Latent Diffusion Model (LDM)</b> optimizada para generar múltiples fotogramas de forma coherente.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.25s">
    <h3>Componentes clave:</h3>
    <ul>
        <li><b>Codificador de texto (CLIP o T5)</b>: procesa el <i>prompt</i> del usuario y lo transforma en una representación latente que se usa como condición para generar el video.</li>
        <li><b>Autoencoder</b>: convierte los fotogramas del video en una representación latente compacta, acelerando el proceso de difusión.</li>
        <li><b>U-Net con atención</b>: red neuronal central que predice cómo debe evolucionar el ruido latente hacia un video realista.</li>
        <li><b>Scheduler de difusión</b>: controla el proceso de denoising para generar múltiples frames coherentes en el tiempo.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.3s">
    <h3>Flujo de trabajo general</h3>
    <ol>
        <li>El texto se convierte en embeddings (vector de características).</li>
        <li>Se inicia un tensor latente con ruido.</li>
        <li>El modelo difunde ese ruido en pasos sucesivos condicionados por el texto.</li>
        <li>Al final, se decodifica ese tensor a video.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="fadein" style="animation-delay:0.35s">
    <h3>Diagrama de Arquitectura</h3>
    <img src="data:image/png;base64,{img_base64}" style="width:100%;max-width:700px;display:block;margin:auto;" />
    <div style="font-size:0.9em;color:gray;margin-top:8px;">
        La arquitectura Video-VAE de LTX-Video:<br>
        (a) Codificador Causal que utiliza convoluciones causales 3D, aplicando una compresión de 32 x 32 x 8 (excepto el primer fotograma, que se codifica como un fotograma latente separado).<br>
        (b) Decodificador de Denoising con condicionamiento por pasos de difusión e inyección de ruido en múltiples capas.
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fadein" style="animation-delay:0.4s">
    <h3>🧪 Enlace al paper</h3>
    <p>
    Para más detalles sobre la arquitectura y el funcionamiento del modelo, puedes consultar el <a href="https://arxiv.org/pdf/2501.00103">paper original</a> de Lightricks.
    </p>
    <hr>
    </div>
    """, unsafe_allow_html=True)