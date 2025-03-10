import seaborn as sns
import matplotlib.pyplot as plt


def plot_hardness_shore_surfaces_chart(summary):
    plt.figure(figsize=(10, 6))

    # Zamiana nazw w legendzie
    summary["Legenda"] = summary["Plate/Print"].replace(
        {"Plate": "Plate", "Print": "Free"}
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
    plt.ylabel("Twardość Shore'a [Shore D]")

    # Zmiana pozycji legendy
    plt.legend(title="Powierzchnia", loc="upper right", bbox_to_anchor=(1, 1))

    # Linie siatki
    ax.grid(True, which="both", axis="y", linestyle="--", linewidth=0.5, alpha=0.5)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary["mean"].max() + 12)

    # Eksport wykresu do pliku PNG
    plt.savefig("outputs/hardness_shore_surfaces.png", dpi=300, bbox_inches="tight")


def plot_hardness_shore_plate_surface_chart(summary):

    summary_plate = summary[summary["Plate/Print"] == "Plate"]

    plt.figure(figsize=(10, 6))

    # Wykres słupkowy dla Plate
    ax = sns.barplot(
        x="Sample",
        y="mean",
        hue="Sample",
        data=summary_plate,
        errorbar=None,
        capsize=5,
        palette="muted",
    )

    # Dodanie odchyleń standardowych
    for i in range(len(summary_plate)):
        x_pos = i  # Ustawienie pozycji na osi X
        yerr_val = summary_plate["std"].iloc[i]
        y_pos = summary_plate["mean"].iloc[i]

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
    plt.ylabel("Twardość Shore'a [Shore D]")

    # Linie siatki
    ax.grid(True, which="both", axis="y", linestyle="--", linewidth=0.5, alpha=0.5)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary_plate["mean"].max() + 12)

    # Eksport wykresu do pliku PNG
    plt.savefig("outputs/hardness_shore_plate.png", dpi=300, bbox_inches="tight")

