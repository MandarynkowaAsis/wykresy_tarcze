import os
import pandas as pd


def load_data(file_path):
    # Załaduj dane z pliku CSV
    df = pd.read_csv(file_path)
    return df


def calculate_statistics(df, column_name):
    if "Plate/Print" in df.columns:
        summary = (
            df.groupby(["Sample", "Plate/Print"])[column_name]
            .agg(["mean", "std"])
            .reset_index()
        )
    else:
        summary = df.groupby("Sample")[column_name].agg(["mean", "std"]).reset_index()
    return summary


def save_summary_to_csv(summary, file_name):
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Zapis do CSV z 4 miejscami po przecinku
    summary.to_csv(
        os.path.join(output_dir, file_name), index=False, float_format="%.4f"
    )
