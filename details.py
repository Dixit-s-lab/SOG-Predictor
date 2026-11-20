import streamlit as st
from PIL import Image

#fig1 = Image.open("/home/ubuntu/Documents/shivam/streamlit/images/shivam.jpeg")
'''
fig2 = Image.open("/home/ubuntu/Documents/shivam/streamlit/images/shivam.jpg")
fig3 = Image.open("images/.jpg")
fig4 = Image.open("images/.jpg")
fig5 = Image.open("images/.jpg")
'''
def detail_page():
    
    with st.container():
        st.subheader("Overview")
        st.write("Write something")
        #st.image(fig3)
    
    with st.container():
        st.subheader("methodology")
        st.write("Write something")
        #st.image(fig2)
    
    with st.container():
        st.subheader("methodology")
        st.write("Write something")
        #st.image(fig4)

    with st.container():
        st.subheader("methodology")
        
        
