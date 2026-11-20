import os
import subprocess

# Get the current working directory
cwd = os.getcwd()

# Loop over all .sdf files in the current directory
for sdf_file in os.listdir(cwd):
    if sdf_file.endswith(".sdf"):
        base_name = os.path.splitext(sdf_file)[0]
        pdbqt_file = f"{base_name}.pdbqt"
        # Run the mk_prepare_ligand.py command
        subprocess.run(["mk_prepare_ligand.py", "-i", sdf_file, "-o", pdbqt_file])

# making directory
subprocess.run(["rm", "-rf", "Prepared_Ligands_pdbqt"])
subprocess.run(["mkdir", "Prepared_Ligands_pdbqt"])
        
for files in os.listdir("."):
    if files.endswith(".pdbqt"):
    	subprocess.run(["mv", files, "Prepared_Ligands_pdbqt/"])
