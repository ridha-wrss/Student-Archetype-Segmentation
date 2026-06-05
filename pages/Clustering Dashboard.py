import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from ui import sidebar, tab

sidebar()
tab()

st.markdown('<h1 style="text-allign:center;">Segmentasi <i>Student Archetype</i></h1>', unsafe_allow_html= True)
st.write("")

@st.cache_data
def load_data():
    df_clustering = pd.read_csv('Data/Hasil_Clustering.csv')
    df_summary = pd.read_csv('Data/Summary_Clustering.csv')
    return df_clustering, df_summary

clustering, summary = load_data()
clustering['Cluster'] = clustering['Cluster'].astype(str)

colors = ['#0133A1', '#FFD13B', '#5BC0DE']
sns.set_palette(sns.color_palette(colors))

fig = px.scatter(
    x=clustering['PCA1'], y=clustering['PCA2'],
    color=clustering['Cluster'],
    title='Hasil Clustering K-Means (K= 3)',
    labels={'x': 'Principal Component 1',
            'y': 'Principal Component 2',
            'color': 'Kelompok Mahasiswa'},    
    color_discrete_sequence= colors
)

fig.update_layout(width=800, height=500)
st.plotly_chart(fig, use_container_width=True)

tab1, tab2, tab3 = st.tabs(["📊 Statistik Cluster", "📈 Distribusi Fitur", "📋 Hasil Cluster"])

with tab1:
    centeroid_T = summary.T

    centeroid_T.columns = ['Cluster 0: Kelompok Berkembang', 'Cluster 1: Kelompok Ambisius & Proaktif', 'Cluster 2: Kelompok Akademis & Stabil']
    st.dataframe(centeroid_T)

    st.markdown("### Profil Masing-Masing Kelompok")
    st.markdown(f"<div style='background-color: #f4f6f9; padding: 15px; border-left: 5px solid #FFD13B; border-radius: 5px;'>🌱 <b>Cluster 0: Kelompok Berkembang (31.75%)\n\n</b>Menunjukkan tingkat kematangan dan ambisi yang masih dalam tahap awal. Rata-rata semester 2.8 dan IPK 3.48. Mencatatkan skor terendah pada metrik Skills (6.91), Compass (7.95), Ambisi (4.88), dan Resiliensi (5.43). Termotivasi oleh finansial dengan gaya kognitif analitis, namun memiliki kecenderungan kuat pada kultur perusahaan formal dan tim berskala kecil.</div>",
                 unsafe_allow_html=True)
    
    st.markdown(f"<div style='background-color: #f4f6f9; padding: 15px; border-left: 5px solid #0133A1; border-radius: 5px;'>🔥 <b>Cluster 1: Kelompok Ambisius & Proaktif (22.13%)\n\n</b>Kelompok terkecil namun diisi oleh individu yang sangat terdorong. Mendominasi skor tertinggi di seluruh metrik (Skills 10.41, Compass 9.04, Ambisi 7.75, Resiliensi 7.99). Sangat tertarik wirausaha, berani menargetkan gaji tinggi, dan proaktif studi lanjut. Menyukai fleksibilitas kerja (flex) serta kultur kolaboratif (collab).</div>",
                 unsafe_allow_html=True)
    
    st.markdown(f"<div style='background-color: #f4f6f9; padding: 15px; border-left: 5px solid #5BC0DE; border-radius: 5px;'>🧠 <b>Cluster 2: Kelompok Akademis & Stabil (46.12%)\n\n</b>Kelompok mayoritas yang sangat solid secara akademis dengan rekor IPK tertinggi (3.64). Skor Skills, Compass, Ambisi, dan Resiliensi berada di level menengah yang stabil. Berorientasi analitis dan menggabungkan preferensi kultur kolaboratif dengan gaya kerja dalam tim berukuran kecil.</div>",
                 unsafe_allow_html=True)

