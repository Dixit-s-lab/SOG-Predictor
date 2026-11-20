import os
import subprocess

for filename in os.listdir("."):
    if filename.endswith(".sdf") and filename != "template.sdf":
        molecule_name = os.path.splitext(filename)[0]
        print(f"Processing molecule: {molecule_name}")

        # Generate 3D coordinates using the distance geometry method
        print(f"Generating 3D coordinates for {molecule_name}")
        subprocess.run(["obabel", filename, "-O", f"{molecule_name}_3D.sdf", "--gen3D"])

        # Calculate molecular fingerprints for the 3D coordinates
        print(f"Calculating fingerprints for {molecule_name}")
        subprocess.run(["obabel", f"{molecule_name}_3D.sdf", "*.sdf", "-ofpt", "-xfFP4", "|", "grep", "-v", "Possible", "|", "awk", "'{print $1,$6}'", ">", f"{molecule_name}-FP4.txt"], shell=True)

        # Clean up temporary 3D SDF file
        os.remove(f"{molecule_name}_3D.sdf")

        print(f"Completed processing for {molecule_name}")

