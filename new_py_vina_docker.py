import subprocess
import glob

receptor_file = '2d06.pdbqt'
output_folder = 'Output_files_pdbqt'

# Create the output folder if it doesn't exist
subprocess.run(['mkdir', '-p', output_folder])

# Get a list of all .pdbqt files in the current directory
ligand_files = glob.glob('*.pdbqt')

for ligand_file in ligand_files:
    output_file = f"{output_folder}/{ligand_file}_docked.pdbqt"
    
    command = [
        'vina',
        '--receptor', receptor_file,
        '--ligand', ligand_file,
        '--config', 'conf.txt',
        '--exhaustiveness', '8',
        '--out', output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Docking completed for {ligand_file}. Output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Docking failed for {ligand_file}. Command '{e.cmd}' returned non-zero exit status {e.returncode}.")

