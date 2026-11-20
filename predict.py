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

header_logo1 = Image.open("sos_predictor_toc.tif")

# Resize the image to fit the screen
header_logo1 = header_logo1.resize((int(header_logo1.width * 0.8), int(header_logo1.height * 0.8)))

with st.container():
    #new_image = header_logo1.resize((1200, 200))
    
    st.image(header_logo1, use_column_width=True)
     
     


    st.markdown("""
    <style>
    .big-font {
        font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('''
    <div style="background-color:#FEDCDC; padding:10px">
        <p style="font-size:45px; font-weight:bold; text-align:center">
            This Web Server allows the Prediction of Phase II Drug Metabolism catalyzed by Sulfotransferase Enzyme 
        </p>
        <p style="font-size:30px; text-align:center">
            It will classify input Molecules into Substrates and Non-substrates. For substrate molecules, the site of sulphonation (SOS) will be displayed along with the atom number. 
            This type of Prediction is essential when a Substrate Molecule has Multiple groups and site-specific information is required.
        <p style="font-size:20px; text-align:center">
            For more information, please see the respective tabs. If you have any questions or problems, please use the contact form below.
''', unsafe_allow_html=True)
    
    
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


def home_page():
	pass
    
from details import detail_page
from team import team_page
from contact import contact_page

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 25px;
}


button> div[data-testid="stMarkdownContainer"] > p {
  font-size: 25px;
}
</style>
"""

st.write(font_css, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Details", "Team", "Contact"])

with tab1:
    home_page()

with tab2:
    detail_page()

with tab3:
    team_page()


with tab4:
    contact_page()


        
result=pd.DataFrame()
result_path=''
molname=[]
SMILES=[]
output = BytesIO()
st.header("Please Upload an sdf file only")
#st.markdown('<div style="background-color:#EEEDED;  font-weight: bold;padding:15px"><p class="big-font" align="center">Please load an .sdf file only</p></div>', unsafe_allow_html=True)
input_file = st.file_uploader("",type=['sdf'])
predict_button = st.button('Predict')

extra_directoty=glob.glob("/home/caddsys3/Documents/software/SOS_predictor/server-test/*/")    



if input_file:
    for dir in extra_directoty:
        subprocess.run(['rm', '-rf', dir])
        
    
    if predict_button:
        placeholder = st.empty()
        placeholder.markdown("<html><body>Please wait for job completion... <progress></progress></body></html>", unsafe_allow_html=True)
       

        save_folder = "/home/caddsys3/Documents/software/SOS_predictor/server-test"
        save_path = Path(save_folder, input_file.name)
        with open(save_path, mode='wb') as w:
            w.write(input_file.getvalue())


        if save_path.exists():
            #st.success(f'File {input_file.name} is successfully saved!')
            subprocess.run(['python', 'SOS.py'])
            result_folder = "/home/caddsys3/Documents/software/SOS_predictor/server_files/Accesibility_Model_NEW.csv"            
            result_path = result_folder #Path(result_folder, input_file.name)
            
            #list_of_files = glob.glob('/home/ubuntu/Documents/shivam/sos-predictor-all-results/*/Results/*.csv') # * means all if need specific format then *.csv
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
                    atom_id=list(result['AtomID'])
                    files='/home/caddsys3/Documents/software/SOS_predictor/server_files/'+input_file.name
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
                            d = rdMolDraw2D.MolDraw2DCairo(250, 200)
                            #m.GetAtomWithIdx(57).SetProp('atomNote', 'sos') 
                            #m.drawOptions().addAtomIndices = True
                            #d.DrawMolecule(m)
                            #d.FinishDrawing()
                            
                            #st.markdown(m)
                            imgfile = molname[i].rstrip('sdf') + '.png'
                            #m.WriteDrawingText('imgfile')
                            #print(imgfile)
                            #m.__sssAtoms = [38]                            
                            Draw.MolToFile(m, imgfile)
                            #Draw.MolToFile(mol_with_atom_index(m))
                            pbar.close()
                            placeholder.empty()
                    break
        
        #st.dataframe(data=result, width=800, height=200)
        result_html = '''<div align="center" style="background-color:#EEEDED; margin:10px"><h3 align="center" style="background-color:#E7F1F3;"> Prediction Result</h3><font size="6"  >'''+result.to_html()+'</font></body></html>'
        st.markdown(result_html,  unsafe_allow_html=True)
        
        
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(result)
        st.download_button( "Press to Download", csv,"Result_file.csv","text/csv",key='download-csv')
        #update result accessibility file name
        file='/home/caddsys3/Documents/software/SOS_predictor/server_files/'+ input_file.name
        
        update_result = file.rstrip('sdf') + "csv"
        subprocess.run(['mv', result_path, update_result])
        
        for i in range(len(molname)):
            image = Image.open(molname[i].rstrip('sdf') + '.png')
            new_image = image.resize((600, 400))
            st.image(new_image)
# right coloum image
logo1 = Image.open("troglita-sos.jpg")

# Resize the image to fit the screen
logo1 = logo1.resize((int(logo1.width * 0.8), int(logo1.height * 0.8)))           


# create a container
container = st.container()

# add content to container
with container:
    st.write("---")
    columns = st.columns(2)

    with columns[0]:
        st.write(f'<h1 style="text-align: center;">HOW TO RUN SOS PREDICTOR!</h1>', unsafe_allow_html=True)
        #st.header("HOW TO RUN SOS PREDICTOR")
        #st.header("*For the Prediction of Site of Sulphonation in the input molecule please keep  following things in mind:")
                
        st.header("* Upload only SDF file without any specific character like underscore(_),  dash(-), and number in the file name.")
               
        st.header("* SDF file should have at least one Hydroxy (-OH) group.") 
        st.header("* Input Molecule having charge on the Molecule or Molecular fragment are  not a valid input for Prediction.")
                
        st.header("* When Input molecule have carboxilic group in molecule please note atomic No of COOH group.")
                


    with columns[1]:
        st.image(logo1, use_column_width=True)
        pass

# set the width of the left column to 70%
columns[0]._width = '50%'


#with right_column:
        #st.image(logo1, use_column_width=True)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact to Developer")
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

st.write('')       
st.write('', scroll_to_top=True)


