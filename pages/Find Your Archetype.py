import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from ui import sidebar, form, button

sidebar()
form()
button()

st.markdown("<h2 style='text-align: center;'>Ayo Cari Tahu Archetype Kamu!</h2>", unsafe_allow_html=True)
st.write("")

@st.cache_resource
def load_models():
    ct_model = joblib.load('Model/transformer.pkl')
    kmeans_model = joblib.load('Model/kmeans.pkl')
    pca_model = joblib.load('Model/pca.pkl')
    return ct_model, kmeans_model, pca_model

# 2. Gunakan cache_data untuk dataframe referensi
@st.cache_data
def load_reference_data():
    return pd.read_csv('Data/Hasil_Clustering.csv')

# 3. Panggil fungsinya
ct, kmeans, pca = load_models()
df = load_reference_data()

if 'step' not in st.session_state:
    st.session_state.step = 1
if 'jawaban' not in st.session_state:
    st.session_state.jawaban = {}

def go_to_1(): st.session_state.step = 1

def go_to_2():
    st.session_state.jawaban.update({
        'M2': st.session_state.M2, 
        'M5': st.session_state.M5, 
        'M8': st.session_state.M8, 
        'M9': st.session_state.M9,
        'semester': st.session_state.semester, 
        'ipk': st.session_state.ipk,
        's2': st.session_state.s2, 
        'belajar': st.session_state.belajar
    })
    st.session_state.step = 2

def go_to_3():
    st.session_state.jawaban.update({
        'gaji': st.session_state.gaji, 
        'wirausaha': st.session_state.wirausaha,
        'bing': st.session_state.bing, 
        'motivasi': st.session_state.motivasi,
        'kogni': st.session_state.kogni, 
        'style': st.session_state.style,
        'kultur': st.session_state.kultur, 
        'ukuran': st.session_state.ukuran
    })
    st.session_state.step = 3

def reset():
    st.session_state.step = 1
    st.session_state.jawaban = {}

# Tampilkan Bar Progress
st.progress((st.session_state.step) / 3)

st.divider()

if st.session_state.step == 1:
    st.markdown("#### 📖 Bagian 1: Profil Akademis & Metrik Kompetensi")
    
    col1, col2 = st.columns(2)
    with col1:
        st.number_input('Skor M2 (Skills)', min_value=0, max_value=15, key='M2')
        st.number_input('Skor M8 (Ambisi)', min_value=0, max_value=10, key='M8')
    with col2:
        st.number_input('Skor M5 (Compass)', min_value=0, max_value=10, key='M5')
        st.number_input('Skor M9 (Resiliensi)', min_value=0, max_value=10, key='M9')

    c1, c2 = st.columns(2)
    with c1:
        st.radio('Semester Saat Ini', options=['Semester 1-2', 'Semester 3-4', 'Semester 5-6', 'Semester 7-8', 'Semester 9+/Lulus'], key='semester')
    with c2:
        st.radio('IPK Kamu', options=['Di Bawah 2,50', '2,50 - 2,99', '3,00 - 3,49', '3,50 - 4,00'], key='ipk')
    
    st.radio('Apakah Kamu Berencana Melanjutkan S2 atau Mengambil Sertifikasi Profesional?', options=['Tidak ada rencana', 'Mungkin suatu saat, tapi belum ada rencana konkret', 'ya, berencana ambil dalam waktu dekat', 'ya, sudah daftar/sedang berproses S2'], key='s2')
    st.radio('Seberapa Sering Kamu Belajar', options=['Jarang - Cukup yang diajarkan di kampus saja', 'Kadang - jika ada waktu luang', 'Cukup Rutin - minimal sekali seminggu', 'Sangat Rutin - tiap hari'], key='belajar')

    st.write("")
    st.button('Selanjutnya ➡️', on_click=go_to_2)

