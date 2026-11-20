#!/usr/bin/env python

import os
from rdkit import Chem
from rdkit.Chem import AllChem

# Define a function to process a molecule
def process_molecule(molecule):
    i = molecule.replace('.sdf', '')

    print(f"Processing molecule: {i}")
    
    # Read the input molecule
    mol_supplier = Chem.SDMolSupplier(molecule)  # Use the input molecule filename directly
    mol = mol_supplier[0]

    if mol is not None:
        # Add explicit hydrogen atoms
        mol = Chem.AddHs(mol)
        
        # Generate 3D coordinates using the ETKDG method
        AllChem.EmbedMolecule(mol, AllChem.ETKDG())
        
        # Calculate molecular fingerprints
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
        fp_bits = list(fp.GetOnBits())

        with open(f"{i}-FP4.txt", 'w') as fp_file:
            for bit in fp_bits:
                fp_file.write(f"{bit}\n")

        print(f"Completed processing for {i}")
    else:
        print(f"Failed to read molecule: {i}")

# Process each molecule
sdf_files = [file for file in os.listdir('.') if file.endswith('IN.sdf')]

for sdf_file in sdf_files:
    process_molecule(sdf_file)
