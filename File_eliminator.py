import os
import subprocess
from pathlib import Path
from biopandas.mol2 import PandasMol2
import time

with open("Out.txt", "w") as outfile:
    print("These molecules don't contain OH groups. If you know for sure that this molecule do undergo sulfonation, "
          "it is quite possible that these molecules first undergo Phase I metabolism by CYP450s which introduce the "
          "OH group.  Thus you may want to pass these molecules through our Phase I models first.", file=outfile)
    print("The following files have been removed", file=outfile)
    print("The following files have been removed")
    pmol = PandasMol2()
    subprocess.run(["rm", "-rf", "Invalid_SDF_molecules"])
    print("Separating the invalid files in 'Invalid_molecules_sdf' folder if any")
    time.sleep(0.5)
    subprocess.run(["mkdir", "Invalid_SDF_molecules"])
    for files in os.listdir("."):
        if files.endswith(".mol2"):
            # for files in files_list:
            pmol.read_mol2(files)
            OH_atoms = pmol.df[pmol.df['atom_type'] == 'O.3']
            if OH_atoms.shape[0] == 0:
                # print("The following file have been removed")
                subprocess.run(["mv", files, "Invalid_SDF_molecules/"])
                subprocess.run(["mv", files.rstrip("mol2") + "sdf", "Invalid_SDF_molecules/"])
                print(files.rstrip(".mol2"), file=outfile)
                print(files.rstrip(".mol2"))
#        print('number of keto groups: %d' % OH_atoms.shape[0])
subprocess.run(["mv", "Out.txt", "Invalid_SDF_molecules/"])
