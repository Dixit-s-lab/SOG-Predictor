import os
import subprocess

receptor_file = "ugt_cofac_pindolol"

for file in os.listdir("."):
    if file.endswith(".pdbqt"):
        ligand = os.path.splitext(file)[0]
        if ligand == receptor_file:
            continue
        else:
            print("Processing ligand", ligand)
            subprocess.run(["mkdir", "-p", ligand])
            subprocess.run(
                [
                    "vina", 
                    "--receptor", receptor_file + ".pdbqt", 
                    "--ligand", ligand + ".pdbqt", 
                    "--config", "conf.txt", 
                    "--exhaustiveness", "8", 
                    "--cpu", "22", 
                    "--out", ligand + "_out.pdbqt", 
                    "--seed", "1"  # Changed seed to 1
                ],
                check=True
            )

subprocess.run(["rm", "-rf", "Output_files_pdbqt"])
subprocess.run(["mkdir", "Output_files_pdbqt"])
for file in os.listdir("."):
    if file.endswith("_out.pdbqt"):
        subprocess.run(["mv", file, "Output_files_pdbqt/"])

