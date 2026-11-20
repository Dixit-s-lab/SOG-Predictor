# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

def prepend_line(sdf-intra-tanimoto-FP4.sh, /home/shivam/Documents/SOS-predictor-test2/subnonsub):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = sdf-intra-tanimoto-FP4.sh + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(sdf-intra-tanimoto-FP4.sh, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(/home/shivam/Documents/SOS-predictor-test2/subnonsub + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(/home/shivam/Documents/SOS-predictor-test2/subnonsub)
    # remove original file
    os.remove(sdf-intra-tanimoto-FP4.sh)
    # Rename dummy file as the original file
    os.rename(dummy_file, sdf-intra-tanimoto-FP4.sh)

