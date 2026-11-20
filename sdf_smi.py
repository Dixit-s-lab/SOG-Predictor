import os
import subprocess

def sdf2smi(file):
    base = os.path.splitext(file)[0]
    smi_file = base + ".smi"
    subprocess.run(["obabel", "-isdf", file, "-osmi", "-O" + smi_file])

for file in os.listdir():
    if file.endswith(".sdf"):
        sdf2smi(file)

