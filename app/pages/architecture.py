import streamlit as st

def arquitectura():
    st.title("🧠 Arquitectura del Modelo LTX Video")

    st.markdown("""
    El modelo **LTX Video**, desarrollado por [Lightricks](https://github.com/Lightricks/LTX-Video), es un sistema de generación de video condicional a texto que se basa en una arquitectura de tipo **Latent Diffusion Model (LDM)** optimizada para generar múltiples fotogramas de forma coherente.

    ### 🧩 Componentes clave:

    - **Codificador de texto (CLIP o T5)**: procesa el *prompt* del usuario y lo transforma en una representación latente que se usa como condición para generar el video.
    - **Autoencoder**: convierte los fotogramas del video en una representación latente compacta, acelerando el proceso de difusión.
    - **U-Net con atención**: red neuronal central que predice cómo debe evolucionar el ruido latente hacia un video realista.
    - **Scheduler de difusión**: controla el proceso de denoising para generar múltiples frames coherentes en el tiempo.

    ### 🛠️ Flujo de trabajo general

    1. El texto se convierte en embeddings (vector de características).
    2. Se inicia un tensor latente con ruido.
    3. El modelo difunde ese ruido en pasos sucesivos condicionados por el texto.
    4. Al final, se decodifica ese tensor a video.

    ### 🖼️ Diagrama de Arquitectura

    ![Arquitectura LTX](https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/architecture_diagram.png)

    > 📘 Imagen tomada del [repositorio oficial de LTX Video](https://github.com/Lightricks/LTX-Video)

    ### 🧪 Enlace al paper (si disponible)

    Actualmente no hay un paper formal publicado. Puedes revisar los detalles técnicos directamente en su [GitHub oficial](https://github.com/Lightricks/LTX-Video).

    ---
    """)
