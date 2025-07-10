

\# Aplikasi Web Pengenalan Wajah



Aplikasi web sederhana untuk pengenalan wajah menggunakan \*\*Streamlit\*\* dan library \*\*face\_recognition\*\* dalam Python.



\## Fitur

\- Unggah gambar referensi (wajah dikenal) dan gambar target.

\- Deteksi dan tandai wajah secara otomatis pada gambar target.

\- Bandingkan wajah untuk menemukan kecocokan dengan gambar referensi.

\- Tampilan visual dengan kotak pembatas dan label ("Match" atau "Unknown").

\- Antarmuka yang mudah digunakan dengan Streamlit.



\## Tampilan Aplikasi

!\[Tampilan Aplikasi saat mendeteksi betul](images/true_capture.jpg)
!\[Tampilan Aplikasi saat mendeteksi salah](images/false_capture.jpg)



\## Teknologi

\- Python 3.x

\- Streamlit (untuk UI)

\- face\_recognition (berbasis dlib)

\- Pillow (untuk gambar dan anotasi)

\- NumPy



\## Cara Menjalankan Secara Lokal

1\. Clone repositori ini:

&nbsp;  git clone https://github.com/username/face-recognition-app.git

&nbsp;  cd face-recognition-app

&nbsp; 

2\. Install dependensi:

&nbsp;  pip install -r requirements.txt

&nbsp;  

3\. Jalankan aplikasi Streamlit:

&nbsp;  streamlit run app.py

&nbsp;  



\## Cara Penggunaan

\- Unggah gambar wajah yang dikenal di sidebar.

\- Unggah gambar target di sidebar.

\- Aplikasi akan menampilkan wajah yang terdeteksi dan menandai wajah yang cocok.



\## Catatan

\- Pastikan gambar wajah yang diunggah jelas dan menghadap depan untuk hasil terbaik.

\- Level toleransi pencocokan wajah disetel default pada 0.5.



