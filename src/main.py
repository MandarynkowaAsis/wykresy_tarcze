from hardness_shore_plot import plot_bar_chart
from density_plot import plot_density_chart
from analyze import load_data, calculate_statistics
import os

from src.impact_tensile_plot import plot_impact_tensile


def save_summary_to_csv(summary, file_name):
    output_dir = 'outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Zapis do CSV z 4 miejscami po przecinku
    summary.to_csv(os.path.join(output_dir, file_name), index=False, float_format='%.4f')


# Pliki CSV
hardness_shore_file = os.path.join('data', 'hardness_shore.csv')
density_file = os.path.join('data', 'density.csv')
impact_tensile_file = os.path.join('data', 'impact_tensile.csv')

# Przetwarzanie dla twardości Shore'a
df_hardness_shore = load_data(hardness_shore_file)
summary_hardness_shore = calculate_statistics(df_hardness_shore)
save_summary_to_csv(summary_hardness_shore, 'hardness_shore_summary.csv')
plot_bar_chart(summary_hardness_shore)

# Przetwarzanie dla gęstości
df_density = load_data(density_file)

# **Sprawdzenie, czy 'Plate/Print' istnieje w danych**
if 'Plate/Print' in df_density.columns:
    summary_density = df_density.groupby(['Sample', 'Plate/Print'])['Value'].agg(['mean', 'std']).reset_index()
else:
    summary_density = df_density.groupby('Sample')['Value'].agg(['mean', 'std']).reset_index()
save_summary_to_csv(summary_density, 'density_summary.csv')
plot_density_chart(summary_density)

# **Przetwarzanie dla Impact Tensile**
df_impact_tensile = load_data(impact_tensile_file)
summary_impact_tensile = df_impact_tensile.groupby('Sample')['it'].agg(['mean', 'std']).reset_index()
save_summary_to_csv(summary_impact_tensile, 'impact_tensile_summary.csv')
plot_impact_tensile(summary_impact_tensile)  # Rysowanie wykresu dla Impact Tensile