import os
import pandas as pd

# Target metrics (compared after rounding to 2 decimal places)
target_tpr = 0.96
target_fpr = 0.17
CUTOFF_DECIMALS = 4
METRIC_DECIMALS = 4


def read_all_excel_files():
    files = [f for f in os.listdir() if f.lower().endswith(".xlsx")
             and not f.startswith("~$")]
    return [(file, pd.read_excel(file)) for file in files]


def calculate_metrics(data, cutoff):
    """Calculate classification metrics without modifying the input DataFrame."""
    predicted_y = data["Molecular Weight"] <= cutoff
    actual_y = data["Annotation"].eq("Y")
    actual_n = data["Annotation"].eq("N")

    tp = int((actual_y & predicted_y).sum())
    fn = int((actual_y & ~predicted_y).sum())
    fp = int((actual_n & predicted_y).sum())
    tn = int((actual_n & ~predicted_y).sum())

    tpr_raw = tp / (tp + fn) if (tp + fn) else 0.0
    fpr_raw = fp / (fp + tn) if (fp + tn) else 0.0
    tnr_raw = tn / (tn + fp) if (tn + fp) else 0.0
    accuracy_raw = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) else 0.0
    balanced_accuracy_raw = (tpr_raw + tnr_raw) / 2

    return {
        "Cutoff": round(float(cutoff), CUTOFF_DECIMALS),
        "TP": tp, "FP": fp, "TN": tn, "FN": fn,
        "TPR": round(tpr_raw, METRIC_DECIMALS),
        "FPR": round(fpr_raw, METRIC_DECIMALS),
        "TNR": round(tnr_raw, METRIC_DECIMALS),
        "Balanced Accuracy": round(balanced_accuracy_raw, METRIC_DECIMALS),
        "Accuracy": round(accuracy_raw, METRIC_DECIMALS),
        # Internal selection fields; removed from exported metrics
        "_tpr_raw": tpr_raw,
        "_fpr_raw": fpr_raw,
        "_balanced_accuracy_raw": balanced_accuracy_raw,
    }


excel_files = read_all_excel_files()
if not excel_files:
    print("No .xlsx files found in the current working directory.")

