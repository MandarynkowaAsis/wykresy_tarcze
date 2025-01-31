import os
import numpy as np
import pandas as pd


def load_data(file_path):
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


def calculate_elasticity(df):
    # Przeliczanie h i h0 z mm na metry
    df["h"] = df["h"] / 1000  # h w metrach
    df["h0"] = df["h0"] / 1000  # h0 w metrach

    df["E2"] = (
        13.65 * (df["P"] - 9.81) / ((df["h"] - df["h0"]) * np.sqrt(df["h"] - df["h0"]))
    )
    df["E2"] = df["E2"] / 1000000  # Przekształcenie z Pa na MPa

    # Grupowanie po "Sample" i "Plate/Print", jeśli kolumna "Plate/Print" istnieje
    if "Plate/Print" in df.columns:
        summary = (
            df.groupby(["Sample", "Plate/Print"])["E2"]
            .agg(["mean", "std"])
            .reset_index()
        )
    else:
        summary = df.groupby("Sample")["E2"].agg(["mean", "std"]).reset_index()

    return summary


def save_summary_to_csv(summary, file_name):
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    summary.to_csv(
        os.path.join(output_dir, file_name), index=False, float_format="%.4f"
    )
