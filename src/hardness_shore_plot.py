import seaborn as sns
import matplotlib.pyplot as plt


def plot_bar_chart(summary):
    plt.figure(figsize=(12, 7))

    # Zamiana nazw w kolumnie "Plate/Print" dla czytelniejszej legendy
    summary['Legenda'] = summary['Plate/Print'].replace({'Plate': 'Plate surface', 'Print': 'Free surface'})

    # Wykres słupkowy z błędami
    ax = sns.barplot(x='Sample', y='mean', hue='Legenda', data=summary,
                     errorbar=None, capsize=5, palette='muted')

    # Dodanie odchyleń standardowych
    for i in range(len(summary)):
        x_pos = i // 2  # Dzielimy na dwie grupy dla "Plate" i "Print"

        # Przesunięcie w poziomie dla "Plate Surface" i "Free Surface"
        offset = -0.2 if summary['Plate/Print'].iloc[i] == 'Plate' else 0.2

        yerr_val = summary['std'][i]
        y_pos = summary['mean'][i]

        # Rysowanie odchyleń standardowych
        ax.errorbar(x=x_pos + offset, y=y_pos, yerr=yerr_val, fmt='none',
                    color='black', capsize=5)

    # Ustawienia osi
    plt.xlabel('Nazwa próbki')
    plt.ylabel("Twardość Shore'a")

    # Dodanie legendy trochę wyżej
    plt.legend(title="Legenda", loc="upper right", bbox_to_anchor=(1, 1))

    # Linie siatki co 10 jednostek
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, alpha=0.5)

    # Ustawienie zakresu na osi y
    ax.set_ylim(0, summary['mean'].max() + 10)

    # Eksport wykresu do pliku PNG
    plt.savefig('outputs/hardness_shore.png', dpi=300, bbox_inches='tight')
