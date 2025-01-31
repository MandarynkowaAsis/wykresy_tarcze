import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np


def plot_elongation_chart(summary):
    plt.figure(figsize=(10, 6))

    # Tworzenie wykresu słupkowego
    ax = sns.barplot(
        x="Sample",
        y="mean",
        data=summary,
        errorbar=None,
        palette="muted",
        hue="Sample",
        legend=False,
    )

    # Dodanie odchyleń standardowych
    for i, row in summary.iterrows():
        plt.errorbar(
            x=i, y=row["mean"], yerr=row["std"], fmt="none", color="black", capsize=5
        )

    # Ustawienie siatki
    ax.set_yticks(np.arange(0, summary["mean"].max() + 1, 1))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.xlabel("Nazwa próbki")
    plt.ylabel(r"Wydłużenie przy zerwaniu ($\epsilon_m$) [%]")

    # Ścieżka do folderu output
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)  # Tworzy folder, jeśli nie istnieje

    # Zapis wykresu do pliku PNG
    plt.savefig(
        os.path.join(output_folder, "elongation.png"), dpi=300, bbox_inches="tight"
    )
