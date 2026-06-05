import streamlit as st
from ui import sidebar

st.set_page_config(
    page_title="Student Archetype | VINIX7", 
    page_icon="🎓", 
    layout="centered"
)

sidebar()

st.markdown("""
    <style>
    /* Ubah font judul utama */
    h1 {
        color: #0133A1; /* Navy Blue khas VINIX7 */
        font-weight: 800;
        text-align: center;
    }
    /* Styling Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Segmentasi Karakteristik dan Ambisi Mahasiswa (Student Archetype)</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555555;'>Pendekatan Algoritma K-Means (Student Archetype)</h4>", unsafe_allow_html=True)
st.divider()

st.markdown("<h6 style='text-align: center; color: #555555;'>Oleh:\n\nJonathan Hutabarat | Ridha Wira Syawal Saputra | Ahmad Fauzan Awaluddin</h6>", unsafe_allow_html=True)
st.divider()

st.info("👈 **Mulai Eksplorasi!** Silakan pilih menu di *sidebar* untuk melihat *Dashboard Clustering* atau ingin melihat kamu masuk ke *Archetype* mana.")