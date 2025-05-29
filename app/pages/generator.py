import os
import replicate  # type: ignore
import streamlit as st  # type: ignore
import time

def generador():
    st.markdown("""
        <style>
        .fadein {
            opacity: 0;
            animation: fadeInAnim 1s ease-in forwards;
        }
        @keyframes fadeInAnim {
            to { opacity: 1; }
        }
        .spacer { height: 24px; }

        /* Personalización widgets Streamlit */
        textarea, .stTextArea textarea {
            background: #181c2b !important;
            color: #fff !important;
            border-radius: 12px !important;
            border: 2px solid #00c6ff !important;
            font-size: 1.1em !important;
            transition: box-shadow 0.3s;
        }
        textarea:focus, .stTextArea textarea:focus {
            box-shadow: 0 0 0 2px #00c6ff;
        }
        .stSelectbox div[data-baseweb="select"] > div {
            background: #181c2b !important;
            color: #fff !important;
            border-radius: 12px !important;
            border: 2px solid #00c6ff !important;
        }
        .stSlider > div {
            padding-top: 12px;
        }
        .stSlider .css-1c5h5b6 {
            background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%) !important;
            border-radius: 8px;
        }
        .stSlider .css-14xtw13 {
            background: #fff !important;
            border: 2px solid #00c6ff !important;
        }
        div.stButton > button {
            background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
            color: #fff;
            border-radius: 30px;
            font-weight: bold;
            font-size: 1.1em;
            border: none;
            padding: 0.7em 2em;
            margin-top: 16px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 16px #00c6ff44;
        }
        </style>
        <script>
        window.addEventListener('DOMContentLoaded', (event) => {
            document.querySelectorAll('.fadein').forEach(el => {
                el.style.opacity = 1;
            });
        });
        </script>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="fadein" style="animation-delay:0.1s">🎬 Generación de Video</h1>', unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown('<div class="fadein" style="animation-delay:0.2s"><h3>Configuración del video</h3></div>', unsafe_allow_html=True)

    st.markdown('<div class="fadein" style="animation-delay:0.25s">', unsafe_allow_html=True)
    prompt = st.text_area(
        "Prompt",
        value="A happy golden retriever swimming in a clear blue swimming pool on a sunny day...",
        height=100
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="fadein" style="animation-delay:0.3s">', unsafe_allow_html=True)
    negative_prompt = st.text_area(
        "Negative Prompt",
        value="low quality, worst quality, deformed, distorted, watermark",
        height=60
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="fadein" style="animation-delay:0.35s">', unsafe_allow_html=True)
    aspect_ratio = st.selectbox("Aspect Ratio", ["16:9", "9:16", "1:1", "4:5"])
    st.markdown('</div>', unsafe_allow_html=True)

    fps = 24
    valid_lengths = [97, 129, 161, 193, 225, 257]
    desired_duration = st.slider("Duración deseada (en segundos)", min_value=3, max_value=10, value=6)

    desired_frames = desired_duration * fps
    closest_length = min(valid_lengths, key=lambda x: abs(x - desired_frames))

    st.markdown(f'<div class="fadein" style="animation-delay:0.4s">🎞️ Duración final usada: <b>~{closest_length / fps:.2f} segundos</b> ({closest_length} frames a {fps} fps)</div>', unsafe_allow_html=True)

    st.markdown('<div class="fadein" style="animation-delay:0.45s">', unsafe_allow_html=True)
    if st.button("Generar Video"):
        if not os.getenv("REPLICATE_API_TOKEN"):
            st.error("API token no configurado. Configura REPLICATE_API_TOKEN en tu archivo `.env`")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        with st.spinner("Generando video..."):
            start_time = time.time()
            try:
                input_data = {
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "aspect_ratio": aspect_ratio,
                    "length": closest_length,
                    "fps": fps,
                    "duration": "long",
                    "cfg": 3,
                    "steps": 30,
                    "target_size": 640
                }

                output = replicate.run(
                    "lightricks/ltx-video:8c47da666861d081eeb4d1261853087de23923a268a69b63febdf5dc1dee08e4",
                    input=input_data
                )

                for index, item in enumerate(output):
                    video_path = f"output_{index}.mp4"
                    with open(video_path, "wb") as f:
                        f.write(item.read())
                    st.success("¡Video generado con éxito!")
                    st.video(video_path)
                    elapsed = time.time() - start_time
                    st.info(f"⏱️ Tiempo de generación: {elapsed:.2f} segundos")

            except Exception as e:
                st.error(f"Error al generar el video: {str(e)}")
    st.markdown('</div>', unsafe_allow_html=True)