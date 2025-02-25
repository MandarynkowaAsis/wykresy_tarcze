import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import analyze


def plot_tensile_temp_chart(summary, column_name):
    plt.figure(figsize=(12, 7))

    # Mapowanie nazw kolumn na etykiety osi Y
    y_labels = {
        "E": r"Moduł Younga dla różnych temperatur ($E$) [MPa]",
        "sm": r"Wytrzymałość na rozciąganie dla różnych temperatur ($\sigma_m$) [MPa]",
        "em": r"Wydłużenie przy zerwaniu dla różnych temperatur ($\varepsilon_m$) [%]",
    }
    y_label = y_labels.get(column_name, column_name)  # Domyślnie używa nazwy kolumny

    # Zamiana nazw w legendzie dla różnych temperatur
    summary["Legenda"] = (
        summary["Temp"].astype(str).replace({"-7": "-7°C", "23": "23°C", "35": "35°C"})
    )

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

    # Pobranie unikalnych próbek i temperatur
    unique_samples = summary["Sample"].unique()
    temp_offsets = {-7: -0.265, 23: 0, 35: 0.265}  # Przesunięcia dla różnych temperatur

    # Mapa indeksów dla pozycji słupków
    sample_positions = {sample: i for i, sample in enumerate(unique_samples)}

    # Dodanie odchyleń standardowych
    for i in range(len(summary)):
        sample = summary["Sample"].iloc[i]
        temp = summary["Temp"].iloc[i]
        x_pos = sample_positions[sample] + temp_offsets[temp]  # Ustawienie pozycji
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

    # Ustawienia osi
    plt.xlabel("Nazwa próbki")
    plt.ylabel(y_label)  # Dynamiczny opis osi Y

    # Zmiana pozycji legendy
    plt.legend(title="Temperatura", loc="upper right", bbox_to_anchor=(1, 1))

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

    # Eksport wykresu do pliku PNG
    plt.savefig(f"outputs/tensile_temp_{column_name}.png", dpi=300, bbox_inches="tight")
