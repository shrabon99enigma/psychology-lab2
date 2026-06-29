import streamlit as st


def apply_theme():
    st.markdown("""
    <style>

    .stApp{
        background:#050505;
        color:#00ff66;
    }

    h1,h2,h3,h4,p,label{
        color:#00ff66 !important;
    }

    .stTextInput>div>div>input{
        background:#111111;
        color:#00ff66;
        border:2px solid #00ff66;
        border-radius:10px;
    }

    .stButton>button{
        width:100%;
        background:#00ff66;
        color:black;
        font-weight:bold;
        border-radius:10px;
        border:none;
        padding:12px;
    }

    .stButton>button:hover{
        background:#00cc55;
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)