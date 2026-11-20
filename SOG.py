# Avik did something here
import os
import subprocess
import os
import time
import datetime
from tqdm import tqdm
import shutil
import os, datetime;
datestring = datetime.datetime.now().strftime("result-%d-%m-%Y-%H-%M-%S");
#print (datestring);

# removing old sdf files and folder
###########################################
def remove_old_files_and_directories():
    current_time = time.time()

    for item in os.listdir():
        item_path = os.path.join(os.getcwd(), item)

        # Exclude the ".streamlit" directory
        if item == ".streamlit":
            continue

        # Check if it's a file or directory
        if os.path.isfile(item_path):
            # For files
            if item.endswith((".sdf", ".smi")):
                file_mtime = os.path.getmtime(item_path)
                if current_time - file_mtime > 180:
                    os.remove(item_path)
                    print(f"Removed file: {item}")

        elif os.path.isdir(item_path):
            # For directories
            dir_mtime = os.path.getmtime(item_path)
            if current_time - dir_mtime > 180:
                shutil.rmtree(item_path)
                print(f"Removed directory: {item}")

if __name__ == "__main__":
    remove_old_files_and_directories()
##########################################
os.mkdir(datestring);



for i in tqdm(range(10), desc="BEGINNING DEPENDENCIES CHECK"):
    #time.sleep(0.1)
    pass
depen = ['Lig_Prep.py', 'obabel_converter.py', 'Result_analysis_for_tanimoto.py', 'Py_Vina_Docker.py',
         'sdf-intra-tanimoto-FP4.sh', 'calculate_using_pdbqt_OEOutput.py', 'main_program_modified.py',
         'Run_Bash_Script.py', 'Tanimoto_all_sdf', 'File_header_for_tanimoto.py', 'SDF-Writer-RDkit.py',
         'BDE-calculator.py', 'File_eliminator.py', 'finding_OH_oxygen.py']
for i in range(len(depen)):
    print("Looking for " + depen[i] + " file in the directory")
    #time.sleep(0.1)
    if depen[i] in os.listdir():
        print(depen[i] + " Found ")

address = "/home/caddsys3/Documents/software/SOS_predictor/SOG_vina"
address1 = os.getcwd()
print("Address 1 is = ", address1)
#fos.mkdir(address + "/Result")
# address = "/home/avik/Documents/ResearchProject/SULT/Final-script-work/sult-scripts/Files"
print("Changing current address to the desired address")
print("The current address directory is")
os.chdir(address)
subprocess.run(["pwd"])

print("Looking for sdf input files")

print("Converting 2D sdf input files to 3D")

from sdf_smi_sdrdkit import *

address7 = r"/home/caddsys3/Documents/software/SOS_predictor/server_files"

for files in os.listdir("."):
    if files.endswith(".sdf"):
        subprocess.run(["cp", files, address7])

print("Conversion of molecules from sdf to mol2 starts")

for files in os.listdir("."):
    if files.endswith(".sdf"):
        # subprocess.run(["obabel", files, "-omol2", "-m"])
        subprocess.run(["obabel", "-isdf", files, "-omol2", "-O" + files.rstrip('.sdf') + ".mol2"])

for i in tqdm(range(10), desc="Removing invalid SDF files starts"):
    #time.sleep(0.1)
    pass
print("Going through all mol2 files")

print("Checking for invalid input molecules containing no Hydroxyl groups")

from File_eliminator import *  # Removing for invalid input molecules containing no Hydroxyl groups

# Checking Tanimoto similarity of Input molecules begins

for i in tqdm(range(10), desc="Checking Tanimoto similarity of Input molecules begins now"):
    #time.sleep(0.1)
    pass
print("Changing File headers of input SDF files ")

print("Creating separate input files for Tanimoto calculation ")

from File_header_for_tanimoto import *

print("Moving input molecules to test dataset folder 'Tanimoto_all_sdf' ")

os.mkdir(address + "/Tanimoto_all_sdf")


for files in os.listdir("."):
    if files.endswith("_IN.sdf"):
        subprocess.run(["mv", files, "Tanimoto_all_sdf/"])

