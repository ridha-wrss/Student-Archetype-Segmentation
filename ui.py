import streamlit as st

def sidebar():
    st.sidebar.image('Logo.png', use_container_width=True)
    st.sidebar.markdown("---")
    st.sidebar.markdown("<h3 style='text-align: center; color: #0133A1;'>Menu Navigasi</h3>", unsafe_allow_html=True)

    st.markdown("""
        <style>
        [data-testid="stSidebarNav"] ul li a span {
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            color: #0133A1 !important;
            padding: 5px 0 !important;
        }
        [data-testid="stSidebarNav"] ul li a {
            border-radius: 8px !important;
            margin: 5px 15px !important;
            transition: all 0.3s ease;
        }
        [data-testid="stSidebarNav"] ul li a:hover {
            background-color: #FFD13B !important; 
            color: #0133A1 !important;
        }
        [data-testid="stSidebarNav"] ul li div:focus-visible {
            background-color: #F0F4FA !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.caption("© 2026 VINIX7 - Student Archetype")

def form():
    st.markdown("""
        <style>
        div[role="radiogroup"] {
            gap: 12px !important;
        }

        div[role="radiogroup"] > label {
            border: 1.5px solid #E0E4E8 !important; 
            border-radius: 10px !important; 
            padding: 12px 18px !important; 
            background-color: #FAFAFA !important; 
            box-shadow: 0px 2px 4px rgba(0,0,0,0.03) !important; 
            transition: all 0.3s ease-in-out !important; 
            margin: 0 !important; /* Hapus margin bawaan kita sebelumnya */
            flex: 1; /* Rahasia biar horizontal bagi rata ruangnya! */
            display: flex;
            align-items: center;
        }

        div[role="radiogroup"] > label:hover {
            border-color: #0133A1 !important; 
            background-color: #F0F4FA !important; 
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

def tab():
    st.markdown("""
        <style>
        button[role="tab"] {
            background-color: #FAFAFA !important;
            border-radius: 8px 8px 0 0 !important; /* Melengkung di atas, rata di bawah */
            border: 1.5px solid #E0E4E8 !important;
            border-bottom: none !important;
            margin-right: 5px !important;
            padding: 10px 24px !important;
            color: #555555 !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }

        button[role="tab"]:hover {
            background-color: #F0F4FA !important;
            color: #0133A1 !important;
        }

        button[role="tab"][aria-selected="true"] {
            background-color: #0133A1 !important; /* Navy Blue VINIX7 */
            color: #FFFFFF !important; /* Teks Putih */
            border: 1.5px solid #0133A1 !important;
            border-bottom: 4px solid #FFD13B !important; /* Garis bawah Gold */
        }

        div[data-baseweb="tab-highlight"] {
            display: none !important;
        }

        div[data-testid="stMarkdownContainer"] {
            padding-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

def button():
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #5BC0DE !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FFD13B !important;
        color: #5BC0DE !important;
    }
    </style>
""", unsafe_allow_html=True)
