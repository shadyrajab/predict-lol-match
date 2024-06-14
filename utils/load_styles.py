import streamlit as st

def load_styles():
    with open("styles/home.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)