import streamlit as st

st.set_page_config(page_title="About the Creator", layout="wide")

st.markdown("""
    <style>
        header[data-testid="stHeader"] { display: none !important; }
        .block-container { padding-top: 0rem !important; }
        [data-testid="stSidebar"] { display: none !important; }
        .nav {
            display: flex;
            gap: 40px;
            background-color: #FFFFFF;
            padding: 15px 30px;
            margin-bottom: 30px;
        }
        .nav a {
            color: black;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }
        .nav a:hover { text-decoration: underline; }
    </style>
    <div class="nav">
        <a href="/" target="_self"> Home Page </a>
        <a href="/About_Creators" target="_self"> About the Creator </a>
        <a href="/Quiz" target="_self"> Carrer Quiz </a>
    </div>
""", unsafe_allow_html=True)

st.title("About the Creator 👤")
st.write("Hi! We are the creators of this project.")