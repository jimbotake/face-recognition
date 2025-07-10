import streamlit as st
import face_recognition
from PIL import Image, ImageDraw
import numpy as np

st.set_page_config(page_title="Face Recognition App", layout="centered")

st.title("🔍 Face Recognition Web App")

# Upload known face
st.sidebar.header("📌 Upload Wajah Dikenal (Referensi)")
known_file = st.sidebar.file_uploader("Upload gambar wajah yang dikenal", type=["jpg", "jpeg", "png"])

# Upload target image
st.sidebar.header("📸 Upload Gambar Target")
target_file = st.sidebar.file_uploader("Upload gambar yang ingin diperiksa", type=["jpg", "jpeg", "png"])

if known_file:
    st.subheader("🖼️ Gambar Wajah Referensi")
    known_image = Image.open(known_file)
    st.image(known_image, caption="Wajah Dikenal", use_column_width=True)

if known_file and target_file:
    st.subheader("🧠 Proses Pengenalan Wajah...")

    # Load and encode known face
    known_img = face_recognition.load_image_file(known_file)
    known_encodings = face_recognition.face_encodings(known_img)

    if len(known_encodings) == 0:
        st.error("❌ Tidak ada wajah terdeteksi di gambar referensi!")
    else:
        known_encoding = known_encodings[0]

        # Load target image
        target_img = face_recognition.load_image_file(target_file)
        target_locations = face_recognition.face_locations(target_img)
        target_encodings = face_recognition.face_encodings(target_img, target_locations)

        # Convert to PIL Image for drawing
        pil_img = Image.fromarray(target_img)
        draw = ImageDraw.Draw(pil_img)

        found_match = False
        for (top, right, bottom, left), face_encoding in zip(target_locations, target_encodings):
            match = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.5)[0]
            color = (0, 255, 0) if match else (255, 0, 0)

            label = "Match" if match else "Unknown"
            if match:
                found_match = True

            draw.rectangle(((left, top), (right, bottom)), outline=color, width=3)
            draw.text((left, bottom + 10), label, fill=color)

        st.image(pil_img, caption="Hasil Deteksi", use_column_width=True)
        if found_match:
            st.success("✅ Wajah dikenali!")
        else:
            st.warning("⚠️ Tidak ada kecocokan ditemukan.")
