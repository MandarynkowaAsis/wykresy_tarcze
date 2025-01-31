import seaborn as sns
import matplotlib.pyplot as plt


def plot_bar_chart(summary):
    plt.figure(figsize=(12, 6))

    # Wykres słupkowy z błędami, bez legendy
    ax = sns.barplot(x='Sample', y='mean', hue='Plate/Print', data=summary,
                     errorbar=None, capsize=5, palette='muted', legend=False)

    # Dodanie odchyleń standardowych
    for i in range(len(summary)):
        # Pozycja x dla każdego słupka
        x_pos = i // 2  # Dzielimy na dwie grupy dla "Plate" i "Print"

        # Przesunięcie w poziomie dla "Plate" i "Print"
        if summary['Plate/Print'].iloc[i] == 'Plate':
            offset = -0.2
        else:
            offset = 0.2

        # Pobieramy wartości dla yerr
        yerr_val = summary['std'][i]
        y_pos = summary['mean'][i]

        # Rysowanie odchyleń standardowych
        ax.errorbar(x=x_pos + offset, y=y_pos, yerr=yerr_val, fmt='none',
                    color='black', capsize=5)

    # Ustawienia osi i tytuł wykresu
    plt.xlabel('Nazwa próbki')
    plt.ylabel("Twardość Shore'a")

    # Usunięcie legendy
    plt.legend([], [], frameon=False)

    # Dodanie delikatnych linii tła co 10 jednostek
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, alpha=0.5)

    # Ustawienie zakresu na osi y, aby linie były widoczne
    ax.set_ylim(0, summary['mean'].max() + 10)

    # Eksportowanie wykresu do pliku PNG
    plt.savefig('outputs/hardness_shore.png', dpi=300, bbox_inches='tight')
