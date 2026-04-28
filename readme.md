# 🍅 AI Deteksi Daun Tomat

Aplikasi berbasis web (_Machine Learning_) untuk mendeteksi klasifikasi penyakit pada daun tomat. Repo ini adalah **catatan dan referensi pribadi** untuk menguasai alur _end-to-end_ (mulai dari _training_ sampai _deployment_) sebelum mengeksekusi project skripsi yang sesungguhnya.

## 🛠️ Teknologi yang Digunakan

- **Bahasa:** Python 3.12+
- **Frontend/UI:** Streamlit
- **Machine Learning Engine:** TensorFlow & Keras
- **Pre-trained Model:** MobileNetV2
- **Image Processing:** NumPy & Pillow (PIL)

## 📂 Struktur Direktori Proyek

Struktur standar yang harus dipertahankan untuk _project_ ML:

```text
TomatoLeafDiseases/
│
├── env/                         # 🚫 Folder Virtual Environment
├── model/                       # Folder khusus penyimpanan model
│   └── model_tomat_finetuned.h5 # Otak AI
├── app.py                       # Main script / Kode UI Streamlit
├── requirements.txt             # Daftar library 
├── .gitignore                   # Penjaga gerbang file raksasa 
└── README.md                    # Readme
```