elif st.session_state.step == 2:
    st.markdown("#### 💼 Bagian 2: Aspirasi Karir & Gaya Kerja")
    st.radio('Ekspektasi Gaji', options=['Di bawah 4 Juta', 'Rp 4-6 Jt', 'Rp 6-10 Jt', 'Rp 10-15 Jt', 'Di atas 15 jt'], key='gaji')
    
    st.write("**Seberapa serius kamu mempertimbangkan untuk berwirausaha di masa depan?**")
    col_kiri, col_kanan = st.columns([1, 1])
    with col_kiri: st.caption("Tidak tertarik")
    with col_kanan: st.markdown("<div style='text-align: right; color: gray; font-size: 14px;'>Sangat serius</div>", unsafe_allow_html=True)
    st.radio('Minat Wirausaha', options=[1, 2, 3, 4, 5], horizontal=True, key='wirausaha', label_visibility="collapsed")
    
    st.radio('Level Bahasa Inggris Kamu', options=['Hanya bisa kalimat sederhana', 'Bisa mengikuti percakapan dan teks umum', 'Bisa presentasi dan menulis email profesional', 'Kerja dalam bahasa inggris tidak masalah'], key='bing')
    st.radio('Hal Yang Paling Memotivasi Kamu Ketika Bekerja', options=['Uang', 'Pengakuan, Prestige, dan Reputasi Profesional', 'Dampak dari Pekerjaan', 'Terus Belajar dan Berkembang Secara Intelektual', 'Kebebasan dalam Berkreasi'], key='motivasi')
    
    c1, c2 = st.columns(2)
    with c1:
        st.radio('Gaya kognitif Kamu Seperti Apa?', options=['analytical', 'creative', 'social', 'strategic'], key='kogni')
        st.radio('Gaya Kerja Kamu Seperti Apa?', options=['solo', 'small', 'big', 'flex'], key='style')
    with c2:
        st.radio('Kultur Kerjamu Seperti Apa?', options=['formal', 'agile', 'collab', 'result'], key='kultur')
        st.radio('Ukuran Perusahaan yang Ideal Buatmu', options=['Korporasi Besar (+1000 Karyawan)', 'Menengah (100 - 1000 Karyawan)', 'Startup (<100 Karyawan)', 'Yang penting culturenya cocok'], key='ukuran')

    st.divider()
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button('⬅️ Sebelumnya', on_click=go_to_1)
    with col2:
        st.button('Lihat Hasil 🚀', on_click=go_to_3, use_container_width=True)

