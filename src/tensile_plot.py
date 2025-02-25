import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import analyze


def plot_tensile_chart(summary, column_name):
    plt.figure(figsize=(10, 6))

    # Mapowanie nazw kolumn na etykiety osi Y
    y_labels = {
        "E": r"Moduł Younga ($E$) [MPa]",
        "sm": r"Wytrzymałość na rozciąganie ($\sigma_m$) [MPa]",
        "em": r"Wydłużenie przy zerwaniu ($\varepsilon_m$) [%]",
    }
    y_label = y_labels.get(column_name, column_name)  # Jeśli brak, użyj nazwy kolumny

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
    max_value = summary["mean"].max()
    ax.set_yticks(
        np.arange(
            0,
            summary["mean"].max() + summary["mean"].max() * 0.1,
            analyze.nice_tick_step(max_value),
        )
    )
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.xlabel("Nazwa próbki")
    plt.ylabel(y_label)  # Dynamiczny opis osi Y

    # Zapis wykresu do pliku PNG
    plt.savefig(f"outputs/tensile_{column_name}.png", dpi=300, bbox_inches="tight")
