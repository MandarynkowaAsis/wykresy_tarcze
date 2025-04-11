import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import analyze


def plot_tensile_chart(summary, column_name, language):
    plt.figure(figsize=(10, 6))

    # Zamiana nazw w legendzie dla różnych temperatur
    summary["Legenda"] = summary["Thick"].map({2: "2 mm", 4: "4 mm"})

    # Wykres słupkowy
    ax = sns.barplot(
        x="Sample",
        y="mean",
        hue="Legenda",
        data=summary,
        errorbar=None,
        capsize=0.1,
        palette="muted",
    )

    # Pobranie unikalnych próbek i grubości
    unique_samples = summary["Sample"].unique()
    thick_offsets = {2: -0.2, 4: 0.2}

    # Mapa indeksów dla pozycji słupków
    sample_positions = {sample: i for i, sample in enumerate(unique_samples)}

    # Dodanie odchyleń standardowych
    for i in range(len(summary)):
        sample = summary["Sample"].iloc[i]
        thick = summary["Thick"].iloc[i]
        x_pos = sample_positions[sample] + thick_offsets[thick]  # Ustawienie pozycji
        y_pos = summary["mean"].iloc[i]
        yerr_val = summary["std"].iloc[i]

        # Rysowanie odchyleń standardowych
        ax.errorbar(
            x=x_pos,
            y=y_pos,
            yerr=yerr_val,
            fmt="none",
            color="black",
            capsize=5,
        )

    if language == "pl":
        # Mapowanie nazw kolumn na etykiety osi Y
        y_labels = {
            "E": r"Moduł Younga ($E$) [MPa]",
            "sm": r"Wytrzymałość na rozciąganie ($\sigma_m$) [MPa]",
            "em": r"Wydłużenie przy zerwaniu ($\varepsilon_m$) [%]",
        }
        y_label = y_labels.get(column_name, column_name)  # Jeśli brak, użyj nazwy kolumny

        # Ustawienia osi
        plt.xlabel("Nazwa próbki")
        plt.ylabel(y_label)  # Dynamiczny opis osi Y

        # Zmiana pozycji legendy
        plt.legend(title="Grubość próbki", loc="upper right", bbox_to_anchor=(1, 1))

    elif language == "en":
        y_labels = {
            "E": r"Young's modulus ($E$) [MPa]",
            "sm": r"Tensile strength ($\sigma_m$) [MPa]",
            "em": r"Elongation at break ($\varepsilon_m$) [%]",
        }

        y_label = y_labels.get(column_name, column_name)

        plt.xlabel("Sample name")
        plt.ylabel(y_label)  # Dynamic Y-axis label

        plt.legend(title="Sample thickness", loc="upper right", bbox_to_anchor=(1, 1))


    # Linie siatki
    max_value = summary["mean"].max()
    ax.set_yticks(
        np.arange(
            0,
            summary["mean"].max() + summary["mean"].max() * 0.1,
            analyze.nice_tick_step(max_value),
        )
    )
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary["mean"].max() * 1.1)

    # Zapis wykresu do pliku PNG
    plt.savefig(f"outputs/tensile_{column_name}.png", dpi=300, bbox_inches="tight")
