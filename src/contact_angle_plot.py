import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_contact_angle_chart(summary):
    plt.figure(figsize=(10, 6))

    # Zamiana nazw w legendzie
    summary["Legenda"] = summary["Plate/Print"].replace(
        {"Plate": "Plate surface", "Print": "Free surface"}
    )

    # Wykres słupkowy
    ax = sns.barplot(
        x="Sample",
        y="Mean_CA",  # Średnia wartość kąta zwilżania
        hue="Legenda",
        data=summary,
        errorbar=None,
        capsize=5,
        palette="muted",
    )

    # Dodanie odchyleń standardowych
    for i in range(len(summary)):
        # Uzyskiwanie pozycji słupków
        x_pos = (
            summary["Sample"].unique().tolist().index(summary["Sample"].iloc[i])
        )  # Indeks próbki
        hue_offset = (
            -0.2 if summary["Plate/Print"].iloc[i] == "Plate" else 0.2
        )  # Przesunięcie w poziomie dla "Plate" i "Print"

        yerr_val = summary["Std_CA"].iloc[i]  # Odchylenie standardowe
        y_pos = summary["Mean_CA"].iloc[i]  # Średnia wartość kąta zwilżania

        # Rysowanie odchyleń standardowych
        ax.errorbar(
            x=x_pos + hue_offset,
            y=y_pos,
            yerr=yerr_val,
            fmt="none",
            color="black",
            capsize=5,
        )

    # Ustawienia osi
    plt.xlabel("Nazwa próbki")
    plt.ylabel("Kąt zwilżania [°]")  # Zmieniamy jednostki na stopnie

    # Zmiana pozycji legendy
    plt.legend(title="Powierzchnia", loc="upper right", bbox_to_anchor=(1, 1))

    # Linie siatki
    ax.grid(True, which="both", axis="y", linestyle="--", linewidth=0.5, alpha=0.5)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary["Mean_CA"].max() + 10)

    # Eksport wykresu do pliku PNG
    plt.savefig("outputs/contact_angle.png", dpi=300, bbox_inches="tight")