elif st.session_state.step == 3:
    mapping_sem= {'Semester 1-2': 1, 'Semester 3-4': 2, 'Semester 5-6': 3, 'Semester 7-8': 4, 'Semester 9+/Lulus': 5}
    mapping_ipk= {'Di Bawah 2,50': 1, '2,50 - 2,99': 2, '3,00 - 3,49': 3, '3,50 - 4,00': 4}
    mapping_s2= {'Tidak ada rencana': 1, 'Mungkin suatu saat, tapi belum ada rencana konkret': 2, 'ya, berencana ambil dalam waktu dekat': 3, 'ya, sudah daftar/sedang berproses S2': 4}
    mapping_belajar= {'Jarang - Cukup yang diajarkan di kampus saja': 1, 'Kadang - jika ada waktu luang': 2, 'Cukup Rutin - minimal sekali seminggu': 3, 'Sangat Rutin - tiap hari': 4}
    mapping_gaji= {'Di bawah 4 Juta': 1, 'Rp 4-6 Jt': 2, 'Rp 6-10 Jt': 3, 'Rp 10-15 Jt': 4, 'Di atas 15 jt': 5}
    mapping_bing= {'Hanya bisa kalimat sederhana': 1, 'Bisa mengikuti percakapan dan teks umum': 2, 'Bisa presentasi dan menulis email profesional': 3, 'Kerja dalam bahasa inggris tidak masalah': 4}
    mapping_motivasi= {'Uang': 'money', 'Pengakuan, Prestige, dan Reputasi Profesional': 'prestige', 'Dampak dari Pekerjaan': 'impact', 'Terus Belajar dan Berkembang Secara Intelektual': 'growth', 'Kebebasan dalam Berkreasi': 'freedom'}
    mapping_ukuran= {'Korporasi Besar (+1000 Karyawan)': 'big', 'Menengah (100 - 1000 Karyawan)': 'mid', 'Startup (<100 Karyawan)': 'startup', 'Yang penting culturenya cocok': 'flex'}

    user_data = pd.DataFrame({
        "Skor M2 (Skills)": [st.session_state.jawaban['M2']],
        "Skor M5 (Compass)": [st.session_state.jawaban['M5']],
        "Skor M8 (Ambisi)": [st.session_state.jawaban['M8']],
        "Skor M9 (Resiliensi)": [st.session_state.jawaban['M9']],
        "Semester": [mapping_sem[st.session_state.jawaban['semester']]],
        "IPK": [mapping_ipk[st.session_state.jawaban['ipk']]],
        "Ekspektasi Gaji": [mapping_gaji[st.session_state.jawaban['gaji']]],
        "Minat Wirausaha": [st.session_state.jawaban['wirausaha']],
        "Rencana S2/Sertifikasi": [mapping_s2[st.session_state.jawaban['s2']]],
        "Frekuensi Belajar": [mapping_belajar[st.session_state.jawaban['belajar']]],
        "Level Bahasa Inggris": [mapping_bing[st.session_state.jawaban['bing']]],
        "Motivasi": [mapping_motivasi[st.session_state.jawaban['motivasi']]],
        "Cognitive Style": [st.session_state.jawaban['kogni']],
        "Work Style": [st.session_state.jawaban['style']],
        "Kultur Kerja": [st.session_state.jawaban['kultur']],
        "Ukuran Perusahaan": [mapping_ukuran[st.session_state.jawaban['ukuran']]]
    })

    user_tr = ct.transform(user_data)
    user_pca = pca.transform(user_tr)
    user_data['PCA1'], user_data['PCA2'] = user_pca[:, 0], user_pca[:, 1]
    
    hasil_cluster = kmeans.predict(user_tr)
    hasil_angka = int(hasil_cluster[0])

    df['Cluster'] = df['Cluster'].astype(str)

    # 1. Mapping warna VINIX7 yang absolut
    warna_cluster = {
        '1': '#0133A1', # Navy Blue
        '0': '#FFD13B', # Yellow
        '2': '#5BC0DE'  # Light Blue
    }

    # 2. Buat Plot dasar untuk semua mahasiswa (df)
    fig = px.scatter(
        df, 
        x='PCA1', 
        y='PCA2',
        color='Cluster',
        title='Posisi Kamu di Antara Mahasiswa Lainnya',
        labels={'Cluster': 'Kelompok Mahasiswa'},    
        color_discrete_map=warna_cluster,
        opacity=0.5 # Ini pengganti argumen alpha=0.5 di Seaborn
    )

    # 3. Tentukan warna bintang mengikuti hasil klasifikasi user
    # hasil_angka didapat dari int(hasil_cluster[0]) di kodinganmu sebelumnya
    warna_bintang = warna_cluster[str(hasil_angka)]

    # 4. Tambahkan layer bintang khusus untuk posisi user
    fig.add_trace(
        go.Scatter(
            x=user_data['PCA1'],
            y=user_data['PCA2'],
            mode='markers',
            marker=dict(
                symbol='star',
                size=22, # Ukuran bintang (sesuaikan jika kurang besar)
                color=warna_bintang,
                line=dict(width=2, color='#0133A1') # Garis pinggir bintang agar tidak nyaru
            ),
            name='Posisi Kamu'
        )
    )

    # Tampilkan plot interaktif di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    jenis_dict = {
        0: 'Kelompok Berkembang 🌱',
        1: 'Kelompok Ambisius & Proaktif 🔥',
        2: 'Kelompok Akademis & Stabil 🧠'
    }
    
    yappingan_res = {
        0: 'Mahasiswa pada kelompok ini menunjukkan tingkat kematangan dan ambisi yang masih dalam tahap awal...',
        1: 'Kelompok ini diisi oleh individu-individu yang sangat terdorong dan proaktif. Mendominasi skor tertinggi...',
        2: 'Kelompok ini menampilkan profil mahasiswa yang sangat solid secara akademis dengan rekor IPK tertinggi...'
    }

    # Desain Output Final bergaya "Card" 
    st.markdown(f"""
    <div style='background-color: #0133A1; padding: 25px; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='color: #FFD13B; margin-bottom: 5px;'>Archetype Kamu:</h3>
        <h1 style='color: white; margin-top: 0;'>{jenis_dict[hasil_angka]}</h1>
        <hr style='border-color: #FFD13B;'>
        <p style='font-size: 16px;'>{yappingan_res[hasil_angka]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.button("🔄 Coba Lagi", on_click=reset, use_container_width=True)