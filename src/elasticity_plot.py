import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np


def plot_elasticity_chart(summary):
    """Tworzy wykres słupkowy dla wartości E2 ze średnią i odchyleniem standardowym."""

    plt.figure(figsize=(12, 7))

    # Zamiana nazw w legendzie
    summary["Legenda"] = summary["Plate/Print"].replace(
        {"Plate": "Plate surface", "Print": "Free surface"}
    )

    # Wykres słupkowy
    ax = sns.barplot(
        x="Sample",
        y="mean",
        hue="Legenda",
        data=summary,
        errorbar=None,
        capsize=5,
        palette="muted",
    )

    # Dodanie odchyleń standardowych
    for i in range(len(summary)):
        x_pos = i // 2  # Dzielimy na dwie grupy dla "Plate" i "Print"

        # Przesunięcie w poziomie dla "Plate Surface" i "Free Surface"
        offset = -0.2 if summary["Plate/Print"].iloc[i] == "Plate" else 0.2

        yerr_val = summary["std"][i]
        y_pos = summary["mean"][i]

        # Rysowanie odchyleń standardowych
        ax.errorbar(
            x=x_pos + offset,
            y=y_pos,
            yerr=yerr_val,
            fmt="none",
            color="black",
            capsize=5,
        )

    # Ustawienia osi
    plt.xlabel("Nazwa próbki")
    plt.ylabel("Współczynnik sprężystości wzdłużnej (E) [MPa]")

    # Zmiana pozycji legendy
    plt.legend(title="Legenda", loc="upper right", bbox_to_anchor=(0.2, 1))

    # Dodanie linii siatki
    ax.set_yticks(np.arange(0, summary["mean"].max() + 1000, 500))
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary["mean"].max() + 1100)

    # Eksport wykresu do pliku PNG
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, "elasticity.png"), dpi=300, bbox_inches="tight")
