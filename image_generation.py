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

result=pd.DataFrame()
result_path=''
molname=[]
SMILES=[]
result=pd.read_csv("/home/cadd-sys3/Documents/shivam/server_files/Accesibility_Model_NEW.csv"  )
atom_id=list(result['AtomID'])
files='/home/cadd-sys3/Documents/shivam/server_files/Acebutolol.sdf'
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
        m.__sssAtoms = atom_id
        Draw.MolToFile(m, imgfile)
