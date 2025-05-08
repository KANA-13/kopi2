import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Judul dan deskripsi
st.title('☕ Simulasi Pemanggangan Biji Kopi Berbasis Web')
st.write("""
Selamat datang!  
Di sini Anda bisa mensimulasikan proses pemanggangan biji kopi, melihat perubahan suhu dan warna secara interaktif!
""")

# Input dari user
durasi = st.slider('Durasi Pemanggangan (menit)', 1, 10, 5)
start = st.button('Mulai Pemanggangan')

# Fungsi untuk simulasi warna biji kopi
def warna_biji(suhu):
    if suhu < 150:
        return 'Coklat Muda'
    elif suhu < 200:
        return 'Coklat Medium'
    else:
        return 'Coklat Tua'

# Simulasi ketika tombol ditekan
if start:
    st.subheader('📈 Perkembangan Suhu dan Warna Biji Kopi')
    suhu_list = []
    waktu_list = []
    
    progress_bar = st.progress(0)
    
    for menit in range(durasi):
        suhu = 100 + 15 * menit  # suhu bertambah 15 derajat tiap menit
        warna = warna_biji(suhu)
        
        st.write(f"Menit ke-{menit+1}: Suhu **{suhu}°C**, Warna Biji: **{warna}**")
        
        suhu_list.append(suhu)
        waktu_list.append(menit+1)
        
        progress_bar.progress((menit+1) / durasi)
        time.sleep(1)  # waktu jeda untuk efek real-time
        
    st.success('Pemanggangan Selesai! ☕')

    # Membuat grafik suhu
    fig, ax = plt.subplots()
    ax.plot(waktu_list, suhu_list, marker='o', color='chocolate')
    ax.set_title('Perubahan Suhu Selama Pemanggangan')
    ax.set_xlabel('Waktu (menit)')
    ax.set_ylabel('Suhu (°C)')
    ax.grid(True)
    st.pyplot(fig)
    
    st.balloons()
