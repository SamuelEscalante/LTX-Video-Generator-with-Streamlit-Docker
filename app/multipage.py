import streamlit as st

class MultiPage:
    """Framework para combinar múltiples aplicaciones de Streamlit."""

    def __init__(self) -> None:
        self.pages = []

    def add_page(self, title, func) -> None:
        """Agregar una nueva página."""
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        """Mostrar el menú y ejecutar la página seleccionada."""
        page = st.sidebar.selectbox(
            'Navegación de la App',
            self.pages,
            format_func=lambda page: page['title']
        )
        page['function']()