for file_path, original_data in excel_files:
    print(f"\nProcessing file: {file_path}")

    required = {"Molecular Weight", "Annotation", "Name"}
    missing = required - set(original_data.columns)
    if missing:
        print(f"Skipping {file_path}; missing columns: {sorted(missing)}")
        continue

    data = original_data.copy()
    data["Molecular Weight"] = pd.to_numeric(data["Molecular Weight"], errors="coerce")
    valid = data[data["Annotation"].isin(["Y", "N"])].copy()
    valid = valid.dropna(subset=["Molecular Weight"])

    if valid.empty:
        print(f"Skipping {file_path}; no valid Y/N annotations with numeric molecular weights.")
        continue

    max_value = float(valid["Molecular Weight"].max())
    min_value = float(valid["Molecular Weight"].min())
    std_dev = float(valid["Molecular Weight"].std())
    average = float(valid["Molecular Weight"].mean())

    # Exhaustive search: predictions can change only at observed molecular weights.
    # Include a cutoff just below the minimum to test the all-negative prediction.
    unique_weights = sorted(valid["Molecular Weight"].unique())
    epsilon = 10 ** (-(CUTOFF_DECIMALS + 2))
    # IMPORTANT: evaluate the exact cutoff value that will be displayed/exported.
    # Previously metrics were calculated at full precision but the cutoff was
    # displayed rounded to 4 decimals, so the same displayed cutoff could yield
    # different classifications from the user-cutoff molecule lists.
    candidate_cutoffs = [round(float(unique_weights[0]) - epsilon, CUTOFF_DECIMALS)]
    candidate_cutoffs += [round(float(x), CUTOFF_DECIMALS) for x in unique_weights]
    candidate_cutoffs = sorted(set(candidate_cutoffs))

    # Calculate metrics using the same rounded cutoff saved in the CSV.
    all_rows = [calculate_metrics(valid, cutoff) for cutoff in candidate_cutoffs]
    results = pd.DataFrame(all_rows)

    # Match targets using the same two-decimal convention as the original script.
    results["_target_match"] = (
        results["_tpr_raw"].round(2).eq(target_tpr)
        & results["_fpr_raw"].round(2).eq(target_fpr)
    )
    matches = results[results["_target_match"]]

    # Prefer exact target matches; otherwise minimize distance from both targets,
    # then prefer higher balanced accuracy.
    results["_target_distance"] = (
        (results["_tpr_raw"] - target_tpr).abs()
        + (results["_fpr_raw"] - target_fpr).abs()
    )
    ranked = results.sort_values(
        ["_target_match", "_target_distance", "_balanced_accuracy_raw"],
        ascending=[False, True, False]
    )
    best = ranked.iloc[0]

    print(f"Target TPR={target_tpr:.2f}, target FPR={target_fpr:.2f}")
    print(f"Meaningful cutoffs tested: {len(results)}")
    if not matches.empty:
        print(f"Found {len(matches)} cutoff(s) matching target TPR/FPR when rounded to 2 decimals.")
    else:
        print("No cutoff matched both targets; showing the closest overall trade-off.")
    print(
        f"Recommended cutoff: {best['Cutoff']:.{CUTOFF_DECIMALS}f} | "
        f"TPR={best['TPR']:.4f} | FPR={best['FPR']:.4f} | "
        f"TNR={best['TNR']:.4f} | Balanced Accuracy={best['Balanced Accuracy']:.4f} | "
        f"Accuracy={best['Accuracy']:.4f}"
    )

    summary_df = pd.DataFrame([
        {"Name": "Max", "Molecular Weight": round(max_value, CUTOFF_DECIMALS)},
        {"Name": "Min", "Molecular Weight": round(min_value, CUTOFF_DECIMALS)},
        {"Name": "Std Dev", "Molecular Weight": round(std_dev, CUTOFF_DECIMALS)},
        {"Name": "Average", "Molecular Weight": round(average, CUTOFF_DECIMALS)},
    ])
    summary_file = f"summary_{os.path.splitext(file_path)[0]}.csv"
    summary_df.to_csv(summary_file, index=False)
    print(f"Summary saved to {summary_file}")

    # Ask for a detailed cutoff; default to the recommended cutoff if blank.
    user_input = input(
        f"Enter cutoff for molecule lists (press Enter to use {best['Cutoff']:.4f}): "
    ).strip()
    try:
        user_cutoff = float(user_input) if user_input else float(best["Cutoff"])
    except ValueError:
        raise ValueError(f"Invalid cutoff value: {user_input!r}. Enter a number, e.g. 123.4567.")
    if not pd.notna(user_cutoff):
        raise ValueError("Cutoff must be a valid number.")
    # Use exactly four decimal places consistently in metrics and molecule files.
    user_cutoff = round(user_cutoff, CUTOFF_DECIMALS)

    # Build classifications once, then use this same classified DataFrame for
    # both the confusion-matrix row and the four molecule files.
    valid["Result"] = valid["Molecular Weight"].le(user_cutoff).map({True: "Y", False: "N"})
    actual_y = valid["Annotation"].eq("Y")
    actual_n = valid["Annotation"].eq("N")
    predicted_y = valid["Result"].eq("Y")
    tp = int((actual_y & predicted_y).sum())
    fp = int((actual_n & predicted_y).sum())
    tn = int((actual_n & ~predicted_y).sum())
    fn = int((actual_y & ~predicted_y).sum())

    # Add the user-selected cutoff to final_metrics, clearly marked, so its
    # TP/FP/TN/FN counts can be compared directly with the molecule files.
    selected_metrics = calculate_metrics(valid, user_cutoff)
    selected_row = {key: selected_metrics[key] for key in [
        "Cutoff", "TP", "FP", "TN", "FN", "TPR", "FPR", "TNR",
        "Balanced Accuracy", "Accuracy"
    ]}
    selected_row["Cutoff Type"] = "User-specified cutoff"
    export_columns = [
        "Cutoff", "TP", "FP", "TN", "FN", "TPR", "FPR", "TNR",
        "Balanced Accuracy", "Accuracy"
    ]
    metrics_df = results[export_columns].drop_duplicates().copy()
    metrics_df["Cutoff Type"] = "Search candidate"
    metrics_df = pd.concat([metrics_df, pd.DataFrame([selected_row])], ignore_index=True)
    metrics_df = metrics_df.sort_values(["Cutoff", "Cutoff Type"]).reset_index(drop=True)
    metrics_file = f"final_metrics_{os.path.splitext(file_path)[0]}.csv"
    metrics_df.to_csv(metrics_file, index=False)
    print(f"All cutoff metrics, including the user-specified cutoff, saved to {metrics_file}")

    groups = {
        "True Positives": valid.loc[actual_y & predicted_y, "Name"].astype(str).tolist(),
        "False Positives": valid.loc[actual_n & predicted_y, "Name"].astype(str).tolist(),
        "True Negatives": valid.loc[actual_n & ~predicted_y, "Name"].astype(str).tolist(),
        "False Negatives": valid.loc[actual_y & ~predicted_y, "Name"].astype(str).tolist(),
    }

    # Verify counts from the files' source lists match the confusion matrix.
    expected_counts = {"True Positives": tp, "False Positives": fp,
                       "True Negatives": tn, "False Negatives": fn}
    for category, names in groups.items():
        out_file = f"{category.replace(' ', '_')}_{os.path.splitext(file_path)[0]}.txt"
        with open(out_file, "w", encoding="utf-8") as handle:
            handle.write("\n".join(names))
        if len(names) != expected_counts[category]:
            raise RuntimeError(
                f"Count mismatch for {category}: metrics={expected_counts[category]}, "
                f"molecule list={len(names)}"
            )
        print(f"{category}: {len(names)} molecule(s); saved to {out_file}")

    print(
        f"CONSISTENCY CHECK — cutoff={user_cutoff:.4f}: "
        f"TP={tp}, FP={fp}, TN={tn}, FN={fn}; "
        f"list counts TP={len(groups['True Positives'])}, "
        f"FP={len(groups['False Positives'])}, TN={len(groups['True Negatives'])}, "
        f"FN={len(groups['False Negatives'])}"
    )
