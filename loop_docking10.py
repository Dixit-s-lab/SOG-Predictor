import os
import shutil

# set directory paths
source_dir = "/home/cadd-sys3/Documents/shivam/subs-non-subs-sdf"  # directory with .sdf files
dest_dir = "/home/cadd-sys3/Documents/shivam/server-test"  # directory to copy .sdf files

# set number of times to run the loop
num_runs = 10

for i in range(num_runs):
    # copy .sdf files to destination directory
    for file in os.listdir(source_dir):
        if file.endswith(".sdf"):
            shutil.copy(os.path.join(source_dir, file), dest_dir)
    
    # run the python script
    os.system("python SOS_ten_models.py")
    
    # remove .sdf files from destination directory
    for file in os.listdir(dest_dir):
        if file.endswith(".sdf"):
            os.remove(os.path.join(dest_dir, file))
            





