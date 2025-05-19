import os
import replicate
import streamlit as st

def generador():
    st.title("🎬 Generación de Video")

    st.subheader("Configuración del video")
    
    prompt = st.text_area(
        "Prompt",
        value="A happy golden retriever swimming in a clear blue swimming pool on a sunny day...",
        height=100
    )

    negative_prompt = st.text_area(
        "Negative Prompt",
        value="low quality, worst quality, deformed, distorted, watermark",
        height=60
    )

    aspect_ratio = st.selectbox("Aspect Ratio", ["16:9", "9:16", "1:1", "4:5"])

    fps = 24
    valid_lengths = [97, 129, 161, 193, 225, 257]
    desired_duration = st.slider("Duración deseada (en segundos)", min_value=3, max_value=10, value=6)

    desired_frames = desired_duration * fps
    closest_length = min(valid_lengths, key=lambda x: abs(x - desired_frames))

    st.markdown(f"🎞️ Duración final usada: **~{closest_length / fps:.2f} segundos** ({closest_length} frames a {fps} fps)")

    if st.button("Generar Video"):
        if not os.getenv("REPLICATE_API_TOKEN"):
            st.error("API token no configurado. Configura REPLICATE_API_TOKEN en tu archivo `.env`")
            return

        with st.spinner("Generando video..."):
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

            except Exception as e:
                st.error(f"Error al generar el video: {str(e)}")
