import pandas as pd
from matplotlib import pyplot as plt
from hardness_shore_plot import plot_hardness_shore_chart
from density_plot import plot_density_chart
from impact_tensile_plot import plot_impact_tensile_chart
from hardness_ball_plot import plot_hardness_ball_chart
from elongation_plot import plot_elongation_chart
from elasticity_plot import plot_elasticity_chart
from tensile_plot import plot_tensile_chart
from young_plot import plot_young_chart
from contact_angle_plot import plot_contact_angle_chart
from analyze import load_data, calculate_statistics, save_summary_to_csv, calculate_elasticity
import os

# Ustawienia globalne dla czcionki
plt.rcParams.update({"font.family": "Times New Roman", "font.size": 11})

# Pliki CSV
hardness_shore_file = os.path.join("data", "hardness_shore.csv")
hardness_ball_file = os.path.join("data", "hardness.csv")
density_file = os.path.join("data", "density.csv")
impact_tensile_file = os.path.join("data", "impact_tensile.csv")
young_file = os.path.join("data", "tensile.csv")
tensile_file = os.path.join("data", "tensile.csv")
elongation_file = os.path.join("data", "tensile.csv")
elasticity_file = os.path.join("data", "hardness.csv")
contact_angle_file = os.path.join("data", "contact_angle.csv")

# Twardość Shore'a
df_hardness_shore = load_data(hardness_shore_file)
summary_hardness_shore = calculate_statistics(df_hardness_shore, "Value")
save_summary_to_csv(summary_hardness_shore, "hardness_shore_summary.csv")
plot_hardness_shore_chart(summary_hardness_shore)

# Twardość metodą kulki
df_hardness_ball = load_data(hardness_ball_file)
summary_hardness_ball = calculate_statistics(df_hardness_ball, "H")
save_summary_to_csv(summary_hardness_ball, "hardness_ball_summary.csv")
plot_hardness_ball_chart(summary_hardness_ball)

# Gęstość
df_density = load_data(density_file)
summary_density = calculate_statistics(df_density, "Value")
save_summary_to_csv(summary_density, "density_summary.csv")
plot_density_chart(summary_density)

# Rozciąganie udarowe
df_impact_tensile = load_data(impact_tensile_file)
summary_impact_tensile = calculate_statistics(df_impact_tensile, "it")
save_summary_to_csv(summary_impact_tensile, "impact_tensile_summary.csv")
plot_impact_tensile_chart(summary_impact_tensile)

# Moduł Younga
df_young = load_data(young_file)
summary_young = calculate_statistics(df_young, "E")
save_summary_to_csv(summary_young, "young_summary.csv")
plot_young_chart(summary_young)

# Wytrzymałość na rozciąganie
df_tensile = load_data(tensile_file)
summary_tensile = calculate_statistics(df_tensile, "sm")
save_summary_to_csv(summary_tensile, "tensile_summary.csv")
plot_tensile_chart(summary_tensile)

# Wydłużenie przy zerwaniu
df_elongation = load_data(elongation_file)
summary_elongation = calculate_statistics(df_elongation, "em")
save_summary_to_csv(summary_elongation, "elongation_summary.csv")
plot_elongation_chart(summary_elongation)

# Współczynnik sprężystości wzdłużnej
df_elasticity = load_data(elasticity_file)
summary_elasticity = calculate_elasticity(df_elasticity)
save_summary_to_csv(summary_elasticity, "elasticity_summary.csv")
plot_elasticity_chart(summary_elasticity)

# Kąt zwilżania metodą kulki
df_contact_angle_ball = pd.read_csv(contact_angle_file)
plot_contact_angle_chart(df_contact_angle_ball)
