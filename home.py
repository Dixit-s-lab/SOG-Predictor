import streamlit as st
from PIL import Image

GA = Image.open("troglita-sos.jpg")
def home_page():
    with st.container():
        st.image(GA)
