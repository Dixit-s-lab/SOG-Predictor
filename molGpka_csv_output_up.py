import requests
import csv
import time
import os

UPLOAD_URL = "http://xundrug.cn:5001/modules/upload0/"
TOKEN = "O05DriqqQLlry9kmpCwms2IJLC0MuLQ7"

INPUT_FILE = "smiles.txt"
OUTPUT_FILE = "pka_results.csv"

MAX_RETRIES = 5
REQUEST_DELAY = 8   # normal delay between molecules


def predict_pka(smiles):

    param = {"Smiles": ("tmg", smiles)}

    headers = {
        "token": TOKEN,
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(
        UPLOAD_URL,
        files=param,
        headers=headers,
        timeout=30
    )

    if response.status_code == 429:
        raise RuntimeError("RATE_LIMIT")

    if response.status_code != 200:
        raise RuntimeError(f"HTTP error {response.status_code}")

    try:
        res_json = response.json()
    except:
        raise RuntimeError("Server returned non-JSON response")

    if res_json.get("status") != 200:
        raise RuntimeError("API returned error status")

    return res_json.get("gen_datas", {})


def load_processed_smiles():

    processed = set()

    if not os.path.exists(OUTPUT_FILE):
        return processed

    with open(OUTPUT_FILE) as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            if row and row[0]:
                processed.add(row[0])

    return processed


def main():

    if not os.path.exists(INPUT_FILE):
        print("Error: smiles.txt not found")
        return

    processed_smiles = load_processed_smiles()

    with open(INPUT_FILE) as f:
        smiles_list = [line.strip() for line in f if line.strip()]

    write_header = not os.path.exists(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as csvfile:

        writer = csv.writer(csvfile)

        if write_header:
            writer.writerow(["smiles", "nature", "atom_no", "pka"])

        total = len(smiles_list)

        for idx, smi in enumerate(smiles_list, 1):

            if smi in processed_smiles:
                print(f"[{idx}/{total}] Skipping (already done)")
                continue

            print(f"[{idx}/{total}] Predicting pKa for: {smi}")

            success = False

            for attempt in range(1, MAX_RETRIES + 1):

                try:
                    data_pka = predict_pka(smi)

                    rows = []

                    for nature in ["Acid", "Base"]:
                        if nature in data_pka:
                            for atom_no, pka_value in data_pka[nature].items():
                                rows.append([nature, atom_no, pka_value])

                    if rows:
                        writer.writerow([smi, *rows[0]])
                        for row in rows[1:]:
                            writer.writerow(["", *row])
                    else:
                        writer.writerow([smi, "None", "", ""])

                    print("  Success")
                    success = True
                    break

                except Exception as e:

                    if str(e) == "RATE_LIMIT":
                        wait_time = 30 * attempt
                        print(f"  Rate limited. Waiting {wait_time} seconds...")
                        time.sleep(wait_time)

                    else:
                        print(f"  Attempt {attempt} failed:", e)
                        time.sleep(10)

            if not success:
                writer.writerow([smi, "Error", "", "Failed after retries"])

            csvfile.flush()

            time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
