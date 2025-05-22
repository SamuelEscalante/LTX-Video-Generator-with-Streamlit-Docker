import streamlit as st
from PIL import Image

def arquitectura():
    st.title("🏗️ Arquitectura del Modelo LTX Video")

    st.markdown("""
    El modelo **LTX Video**, desarrollado por [Lightricks](https://github.com/Lightricks/LTX-Video), es un sistema de generación de video condicional a texto que se basa en una arquitectura de tipo **Latent Diffusion Model (LDM)** optimizada para generar múltiples fotogramas de forma coherente.

    ### Componentes clave:

    - **Codificador de texto (CLIP o T5)**: procesa el *prompt* del usuario y lo transforma en una representación latente que se usa como condición para generar el video.
    - **Autoencoder**: convierte los fotogramas del video en una representación latente compacta, acelerando el proceso de difusión.
    - **U-Net con atención**: red neuronal central que predice cómo debe evolucionar el ruido latente hacia un video realista.
    - **Scheduler de difusión**: controla el proceso de denoising para generar múltiples frames coherentes en el tiempo.

    ### Flujo de trabajo general

    1. El texto se convierte en embeddings (vector de características).
    2. Se inicia un tensor latente con ruido.
    3. El modelo difunde ese ruido en pasos sucesivos condicionados por el texto.
    4. Al final, se decodifica ese tensor a video.

    ### Diagrama de Arquitectura
    """)

    image = Image.open("docs/_static/arquitectura.png")
    st.image(image, caption="""La arquitectura Video-VAE de LTX-Video:
                                (a) Codificador Causal que utiliza convoluciones causales 3D, aplicando una compresión de 32 x 32 x 8 (excepto el primer fotograma, que se codifica como un fotograma latente separado).
                                (b) Decodificador de Denoising con condicionamiento por pasos de difusión e inyección de ruido en múltiples capas.""", use_column_width=True)

    st.markdown("""
    ### 🧪 Enlace al paper

    Para más detalles sobre la arquitectura y el funcionamiento del modelo, puedes consultar el [paper original](https://arxiv.org/pdf/2501.00103) de Lightricks.

    ---
    """)

