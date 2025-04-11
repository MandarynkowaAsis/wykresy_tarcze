import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_density_chart(summary, language):
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

    # Dodanie linii siatki
    ax.set_yticks(np.arange(0, summary["mean"].max() + 100, 200))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    if language == "pl":
        plt.xlabel("Nazwa próbki")
        plt.ylabel(r"Gęstość $\rho$ [kg/m$^3$]")
    elif language == "en":
        plt.xlabel("Sample name")
        plt.ylabel(r"Density $\rho$ [kg/m$^3$]")

    # Zapis wykresu do pliku PNG
    plt.savefig("outputs/density.png", dpi=300, bbox_inches="tight")
