import pandas as pd

def load_data(file_path):
    # Załaduj dane z pliku CSV
    df = pd.read_csv(file_path)
    return df

def calculate_statistics(df):
    # Grupowanie danych i obliczanie średnich i odchyleń standardowych
    summary = df.groupby(['Sample', 'Plate/Print'])['Value'].agg(['mean', 'std']).reset_index()
    return summary
