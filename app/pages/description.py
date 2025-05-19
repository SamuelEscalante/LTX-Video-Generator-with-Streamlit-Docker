import streamlit as st

def descripcion():
    st.title("📽️ Descripción de la Aplicación")
    
    st.markdown("""
    Esta aplicación genera videos a partir de descripciones de texto utilizando el modelo **LTX Video** de Replicate.

    ### ¿Qué puedes hacer?
    - Escribir un *prompt* para describir lo que quieres ver en el video.
    - Configurar aspectos como la relación de aspecto y duración.
    - Generar automáticamente un video basado en tu descripción.

    ### Requisitos
    - Tener configurado el API Token de Replicate en tu archivo `.env`.
    
    ### Ejemplo de Prompt
    `"A man in a dimly lit room talks on a vintage telephone..."`

    --- 
    """)
    st.image("https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00006.gif", caption="Ejemplo visual", use_column_width=True)
    st.caption(" © Ejemplo visual extraído del [repositorio oficial de LTX Video en GitHub](https://github.com/Lightricks/LTX-Video)")
