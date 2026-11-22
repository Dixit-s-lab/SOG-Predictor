import streamlit as st
#from server_test.predict import prediction
from predict import prediction
from home import home_page
from contact import contact_page
from details import detail_page
from team import team_page



from PIL import Image
header_logo1 = Image.open("top1.png")

with st.container():
     st.image(header_logo1)
    
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Predict", "Details", "Team", "Contact"])
with tab1:
    home_page()

with tab2:
    prediction()

with tab5:
    contact_page()

with tab3:
    detail_page()

with tab4:
    team_page()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style.css")
