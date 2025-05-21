import streamlit as st
from app.pages.inicio import inicio
from app.pages.description import descripcion
from app.pages.generator import generador
from app.pages.acerca_de import acerca_de

def main():
    st.set_page_config(page_title="Generador de Video LTX", layout="wide")
    
    st.sidebar.title("Navegación")
    opcion = st.sidebar.radio(
        "Ir a",
        (
            "🏠 Inicio",
            "📄 Descripción",
            "🎬 Generación de Video",
            "👨‍💻 Acerca de"
        )
    )

    if opcion == "🏠 Inicio":
        inicio()
    elif opcion == "📄 Descripción":
        descripcion()
    elif opcion == "🏗️ Arquitectura":
        arquitectura()
    elif opcion == "🎬 Generación de Video":
        generador()
    elif opcion == "👨‍💻 Acerca de":
        acerca_de()

if __name__ == "__main__":
    main()
