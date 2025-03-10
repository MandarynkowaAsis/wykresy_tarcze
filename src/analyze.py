import os
import numpy as np
import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def calculate_statistics(df, column_name):
    if "Plate/Print" in df.columns and "Temp" in df.columns:
        summary = (
            df.groupby(["Sample", "Plate/Print", "Temp"])[column_name]
            .agg(["mean", "std"])
            .reset_index()
        )
    elif "Plate/Print" in df.columns:
        summary = (
            df.groupby(["Sample", "Plate/Print"])[column_name]
            .agg(["mean", "std"])
            .reset_index()
        )
    elif "Temp" in df.columns:
        summary = (
            df.groupby(["Sample", "Temp"])[column_name]
            .agg(["mean", "std"])
            .reset_index()
        )
    elif "Thick" in df.columns:
        summary = (
            df.groupby(["Sample", "Thick"])[column_name]
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


def nice_tick_step(max_value):
    if max_value == 0:
        return 1
    elif max_value < 1:
        return 0.2
    elif max_value < 5:
        return 1
    elif max_value < 10:
        return 2
    elif max_value < 50:
        return 10
    elif max_value < 100:
        return 20
    elif max_value < 500:
        return 100
    elif max_value < 1000:
        return 200
    elif max_value < 5000:
        return 500
    elif max_value < 20000:
        return 2000
    else:
        return round(max_value * 0.2, -2)
