import os
import subprocess

from sdf_smi import *

# List all .smi files in the current directory
smi_files = [f for f in os.listdir() if f.endswith('.smi')]

# Loop through each .smi file
for smi_file in smi_files:
    # Check if the file contains isomeric SMILES
    with open(smi_file) as f:
        if '@@' in f.read():
            # If it's isomeric, convert it to canonical SMILES
            subprocess.run(["obabel", "-ismi", smi_file, "-ocan", "-O" + smi_file.rstrip('.smi') + ".can"])
            
            # Replace the original .smi file with the .can file
            os.rename(smi_file.rstrip('.smi') + ".can", smi_file)
for file in smi_files:
    # convert .smi to .sdf (2D)
    subprocess.run(["obabel", "-ismi", file, "-osdf", "-O" + file.rstrip('.smi') + ".sdf", "--gen2D"])
    
    # convert .sdf (2D) to .sdf (3D)
    sdf_2d = file.rstrip('.smi') + ".sdf"
    subprocess.run(["obabel", "-isdf", sdf_2d, "-osdf", "-O" + sdf_2d, "--gen3D"])
    


