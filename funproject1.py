#Fun Project #1 - Mini Quiz App dengan Streamlit
#Project Description
#Peserta akan membuat Mini Quiz App menggunakan Streamlit yang membantu pengguna mengetahui profesi yang cocok berdasarkan pilihan-pilihan mereka. Kuis ini akan menampilkan beberapa pertanyaan dan berdasarkan jawaban, pengguna akan diberi hasil yang mengarah pada salah satu profesi, misalnya: Programmer, Designer, atau Data Scientist.

#Key Features
#Multiple Choice Questions (Radio Buttons): Menampilkan serangkaian pertanyaan dengan pilihan jawaban menggunakan radio buttons.
#Skoring Berdasarkan Jawaban: Menghitung skor untuk masing-masing kategori (Programmer, Designer, Data Scientist) berdasarkan jawaban yang dipilih pengguna.
#UI yang Menarik: Menambahkan gambar dan pesan untuk hasil kuis yang menarik.
#Tombol untuk Melihat Hasil: Pengguna dapat menekan tombol untuk melihat hasil berdasarkan jawaban yang mereka pilih.
#Day 1 - Core Features
#Setup Streamlit dan membuat tampilan dasar aplikasi.
#Membuat Pertanyaan: Menambahkan beberapa pertanyaan dengan pilihan jawaban menggunakan radio buttons.
#Skoring dan Hasil: Menambahkan logika untuk menghitung skor berdasarkan pilihan jawaban dan menampilkan hasil yang sesuai.
#Day 2 - Finishing & Showcase
#Menyempurnakan Antarmuka: Menambah elemen visual seperti gambar atau icon untuk membuat aplikasi lebih menarik.
#Pengujian & Penyempurnaan: Pastikan aplikasi berjalan lancar dan hasil kuis sesuai dengan jawaban.

#Q1: Hal apa yang kamu sukai?
#a. Matematika
#b. Data
#c. Menggambar

#Q2: Apa yang kamu lakukan diwaktu luang?
#a. Ngoding
#b. Olah data
#C. Menggambar

#Q3: Kalau ada kesempatan kuliah lagi, kamu mau ambil konsentrasi apa?
#a. Computer Science
#b. Design Grafis
#c. Statistika

#Logika Skoring:

# mini_quiz_app.py

import streamlit as st

st.set_page_config(page_title="Mini Quiz App", page_icon="💻", layout="centered")

st.markdown(
    """
    <style>
    /* Ubah warna background utama */
    .stApp {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💻 Kamu cocoknya jadi apa nih?")
st.write("Coba kamu jawab dulu pertanyaan-pertanyaan ini buat tahu profesi apa yang cocok buat kamu!")

# Inisialisasi skor
scores = {"Programmer": 0, "Designer": 0, "Data Scientist": 0}

# Pertanyaan 1
q1 = st.radio(
    "1. Kamu suka belajar apa?",
    ["Matematika dan Algoritma Pemrograman", "Menggambar atau membuat desain", "Statistika dan Analisis Data"]
)
if q1 == "Matematikda dan Algoritma Pemrograman":
    scores["Programmer"] += 1
elif q1 == "Menggambar atau membuat desain":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

# Pertanyaan 2
q2 = st.radio(
    "2. Tool mana yang paling menarik menurutmu?",
    ["Visual Studio Code / PyCharm", "Figma / Photoshop", "Excel / R Studio"]
)
if q2 == "Visual Studio Code / PyCharm":
    scores["Programmer"] += 1
elif q2 == "Figma / Photoshop":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

# Pertanyaan 3
q3 = st.radio(
    "3. Kalau lagi stress, kamu lebih suka ngapain?",
    ["Mencari solusi lewat logika & algoritma", "Mencari ide kreatif & estetik", "Mencari pola lewat data"]
)
if q3 == "Mencari solusi lewat logika & algoritma":
    scores["Programmer"] += 1
elif q3 == "Mencari ide kreatif & estetik":
    scores["Designer"] += 1
else:
    scores["Data Scientist"] += 1

# Tombol untuk lihat hasil
if st.button("Lihat Hasil 💻🎨📊"):
    result = max(scores, key=scores.get)  # Ambil profesi dengan skor tertinggi
    st.subheader(f"Kamu cocok jadi: **{result}**")
    
    if result == "Programmer":
        st.success("💻 Kamu cocok jadi **Programmer**! Kamu suka logika, pemecahan masalah, dan dunia coding.")
    elif result == "Designer":
        st.success("🎨 Kamu cocok jadi **Designer**! Kreativitas dan estetika adalah kekuatanmu.")
    else:
        st.success("📊 Kamu cocok jadi **Data Scientist**! Kamu suka angka, analisis, dan membuat insight dari data.")
