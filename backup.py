import streamlit as st
import numpy as np 
import pandas as pd
import time
from pathlib import Path
from io import BytesIO
from io import StringIO
import os
import glob
from pathlib import Path
import os.path
import subprocess
from PIL import Image
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from tqdm import tqdm
st.set_page_config(layout="wide") 

from PIL import Image

header_logo1 = Image.open("top1.png")
with st.container():
     st.image(header_logo1)

with st.container():
    st.markdown("<h1 style='text-align: center; color: w;'>SITE OF SULPHONATION (SOS) PREDICTOR</h1>", unsafe_allow_html=True)
    
    #st.subheader("SITE OF SULPHONATION (SOS) PREDICTOR")
    #st.title("WELCOME")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://pythonandvba.com)")



#GA1 = Image.open('sos-msg.png')

#with st.container():
    
    #st.image(GA1)
    
#GA = Image.open("troglita-sos.jpg")
def home_page():
	pass
    #with st.container():
        #st.image(GA)

#from home import home_page
from details import detail_page
from team import team_page
from contact import contact_page

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Details", "Team", "Contact"])
with tab1:
    home_page()

with tab2:
    detail_page()

with tab3:
    team_page()


with tab4:
    contact_page()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
        


result=pd.DataFrame()
result_path=''
molname=[]
SMILES=[]
output = BytesIO()
input_file = st.file_uploader("load an .sdf file only",type=['sdf'])
predict_button = st.button('Predict')

if input_file:
    if predict_button:
        placeholder = st.empty()
        placeholder.markdown("<html><body>Please wait for job completion... <progress></progress></body></html>", unsafe_allow_html=True)
       

        save_folder = "/home/cadd-sys3/Documents/shivam/server-test/"
        save_path = Path(save_folder, input_file.name)
        with open(save_path, mode='wb') as w:
            w.write(input_file.getvalue())


        if save_path.exists():
            #st.success(f'File {input_file.name} is successfully saved!')
            subprocess.run(['python', 'SOS.py'])
            result_folder = "/home/cadd-sys3/Documents/shivam/server_files/Accesibility_Model_NEW.csv"            
            result_path = result_folder #Path(result_folder, input_file.name)
            
            #list_of_files = glob.glob('/home/cadd-sys3/Documents/shivam/sos-predictor-all-results/*/Results/*.csv') # * means all if need specific format then *.csv
            #latest_file = max(list_of_files, key=os.path.getctime)
            
            #new code for atom number
            def mol_with_atom_index(mol):
                for atom in mol.GetAtoms():
                    atom.SetAtomMapNum(atom.GetIdx())
                return mol
            p=0
            pbar=tqdm(desc='while loop',total=1000000)
            while True:
                p=p+1
                pbar.update(p)
                #if my_file.is_file():
                if os.path.isfile(result_path): 
                    result=pd.read_csv(result_path)
                    files='/home/cadd-sys3/Documents/shivam/server_files/'+input_file.name
                    molname.append(files)
                    sminame = files.rstrip('sdf') + 'txt'
                    #print(sminame)
                    subprocess.run(["obabel", files, "-o", "smi", "-O", files.rstrip('sdf') + "txt", "-h"], check=True)
                    with open(sminame) as f:
                        line = f.readlines()
                        for i in range(len(line)):
                            SMILES.append(line[i].split("\t")[0])
                        for i in range(len(SMILES)):
                            smi = SMILES[i]
                            #print(smi)
                            
                            m = Chem.MolFromSmiles(smi)
                            #st.markdown(m)
                            imgfile = molname[i].rstrip('sdf') + '.png'
                            #print(imgfile)
                            Draw.MolToFile(mol_with_atom_index(m), imgfile)
                            pbar.close()
                            placeholder.empty()
                    break
        #st.markdown(result.to_html)
        #result_html = '<html><body>'+result.to_html()+'</body></html>'
        #st.markdown(result,unsafe_allow_html=True)

        st.write(result)
        
        
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(result)
        st.download_button( "Press to Download", csv,"Result_file.csv","text/csv",key='download-csv')
        #update result accessibility file name
        file='/home/cadd-sys3/Documents/shivam/server_files/'+ input_file.name
        #files.rstrip('.sdf') + ".mol2"
        update_result = file.rstrip('sdf') + "csv"
        subprocess.run(['mv', result_path, update_result])
        
        
        for i in range(len(molname)):
            image = Image.open(molname[i].rstrip('sdf') + '.png')
            new_image = image.resize((600, 400))
            st.image(new_image)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/vyasshivam16@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WORKFLOW OF SOS PREDICTOR")
        st.write("##")
        st.write(
            """
            In this workflow following steps will complete for prediction of site of sulphonation:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    
logo1 = Image.open("troglita-sos.jpg")
    
with right_column:
        st.image(logo1)



