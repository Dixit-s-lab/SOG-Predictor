import requests
import csv

upload_url = r'http://xundrug.cn:5001/modules/upload0/'

def predict_pka(smi):
    param = {"Smiles": ("tmg", smi)}
    headers = {'token': 'O05DriqqQLlry9kmpCwms2IJLC0MuLQ7'}
    response = requests.post(url=upload_url, files=param, headers=headers)
    jsonbool = int(response.headers['ifjson'])
    if jsonbool == 1:
        res_json = response.json()
        if res_json['status'] == 200:
            return res_json['gen_datas']
        else:
            raise RuntimeError(f"Error for pKa prediction on SMILES {smi}: Bad status code")
    else:
        raise RuntimeError(f"Error for pKa prediction on SMILES {smi}: No JSON returned")

def main():
    input_file = "smiles.txt"
    output_csv = "pka_results.csv"

    try:
        with open(input_file, "r") as infile, open(output_csv, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Added "name" column
            writer.writerow(["smiles", "name", "nature", "atom_no", "pka"])  

            # Each line is expected like: SMILES   Name
            smiles_list = []
            for line in infile:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    smi, name = parts
                elif len(parts) == 1:
                    smi, name = parts[0], ""  # handle missing name
                else:
                    continue
                smiles_list.append((smi, name))
            
            for idx, (smi, name) in enumerate(smiles_list, 1):
                print(f"[{idx}/{len(smiles_list)}] Predicting pKa for: {smi} ({name})")
                try:
                    data_pka = predict_pka(smi)
                    rows = []

                    for nature in ["Acid", "Base"]:
                        if nature in data_pka:
                            for atom_no, pka_value in data_pka[nature].items():
                                rows.append([nature, atom_no, pka_value])

                    if rows:
                        # First row with SMILES + Name
                        writer.writerow([smi, name, *rows[0]])
                        for row in rows[1:]:
                            writer.writerow(["", "", *row])
                        print("  Success.")
                    else:
                        writer.writerow([smi, name, "None", "", ""])
                        print("  No pKa data found.")
                except Exception as e:
                    print("  Failed:", e)
                    writer.writerow([smi, name, "Error", "", str(e)])
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == "__main__":
    main()
