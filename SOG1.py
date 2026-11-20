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

os.mkdir(datestring);

#address = "/home/caddsys3/Documents/software/SOS_predictor/SOG_vina"
address1 = os.getcwd()
print("Address 1 is = ", address1)

print("Changing current address to the desired address")
print("The current address directory is")
#############
# copying all scripts

scripts = "/home/caddsys3/Documents/software/SOS_predictor/SOG_scripts"
os.chdir(scripts)


# Define the paths
scripts = "/home/caddsys3/Documents/software/SOS_predictor/SOG_scripts"  # Update this to the actual path
address = address1  # Update this to the actual path

# Change the current working directory to 'scripts' directory
try:
    os.chdir(scripts)
    print(f"Changed working directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"The directory {scripts} does not exist.")
    exit(1)

# Ensure the destination directory exists
if not os.path.exists(address1):
    os.makedirs(address1)
    print(f"Created destination directory: {address1}")

# Copy all contents from 'scripts' directory to 'address1' directory
try:
    for item in os.listdir(scripts):
        source = os.path.join(scripts, item)
        destination = os.path.join(address1, item)
        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)
    print(f"Copied all contents from {scripts} to {address1}")
except Exception as e:
    print(f"An error occurred: {e}")

#############
os.chdir(address1)

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

os.mkdir(address1 + "/Tanimoto_all_sdf")


for files in os.listdir("."):
    if files.endswith("_IN.sdf"):
        subprocess.run(["mv", files, "Tanimoto_all_sdf/"])

subprocess.run(["cp", "process_mol.py", "Tanimoto_all_sdf/"])

print("Changing current directory to test dataset folder 'Tanimoto_all_sdf' ")

# address2 = address + "/Tanimoto_all_sdf/Prepared_Ligands_pdbqt"


os.chdir(address1 + "/Tanimoto_all_sdf")

for i in tqdm(range(10), desc="Similarity calculation for input molecules starts"):
    #time.sleep(0.1)
     pass

from process_mol import *

for i in tqdm(range(10), desc="Output file screening based on range starts "):
    #time.sleep(0.1)
    pass

#from Result_analysis_for_tanimoto import *

os.chdir(address1)



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

os.chdir(address1)
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

os.chdir(address1)
#if not os.path.exists("address1/Results"):
#os.mkdir("address1/Results")

os.mkdir(address1 + "/Results")
address5 = address1 + "/Results"
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
subprocess.run(["cp", "ugt_cofac_pindolol.pdbqt", address1])
os.chdir(address1)

for files in os.listdir("."):
    if files.endswith(".smi"):
        subprocess.run(["mv", files, address5])

for files in os.listdir("."):
    if files.endswith(".mol2"):
        subprocess.run(["mv", files, address5])



for files in os.listdir("."):
    if files.endswith(".sdf"):
        subprocess.run(["mv", files, address5])
########################
# Or use os.getcwd() to automatically get the current working directory
address1 = os.getcwd()

# Define the original paths using the address1 variable
original = os.path.join(address1, "Prepared_Ligands_pdbqt")
original1 = os.path.join(address1, "Invalid_SDF_molecules")
original2 = os.path.join(address1, "Tanimoto_all_sdf")
original4 = os.path.join(address1, "Results")

# Define the target directory using a date string
#datestring = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
target = os.path.join(address1, datestring)

# Create the target directory if it does not exist
os.makedirs(target, exist_ok=True)

# Function to move directories with error handling
def move_directory(src, dst):
    try:
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")
    except FileNotFoundError:
        print(f"Directory {src} not found.")
    except shutil.Error as e:
        print(f"Error moving {src} to {dst}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Move the directories
move_directory(original, target)
move_directory(original1, target)
move_directory(original2, target)
move_directory(original4, target)

########################
# files transfer in results directory
"""
original = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Prepared_Ligands_pdbqt"

original1 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Invalid_SDF_molecules"


original2 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Tanimoto_all_sdf"

#original3 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/__pycache__"


original4 = r"/home/caddsys3/Documents/software/SOS_predictor/SOG_vina/Results"


#print (os. getcwd())

target = datestring
shutil.move(original, target)
shutil.move(original1, target)
shutil.move(original2, target)
#shutil.move(original3, target)
shutil.move(original4, target)
"""
target1 = r"/home/caddsys3/Documents/software/SOS_predictor/sos-predictor-all-results"



shutil.move(target, target1)