with tab2:
    kolom_numerik= [
        'Skor M2 (Skills)', 'Skor M5 (Compass)', 'Skor M8 (Ambisi)', 'Skor M9 (Resiliensi)',
        'Semester', 'IPK', 'Ekspektasi Gaji', 'Minat Wirausaha',
        'Rencana S2/Sertifikasi', 'Frekuensi Belajar', 'Kesiapan Interview', 'Level Bahasa Inggris'
    ]

    kolom_kategori = [
        'Motivasi', 'Cognitive Style', 'Work Style', 'Kultur Kerja', 'Ukuran Perusahaan'
    ]

    x = st.selectbox(
        'Pilih Kolom:',
        ['Skor M2 (Skills)', 
        'Skor M5 (Compass)',
        'Skor M8 (Ambisi)',
        'Skor M9 (Resiliensi)',
        'Semester',
        'IPK',
        'Ekspektasi Gaji',
        'Minat Wirausaha',
        'Rencana S2/Sertifikasi',
        'Frekuensi Belajar',
        'Level Bahasa Inggris',
        'Motivasi',
        'Cognitive Style',
        'Work Style',
        'Kultur Kerja',
        'Ukuran Perusahaan']
    )

    if x in kolom_numerik:
        plt.figure(figsize=(10, 6))
        
        # Membuat plot, mengatur judul plot, judul sumbu x, dan judul sumbu y, serta mengatur axis x  dan y
        sns.histplot(data=clustering, x= x, hue= 'Cluster', alpha= 0.6, discrete= True, multiple= 'layer', palette= 'tab10')
        plt.title(f'{x} Distribution', fontsize=14, fontweight='bold')
        plt.xlabel(x, family= 'serif', size= 12, weight= 'bold')
        plt.ylabel('Frekuensi', family= 'serif', size= 12, weight= 'bold')
        plt.xticks(family='serif', size= 9)
        plt.yticks(family='serif', size= 9)
        plt.ticklabel_format(style= 'plain', axis='both')

        st.pyplot(plt)
    elif x in kolom_kategori:
        ax = sns.countplot(data=clustering,
                    x= x,
                    order= clustering[x].value_counts().index,
                    hue= 'Cluster',
                    alpha= 0.6)
        plt.title(f'{x} Distribution', fontsize=14,fontweight='bold')
        plt.xlabel(x, family= 'serif', size= 12, weight= 'bold')
        plt.ylabel('Frekuensi', family= 'serif', size= 12, weight= 'bold')
        plt.xticks(family='serif', size= 9)
        plt.yticks(family='serif', size= 9)

        # Menambahkan keterangan Jumlah ulasan pada setiap bar nya
        for p in ax.patches:
            ax.annotate(f"{p.get_height()}", (p.get_x() + p.get_width()/2., p.get_height()),ha = "center", va = "bottom", fontsize = 10)

        st.pyplot(plt)

    yappingan = {
        'Skor M2 (Skills)': 'Puncak skor M2 terpusat di angka 9 melalui dominasi Klaster 1. Selanjutnya, Klaster 0 menguasai rentang skor tertinggi sedangkan observasi Klaster 2 lebih banyak menumpuk di area skor terendah.', 
        'Skor M5 (Compass)': 'Puncak distribusi skor M5 terpusat pada angka 8 dengan dominasi porsi dari Klaster 1. Selanjutnya, Klaster 0 terlihat menguasai perolehan skor tertinggi di angka 10 sedangkan sebagian besar observasi Klaster 2 berada pada rentang skor yang lebih rendah.',
        'Skor M8 (Ambisi)': 'Puncak distribusi skor ambisi didominasi oleh Klaster 1 pada rentang nilai menengah. Sementara itu, Klaster 0 secara jelas menguasai perolehan skor tertinggi dan mayoritas observasi Klaster 2 menumpuk pada skor terendah.',
        'Skor M9 (Resiliensi)': 'Mayoritas distribusi skor resiliensi terpusat pada rentang 6 hingga 8 dengan porsi terbesar diisi oleh Klaster 1. Sementara itu, distribusi Klaster 2 lebih banyak menumpuk pada skor yang lebih rendah di sekitar rentang 4 hingga 6, dan Klaster 0 mendominasi perolehan skor tertinggi.',
        'Semester': 'Distribusi semester terpusat secara signifikan pada semester 3 yang didominasi oleh penumpukan observasi dari Klaster 1 dan Klaster 0. Sebaliknya, frekuensi kemunculan pada semester lainnya terpantau jauh lebih sedikit dan tersebar cukup merata di semua klaster.',
        'IPK': 'Mayoritas distribusi IPK terpusat pada rentang tertinggi yakni 3,5 hingga 4,5 dengan porsi terbesar diisi oleh Klaster 1 dan Klaster 0. Sebaliknya, observasi pada rentang IPK di bawah 2,5 terlihat sangat minim secara keseluruhan di semua klaster.',
        'Ekspektasi Gaji': 'Puncak ekspektasi gaji berada pada level 2 dengan dominasi yang kuat dari Klaster 1. Selanjutnya, Klaster 0 terlihat menguasai tingkatan level yang lebih tinggi sedangkan distribusi Klaster 2 lebih banyak menumpuk di level terendah.',
        'Minat Wirausaha': 'Puncak minat wirausaha terletak pada level 4 dengan dominasi dari Klaster 1. Selanjutnya, Klaster 0 terlihat menguasai level tertinggi sedangkan distribusi Klaster 2 lebih terkonsentrasi pada level 3 ke bawah.',
        'Rencana S2/Sertifikasi': 'Rencana S2 atau sertifikasi terpusat pada rentang 1,5 hingga 2,5 dengan dominasi kuat dari Klaster 1. Selanjutnya, Klaster 0 menguasai tingkatan yang lebih tinggi dan Klaster 2 menumpuk di tingkat terendah.',
        'Frekuensi Belajar': 'Frekuensi belajar terpusat pada rentang 1,5 hingga 2,5 dengan dominasi Klaster 1. Klaster 0 menguasai level tertinggi dan Klaster 2 menumpuk di level terendah',
        'Level Bahasa Inggris': 'Mayoritas observasi terkonsentrasi pada level bahasa Inggris 1,5 hingga 2,5 dengan dominasi kuat dari Klaster 1. Sebaliknya, frekuensi kemunculan pada level yang lebih tinggi semakin menurun drastis dan mayoritas distribusinya diisi oleh Klaster 0.',
        'Motivasi': 'Distribusi motivasi menunjukkan bahwa kategori money merupakan faktor pendorong yang paling dominan secara keseluruhan dengan nilai frekuensi tertinggi dicatatkan oleh Klaster 1 sebesar 296,0. Sebaliknya, motivasi prestige dan freedom menjadi faktor dengan tingkat kemunculan paling rendah di semua kelompok, di mana Klaster 0 dan Klaster 2 masing-masing hanya mencatatkan nilai 23,0 pada kategori freedom.',
        'Cognitive Style': 'Gaya kognitif analitis mendominasi distribusi dengan frekuensi tertinggi dicatatkan oleh Klaster 1 yang mencapai nilai 347,0. Di sisi lain, kategori sosial menempati posisi kedua terbanyak dengan persebaran yang hampir seimbang antara Klaster 1 dan Klaster 2, sementara gaya strategis dan kreatif memiliki tingkat kemunculan yang jauh lebih rendah di semua klaster.',
        'Work Style': 'Kategori small dan flex merupakan yang paling dominan, di mana Klaster 1 mencatat frekuensi tertinggi pada kedua kategori tersebut dengan nilai masing-masing 237,0 dan 221,0. Sementara itu, gaya kerja big memiliki frekuensi paling rendah secara keseluruhan, sedangkan pada kategori solo Klaster 2 justru memimpin dibandingkan klaster lainnya dengan mencatatkan nilai sebesar 111,0.',
        'Kultur Kerja': 'Klaster 1 mencatat frekuensi tertinggi pada kultur collab dengan nilai mencapai 282,0, disusul oleh dominasi yang sama pada kultur formal sebanyak 242,0. Sebaliknya, kultur agile dan result memiliki tingkat kemunculan yang jauh lebih rendah secara keseluruhan, dengan klaster 0 sedikit memimpin pada kedua kategori tersebut melalui nilai frekuensi masing-masing sebesar 57,0 dan 38,0.',
        'Ukuran Perusahaan': ' Klaster 1 secara konsisten mendominasi frekuensi pada kategori ukuran perusahaan flex, mid, dan big, dengan jumlah tertingginya berada di kategori flex sebanyak 285 observasi. Sebaliknya, kategori startup memiliki frekuensi kemunculan terendah secara keseluruhan, di mana distribusinya relatif seimbang antara Klaster 0 (46) dan Klaster 1 (45).'
    }

    st.markdown(f"<div style='background-color: #f4f6f9; padding: 15px; border-left: 5px solid #0133A1; border-radius: 5px;'><i>💡 <b>Insight:</b> {yappingan.get(x, '')}</i></div>", unsafe_allow_html=True)

with tab3:
    selected_cluster = st.selectbox(
        'Pilih Cluster yang Ingin dilihat',
        ['All'] + list(sorted(clustering['Cluster'].unique()))
    )

    if selected_cluster == 'All':
        st.dataframe(clustering)
    else:
        cluster_sampel = clustering[clustering['Cluster'] == selected_cluster]
        st.dataframe(cluster_sampel)
        st.write(f'Cluster {selected_cluster} mencakup {len(cluster_sampel)/len(clustering)*100:.1f}% dari total data.')