import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Modul Sebutan Digital", layout="wide")

# --- DATA PERKATAAN (7 BAHAGIAN) ---
data_bahagian = {
    "Bahagian 1 (Ny)": ["Nyanyi", "Nyonya", "Minyak", "Nyala", "Nyamuk", "Nyewa", "Nyusur", "Nyawa"],
    "Bahagian 2 (Ng)": ["Nganga", "Ngiru", "Bunga", "Singa", "Kucing", "Langit", "Bangku", "Ngaji"],
    "Bahagian 3 (Kh)": ["Khamis", "Khabar", "Akhir", "Khutbah", "Khidmat", "Khayal", "Khu", "Khi"],
    "Bahagian 4 (Sy)": ["Syukur", "Syarat", "Syiling", "Syahdu", "Syurga", "Syor", "Syam", "Syif"],
    "Bahagian 5 (ai)": ["Kedai", "Sungai", "Tupai", "Serai", "Ramai", "Lalai", "Pandai", "Rantai"],
    "Bahagian 6 (oi)": ["Amboi", "Kaloi", "Poi", "Konvoi", "Dodoi", "Sepoi", "Boikot"],
    "Bahagian 7 (au)": ["Halau", "Marau", "Kacau", "Pulau", "Pisau", "Hijau", "Danau", "Wau"]
}

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("📁 Menu Bahagian")
pilihan_bhg = st.sidebar.radio("Pilih Bahagian:", list(data_bahagian.keys()))

# --- MAIN INTERFACE ---
st.title(f"🎤 Latihan Sebutan: {pilihan_bhg}")
st.write("Dengar sebutan guru dan murid boleh merakam suara sendiri.")

senarai_perkataan = data_bahagian[pilihan_bhg]

# Pilih perkataan
index = st.selectbox(
    "Pilih Perkataan:", 
    range(len(senarai_perkataan)), 
    format_func=lambda x: f"Perkataan {x+1}: {senarai_perkataan[x]}"
)

perkataan_aktif = senarai_perkataan[index]

st.divider()
st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{perkataan_aktif}</h1>", unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("👤 **BAHAGIAN GURU**")
    rakaman_g = mic_recorder(key=f"g_{pilihan_bhg}_{index}", start_prompt="Rakam Contoh Guru", stop_prompt="Tamat")
    if rakaman_g:
        st.audio(rakaman_g['bytes'])

with col2:
    st.success("👶 **BAHAGIAN MURID**")
    rakaman_m = mic_recorder(key=f"m_{pilihan_bhg}_{index}", start_prompt="Mula Rakam Murid", stop_prompt="Tamat")
    if rakaman_m:
        st.audio(rakaman_m['bytes'])
        # Butang muat turun supaya murid boleh simpan hasil mereka sendiri
        st.download_button(
            label="Muat Turun Rakaman Saya",
            data=rakaman_m['bytes'],
            file_name=f"Murid_{perkataan_aktif}.wav",
            mime="audio/wav"
        )

st.sidebar.divider()
st.sidebar.info("Nota: Sebagai website, rakaman tidak disimpan secara kekal di server. Murid digalakkan muat turun hasil rakaman jika perlu.")