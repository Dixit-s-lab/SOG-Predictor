import subprocess

input_file = "fred_docked.pdbqt"
output_file = "new.pdbqt"

try:
    subprocess.run(["obabel", input_file, "-O", output_file, "-m"], check=True)
    print(f"Conversion successful. Output written to {output_file}")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

