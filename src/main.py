import argparse
import pandas as pd
from matplotlib import pyplot as plt
from hardness_shore_plot import plot_hardness_shore_surfaces_chart, plot_hardness_shore_plate_surface_chart
from density_plot import plot_density_chart
from impact_tensile_plot import plot_impact_tensile_chart
from hardness_ball_plot import plot_hardness_ball_surfaces_chart, plot_hardness_ball_plate_surface_chart
from elasticity_plot import plot_elasticity_chart
from impact_tensile_temp_plot import plot_impact_tensile_temp_chart
from tensile_temp_plot import plot_tensile_temp_chart
from tensile_plot import plot_tensile_chart
from contact_angle_plot import plot_contact_angle_chart
from analyze import (
    load_data,
    calculate_statistics,
    save_summary_to_csv,
    calculate_elasticity,
)
import os

# Przyjęcie argumentów z konsoli
parser = argparse.ArgumentParser(description="Wybierz język wykresu!")
parser.add_argument("--language", type=str, choices=["pl", "en"], default="pl", help="Wybierz język: 'pl' lub 'en'")
args = parser.parse_args()

language_selection = args

# Ustawienia globalne dla czcionki
plt.rcParams.update({"font.family": "Times New Roman", "font.size": 11})

# Pliki CSV
hardness_shore_file = os.path.join("data", "hardness_shore.csv")
hardness_ball_file = os.path.join("data", "hardness.csv")
density_file = os.path.join("data", "density.csv")
impact_tensile_file = os.path.join("data", "impact_tensile.csv")
impact_tensile_temp_file = os.path.join("data", "impact_tensile_temp.csv")
young_file = os.path.join("data", "tensile.csv")
tensile_file = os.path.join("data", "tensile.csv")
elongation_file = os.path.join("data", "tensile.csv")
elasticity_file = os.path.join("data", "hardness.csv")
contact_angle_file = os.path.join("data", "contact_angle.csv")
tensile_temp_file = os.path.join("data", "tensile_temp.csv")


# Twardość Shore'a
df_hardness_shore = load_data(hardness_shore_file)
summary_hardness_shore = calculate_statistics(df_hardness_shore, "Value")
save_summary_to_csv(summary_hardness_shore, "hardness_shore_summary.csv")
plot_hardness_shore_surfaces_chart(summary_hardness_shore, language_selection.language)
plot_hardness_shore_plate_surface_chart(summary_hardness_shore, language_selection.language)


# Twardość metodą kulki
df_hardness_ball = load_data(hardness_ball_file)
summary_hardness_ball = calculate_statistics(df_hardness_ball, "H")
save_summary_to_csv(summary_hardness_ball, "hardness_ball_summary.csv")
plot_hardness_ball_surfaces_chart(summary_hardness_ball, language_selection.language)
plot_hardness_ball_plate_surface_chart(summary_hardness_ball, language_selection.language)

# Gęstość
df_density = load_data(density_file)
summary_density = calculate_statistics(df_density, "Value")
save_summary_to_csv(summary_density, "density_summary.csv")
plot_density_chart(summary_density, language_selection.language)

# Rozciąganie udarowe
df_impact_tensile = load_data(impact_tensile_file)
summary_impact_tensile = calculate_statistics(df_impact_tensile, "it")
save_summary_to_csv(summary_impact_tensile, "impact_tensile_summary.csv")
plot_impact_tensile_chart(summary_impact_tensile, language_selection.language)

# Rozciąganie udarowe w różnych temperaturach
df_impact_tensile_temp = load_data(impact_tensile_temp_file)
summary_impact_tensile_temp = calculate_statistics(df_impact_tensile_temp, "it")
save_summary_to_csv(summary_impact_tensile_temp, "impact_tensile_frost_summary.csv")
plot_impact_tensile_temp_chart(summary_impact_tensile_temp, language_selection.language)

# Moduł Younga
df_young = load_data(young_file)
summary_young = calculate_statistics(df_young, "E")
save_summary_to_csv(summary_young, "tensile_E_summary.csv")
plot_tensile_chart(summary_young, "E", language_selection.language)

# Moduł Younga w różnych temperaturach
df_tensile_temp = load_data(tensile_temp_file)
summary_tensile_temp = calculate_statistics(df_tensile_temp, "E")
save_summary_to_csv(summary_tensile_temp, "tensile_temp_E_summary.csv")
plot_tensile_temp_chart(summary_tensile_temp, "E", language_selection.language)

# Wytrzymałość na rozciąganie
df_tensile = load_data(tensile_file)
summary_tensile = calculate_statistics(df_tensile, "sm")
save_summary_to_csv(summary_tensile, "tensile_sm_summary.csv")
plot_tensile_chart(summary_tensile, "sm", language_selection.language)

# Wytrzymałość na rozciąganie w różnych temperaturach
df_tensile_temp = load_data(tensile_temp_file)
summary_tensile_temp = calculate_statistics(df_tensile_temp, "sm")
save_summary_to_csv(summary_tensile_temp, "tensile_temp_sm_summary.csv")
plot_tensile_temp_chart(summary_tensile_temp, "sm", language_selection.language)

# Wydłużenie przy zerwaniu
df_elongation = load_data(elongation_file)
summary_elongation = calculate_statistics(df_elongation, "em")
save_summary_to_csv(summary_elongation, "tensile_em_summary.csv")
plot_tensile_chart(summary_elongation, "em", language_selection.language)

# Wydłużenie przy zerwaniu w różnych temperaturach
df_tensile_temp = load_data(tensile_temp_file)
summary_tensile_temp = calculate_statistics(df_tensile_temp, "em")
save_summary_to_csv(summary_tensile_temp, "tensile_temp_em_summary.csv")
plot_tensile_temp_chart(summary_tensile_temp, "em", language_selection.language)

# Współczynnik sprężystości wzdłużnej
df_elasticity = load_data(elasticity_file)
summary_elasticity = calculate_elasticity(df_elasticity)
save_summary_to_csv(summary_elasticity, "elasticity_summary.csv")
plot_elasticity_chart(summary_elasticity, language_selection.language)

# Kąt zwilżania
df_contact_angle = pd.read_csv(contact_angle_file)
plot_contact_angle_chart(df_contact_angle, language_selection.language)