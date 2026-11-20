import os
import subprocess

for files in os.listdir("."):
    if files.endswith(".sdf"):
    	ligand = files.rstrip('.sdf')
    	#subprocess.run(["obabel", "-isdf", files, "-osdf", "-O" + files.strip('.sdf') + "_conf.sdf", "--gen3d", "--conformer", "--nconf", "10", "--weighted", "--ff"], check=True)
    	subprocess.run(["obabel", files, "-O", ligand + "_conf.sdf", "--gen3d"], check=True)

for files in os.listdir("."):
    if files.endswith("conf.sdf"):
    	print("Converting molecule " + files.rstrip('.sdf'))
    	subprocess.run(["obabel", "-isdf", files, "-opdbqt", "-O" + files.rstrip('_conf.sdf') + ".pdbqt", "--partialcharge", "gasteiger"], check=True)

for files in os.listdir("."):
    if files.endswith("_conf.sdf"):
        os.remove(files)
    #if files.endswith("_lig.sdf"):
        #os.remove(files)

subprocess.run(["rm", "-rf", "Prepared_Ligands_pdbqt"])
subprocess.run(["mkdir", "Prepared_Ligands_pdbqt"])
        
for files in os.listdir("."):
    if files.endswith(".pdbqt"):
    	subprocess.run(["mv", files, "Prepared_Ligands_pdbqt/"])

#subprocess.run(["rm", "-rf", "Minimized_Ligands_sdf"])
#subprocess.run(["mkdir", "Minimized_Ligands_sdf"])
        
for files in os.listdir("."):
    if files.endswith("_lig.sdf"):
    	subprocess.run(["mv", files, "Minimized_Ligands_sdf/"])
    	
#subprocess.run(["mkdir", "Raw_Ligands_sdf"])

#for files in os.listdir("."):
    #if files.endswith(".sdf"):
    	#subprocess.run(["mv", files, "Raw_Ligands_sdf/"])
