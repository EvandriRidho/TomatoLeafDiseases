import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Konfigurasi UI & Judul
st.set_page_config(page_title="Deteksi Penyakit Daun Tomat", page_icon="🍅")

st.title("🍅 AI Deteksi Penyakit Daun Tomat")
st.write("Silahkan upload foto daun tomat, AI akan menganilisis penyakitnya")

# Panggil Model
@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('model/model_daun_tomat_pintar.h5')

model = load_my_model()

# Daftar Penyakit berdasarkan index
class_names = [
    'Bacterial Spot (Bercak Bakteri)', 
    'Early Blight (Bercak Daun Awal)', 
    'Late Blight (Bercak Daun Akhir)', 
    'Leaf Mold (Jamur Daun)', 
    'Septoria Leaf Spot (Bercak Septoria)', 
    'Spider Mites (Tungau Laba-laba)', 
    'Target Spot (Bercak Target)', 
    'Yellow Leaf Curl Virus (Virus Daun Kuning Keriting)', 
    'Mosaic Virus (Virus Mosaik)', 
    'Healthy (Daun Sehat)'
]

# Fitur Upload & Nampilin Gambar
uploaded_file = st.file_uploader("Pilih foto daun tomat...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    #Buka file pake PIL
    image = Image.open(uploaded_file)
    # Tampilkan ke web
    st.image(image, caption="Foto Daun yang diupload", use_container_width=True)
    st.write("Sedang menganalisis Gambar....")

    # samain ukuran foto
    img_resized = image.resize((224,224))
    # ubah gambar jadi matriks
    img_array = tf.keras.preprocessing.image.img_to_array(img_resized)
    # bagi 255 biar nilai 0 - 1
    img_array = img_array / 255.0
    # bungkus dalam 1 array
    img_array = np.expand_dims(img_array, axis=0)

    # AI Predection
    predictions = model.predict(img_array)
    # Cari nilai persentase tinggi
    index_tertinggi = np.argmax(predictions[0])
    nama_penyakit = class_names[index_tertinggi]
    akurasi = predictions[0][index_tertinggi] * 100

    # Tampilkan ke web
    st.success(f"Hasil Prediksi: {nama_penyakit} ")
    st.info(f"Tingkat Keyakinan AI: {akurasi:.2f}%")