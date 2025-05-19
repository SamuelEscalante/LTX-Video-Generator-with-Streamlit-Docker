import streamlit as st

def inicio():
    st.title("🎥 Bienvenido a LTX - Video")
    st.markdown("""
    Esta aplicación permite generar videos realistas a partir de texto usando **LTX Video**.
    
    Usa la barra lateral para navegar entre secciones.
    """)
    
    st.image(
        "https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00013.gif",
        caption="Ejemplo visual",
        use_column_width=True
    )

    st.caption(" © Ejemplo visual extraído del [repositorio oficial de LTX Video en GitHub](https://github.com/Lightricks/LTX-Video)")
