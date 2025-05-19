# 🎬 LTX Video Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Replicate](https://img.shields.io/badge/Replicate-FF6C37?logo=replicate&logoColor=white)](https://replicate.com/)

Aplicación web para generar videos de alta calidad usando el modelo **LTX Video** de Lightricks a través de la API de Replicate, con interfaz intuitiva en Streamlit y empaquetado en Docker.

## ✨ Características

- Generación de videos de 3-8 segundos con prompts de texto
- Control avanzado mediante negative prompts
- Ajuste de relación de aspecto (16:9, 9:16, etc.)
- Interfaz amigable con previsualización de resultados
- Despliegue local o en la nube con Docker

## 🚀 Cómo Usar

### Requisitos
- Python 3.9+
- Cuenta en [Replicate](https://replicate.com) (API token)
- Docker (opcional)

### Instalación Local
```bash
git clone https://github.com/tu-usuario/ltx-video-generator.git
cd ltx-video-generator
pip install -r requirements.txt