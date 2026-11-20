import os

def modify_file_names(substrate=True):
    for files in os.listdir("."):
        if files.endswith(".sdf"):
            name = files.rstrip('.sdf')
            if substrate:
                name += "_substrate"
            else:
                name += "_nonsubstrate"
            with open(files) as f:
                line = f.readlines()
                line[0] = name + "\n"
            with open(files, "w") as f:
                f.writelines(line)

# Example usage:
substrate_choice = input("Do you want to add 'substrate' or 'nonsubstrate'? ")
if substrate_choice.lower() == "substrate":
    modify_file_names(substrate=True)
elif substrate_choice.lower() == "nonsubstrate":
    modify_file_names(substrate=False)
else:
    print("Invalid choice. Please enter 'substrate' or 'nonsubstrate'.")

