import os
import subprocess

for files in os.listdir("."):
    if files.endswith(".sdf"):
    	print("Converting molecule " + files.rstrip('.sdf'))
    	subprocess.run(["obabel", "-isdf", files, "-opdbqt", "-O" + files.rstrip('.sdf') + ".pdbqt", "--partialcharge", "gasteiger"], check=True)

for files in os.listdir("."):
    if files.endswith(".sdf"):
        os.remove(files)
    

subprocess.run(["rm", "-rf", "Prepared_Ligands_pdbqt"])
subprocess.run(["mkdir", "Prepared_Ligands_pdbqt"])
        
for files in os.listdir("."):
    if files.endswith(".pdbqt"):
    	subprocess.run(["mv", files, "Prepared_Ligands_pdbqt/"])


"""       
for files in os.listdir("."):
    if files.endswith("_lig.sdf"):
    	subprocess.run(["mv", files, "Minimized_Ligands_sdf/"])
"""
    	

