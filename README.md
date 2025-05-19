# 🎬 LTX Video Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Replicate](https://img.shields.io/badge/Replicate-FF6C37?logo=replicate&logoColor=white)](https://replicate.com/)

Aplicación web para generar videos de alta calidad usando el modelo **LTX Video** de Lightricks a través de la API de Replicate, con interfaz intuitiva en Streamlit y empaquetado en Docker.

Proyecto basado en el paper [LTX-Video: Realtime Video Latent Diffusion](https://arxiv.org/abs/2501.00103)

## ✨ Características

- Generación de videos de 3-10 segundos con prompts de texto
- Control avanzado mediante negative prompts
- Ajuste de relación de aspecto (16:9, 9:16, etc.)
- Interfaz amigable con previsualización de resultados
- Despliegue local o en la nube con Docker

## 🚀 Cómo Usar

### Requisitos
- Python 3.9+
- Cuenta en [Replicate](https://replicate.com) (API token)
- Docker




## Instalación Local

### Obtención del API Token de Replicate

### Paso 1: Crear cuenta
1. Visita [replicate.com](https://replicate.com)
2. Haz clic en "Sign Up" (registro con GitHub)

### Paso 2: Acceder a API Tokens
1. Haz clic en tu avatar (esquina superior derecha)
2. Selecciona **"API Tokens"** en el menú


### Paso 3: Copiar token
1. Busca tu token en la lista
2. Haz clic en el icono de copiar 📋  
   **⚠️ Importante:** Nunca lo expongas en código público

### Paso 4: Configurar proyecto

1. Crea archivo `.env` en la raíz del proyecto:
```bash
    REPLICATE_API_TOKEN="tu_token_aqui"
```

```bash
git clone https://github.com/tu-usuario/ltx-video-generator.git
cd ltx-video-generator
