from rdkit import Chem
from rdkit.Chem.Draw import MolToImage, DrawingOptions
import os

# Set the input directory and output directory to the current working directory
input_dir = '.'
output_dir = '.'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Set the drawing options
options = DrawingOptions()
options.atomLabelFontSize = 12
options.dotsPerAngstrom = 100

# Loop over each SDF file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.sdf'):
        # Read the SDF file
        sdf_file = os.path.join(input_dir, filename)
        mols = [mol for mol in Chem.SDMolSupplier(sdf_file)]

        # Loop over each molecule in the file
        for i, mol in enumerate(mols):
            if mol is not None:
                # Add atom numbering to the molecule
                for atom in mol.GetAtoms():
                    atom.SetProp('atomLabel', str(atom.GetIdx() + 1))

                # Generate the image
                img = MolToImage(mol, size=(400, 400), options=options)

                # Set the output filename
                base_filename, ext = os.path.splitext(filename)
                img_file = f'{base_filename}_{i+1}.png'
                img_file = os.path.join(output_dir, img_file)

                # Save the image
                img.save(img_file)