subprocess.run(["cp", "process_mol.py", "Tanimoto_all_sdf/"])

print("Changing current directory to test dataset folder 'Tanimoto_all_sdf' ")

# address2 = address + "/Tanimoto_all_sdf/Prepared_Ligands_pdbqt"


os.chdir(address + "/Tanimoto_all_sdf")

for i in tqdm(range(10), desc="Similarity calculation for input molecules starts"):
    #time.sleep(0.1)
     pass

from process_mol import *

for i in tqdm(range(10), desc="Output file screening based on range starts "):
    #time.sleep(0.1)
    pass

#from Result_analysis_for_tanimoto import *

os.chdir(address)



from Lig_Prep_rd import *    # AT THIS POINT 2d06 is removed LINE 24


address2 = address1 + "/Prepared_Ligands_pdbqt"
print("Address 2 is =", address2)


os.chdir(address1)
print(os.getcwd())
#subprocess.run(["cp", "conf.txt", address2])
subprocess.run(["cp", "conf.txt", address2])
subprocess.run(["cp", "Py_Vina_Docker.py", address2])

os.chdir(address2)
subprocess.run(["pwd"])
print(os.listdir())

from Py_Vina_Docker import *

address3 = address2 + "/Output_files_pdbqt"
os.chdir(address3)
subprocess.run(["pwd"])
print(os.listdir())

os.chdir(address)
subprocess.run(["cp", "main_program_modified.py", address3])
subprocess.run(["cp", "obabel_converter.py", address3])
subprocess.run(["cp", "finding_OH_oxygen.py", address3])
subprocess.run(["cp", "calculating_atom_dist_test.py", address3])
#subprocess.run(["cp", "calculate_using_pdbqt_OEOutput.py", address3])

os.chdir(address3)
print(address3)
from main_program_modified import *

os.mkdir(address3 + "/BDE-calculation")
address4 = address3 + "/BDE-calculation"
os.chdir(address3)
#print(os.listdir())
for files in os.listdir("."):
    if files.endswith(".pdbqt"):
        subprocess.run(["mv", files, address4])

os.chdir(address)
#if not os.path.exists("address/Results"):
#os.mkdir("address/Results")

os.mkdir(address + "/Results")
address5 = address + "/Results"
print(address5)

address7 = r"/home/caddsys3/Documents/software/SOS_predictor/server_files"
subprocess.run(["cp", "mopac_inp_file_creator.py", address4])
subprocess.run(["cp", "BDE-calculator.py", address4])
subprocess.run(["cp", "get-mopac-Es-2.sh", address4])
subprocess.run(["cp", "new_modelxl.py", address4])

os.chdir(address4)

from mopac_inp_file_creator import *
subprocess.call(['bash', 'get-mopac-Es-2.sh'])
os.chdir(address3)
subprocess.run(["cp", "Final_Output_OH_OXYGEN_only.txt", address4])
os.chdir(address4)
from new_modelxl import *
subprocess.run(["cp", "Accesibility_Model_NEW.csv", address5])
subprocess.run(["cp", "Accesibility_Model_NEW.csv", "/home/caddsys3/Documents/software/SOS_predictor/server_files/"])
os.chdir(address2)
subprocess.run(["cp", "ugt_cofac_pindolol.pdbqt", address])
os.chdir(address)

for files in os.listdir("."):
    if files.endswith(".smi"):
        subprocess.run(["mv", files, address5])

for files in os.listdir("."):
    if files.endswith(".mol2"):
        subprocess.run(["mv", files, address5])



for files in os.listdir("."):
    if files.endswith(".sdf"):
        subprocess.run(["mv", files, address5])

# files transfer in results directory

original = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Prepared_Ligands_pdbqt"

original1 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Invalid_SDF_molecules"


original2 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Tanimoto_all_sdf"

original3 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/__pycache__"


original4 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Results"


#print (os. getcwd())

target = datestring
shutil.move(original, target)
shutil.move(original1, target)
shutil.move(original2, target)
shutil.move(original3, target)
shutil.move(original4, target)

target1 = r"/home/caddsys3/Documents/software/SOS_predictor/sos-predictor-all-results"



shutil.move(target, target1)


