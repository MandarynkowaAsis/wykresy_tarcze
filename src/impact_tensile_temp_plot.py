import seaborn as sns
import matplotlib.pyplot as plt


def plot_impact_tensile_temp_chart(summary):
    plt.figure(figsize=(10, 6))

    # Zamiana nazw w legendzie
    summary["Legenda"] = (
        summary["Temp"].astype(str).replace({"-7": "-7°C", "23": "23°C"})
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
        x_pos = i // 2  # Dzielimy na dwie grupy dla dwóch temperatur

        # Przesunięcie w poziomie dla temperatur
        offset = -0.2 if summary["Temp"].iloc[i] == -7 else 0.2

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
    plt.ylabel(
        r"Rozciąganie udarowe w różnych temperaturach ($\sigma_{i}^{t}$) [kJ/m$^2$]"
    )

    # Zmiana pozycji legendy
    plt.legend(title="Temperatura", loc="upper right", bbox_to_anchor=(1, 1))

    # Linie siatki
    ax.grid(True, which="both", axis="y", linestyle="--", linewidth=0.5, alpha=0.5)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary["mean"].max() + 10)

    # Zapis wykresu do pliku PNG
    plt.savefig("outputs/impact_tensile_temp.png", dpi=300, bbox_inches="tight")
