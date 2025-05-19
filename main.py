from app.multipage import MultiPage
from app.pages.inicio import inicio
from app.pages.description import descripcion
from app.pages.generator import generador
from app.pages.acerca_de import acerca_de
import streamlit as st

def main():
    st.set_page_config(page_title="Generador de Video LTX", layout="wide")

    app = MultiPage()
    st.sidebar.title("Navegación")

    app.add_page("🏠 Inicio", inicio)
    app.add_page("📄 Descripción", descripcion)
    app.add_page("🎬 Generación de Video", generador)
    app.add_page("👨‍💻 Acerca de", acerca_de)

    app.run()

if __name__ == "__main__":
    main()
