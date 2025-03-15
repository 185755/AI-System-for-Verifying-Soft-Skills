import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dane
data = {
    'Model': ['4o', '3.5turbo', 'o1mini', '4omini', 'Qwen', 'MistralAI', 'Llama 70B', 'Llama 3B', 'HuggingF'],
    'Precision': [0.6202, 0.53665, 0.59983, 0.55254, 0.63787, 0.61851, 0.6297, 0.62428, 0.60621],
    'Recall': [0.95949, 0.99691, 0.91904, 0.99588, 0.86108, 0.89391, 0.99306, 0.47635, 0.59072],
    'F1-Score': [0.70756, 0.65538, 0.69716, 0.67686, 0.70282, 0.70235, 0.7445, 0.45872, 0.56639],
    'Accuracy': [0.64298, 0.54051, 0.64666, 0.56157, 0.62209, 0.59264, 0.63501, 0.44921, 0.53973],
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Funkcja do rysowania wykresu w osobnym oknie
def plot_single_metric_sorted(df, metric, title, color):
    # Sortowanie danych według podanej metryki
    df_sorted = df.sort_values(by=metric, ascending=False)
    x_sorted = np.arange(len(df_sorted['Model']))
    
    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.bar(x_sorted, df_sorted[metric], color=color, width=0.5, label=metric)
    plt.xlabel('Model', fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.title(title, fontsize=14)
    plt.xticks(x_sorted, df_sorted['Model'], rotation=45)
    plt.ylim(0, 1.0)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Wykres 1: Oryginalne dane (wszystkie metryki)
def plot_all_metrics(df, title):
    x = np.arange(len(df['Model']))
    width = 0.2

    plt.figure(figsize=(10, 6))
    plt.bar(x - 1.5*width, df['Precision'], width, label='Precision', color='blue')
    plt.bar(x - 0.5*width, df['Recall'], width, label='Recall', color='orange')
    plt.bar(x + 0.5*width, df['F1-Score'], width, label='F1-Score', color='gray')
    plt.bar(x + 1.5*width, df['Accuracy'], width, label='Accuracy', color='yellow')

    plt.xlabel('Model', fontsize=12)
    plt.ylabel('Wartość', fontsize=12)
    plt.title(title, fontsize=14)
    plt.xticks(x, df['Model'], rotation=45)
    plt.ylim(0, 1.0)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Wykresy
plot_all_metrics(df, 'Porównanie Modeli')
plot_single_metric_sorted(df, 'Accuracy', 'Modele Posortowane według Accuracy', 'yellow')
plot_single_metric_sorted(df, 'Precision', 'Modele Posortowane według Precision', 'blue')
plot_single_metric_sorted(df, 'Recall', 'Modele Posortowane według Recall', 'orange')
plot_single_metric_sorted(df, 'F1-Score', 'Modele Posortowane według F1-Score', 'gray')
