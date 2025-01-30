import os
import pandas as pd
from hardness_shore_plot import plot_bar_chart
from density_plot import plot_density_chart
from analyze import load_data, calculate_statistics

# Pliki CSV
hardness_file = os.path.join('data', 'hardness_shore.csv')
density_file = os.path.join('data', 'density.csv')

# Przetwarzanie dla twardości Shore'a
df_hardness = load_data(hardness_file)
summary_hardness = calculate_statistics(df_hardness)
print(summary_hardness)
plot_bar_chart(summary_hardness)

# Przetwarzanie dla gęstości
df_density = load_data(density_file)

# **Sprawdzenie, czy 'Plate/Print' istnieje w danych**
if 'Plate/Print' in df_density.columns:
    summary_density = df_density.groupby(['Sample', 'Plate/Print'])['Value'].agg(['mean', 'std']).reset_index()
else:
    summary_density = df_density.groupby('Sample')['Value'].agg(['mean', 'std']).reset_index()

print(summary_density)
plot_density_chart(summary_density)
