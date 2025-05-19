import streamlit as st

def acerca_de():
    st.title("👨‍💻 Acerca del Proyecto")

    st.markdown("""
    Ésta **interfaz** fue desarrollada por estudiantes de Ingeniería de Datos e Inteligencia Artificial:

    - **Juan Camilo Burbano**  
    - **Samuel Escalante**  
    - **Emmanuel Quintero**

    Universidad Autónoma de Occidente  
    Cali, Colombia – 2025
    """)

    st.markdown("""
    **Nota:**  
    La herramienta **LTX Video** no fue creada por nosotros. Todos los créditos y derechos pertenecen a sus autores originales.  
    Repositorio oficial de LTX Video en GitHub: [LTX Video in GitHub](https://github.com/Lightricks/LTX-Video)
    """)

    st.markdown("""
    **Importante:**  
    Para ejecutar el modelo **LTX Video**, se utilizó la plataforma [Replicate](https://replicate.com/) como API, debido a la alta complejidad computacional que requiere este modelo.
    """)