import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

def load_and_initial_clean(file_path):
    data = pd.read_csv(file_path, compression='gzip')
    data.dropna(axis=1, how='all', inplace=True)
    return data

def thorough_clean(data):
    data['price'] = pd.to_numeric(data['price'].str.replace("[$,]", ""), errors='coerce')
    data.dropna(subset=['price'], inplace=True)
    for col in data.select_dtypes(include=np.number).columns:
        data[col].fillna(data[col].median(), inplace=True)
    for col in data.select_dtypes(include='object').columns:
        data[col].fillna(data[col].mode()[0], inplace=True)
    data['z_score'] = np.abs(zscore(data['price']))
    data = data[data['z_score'] < 3]
    data.drop(columns=['z_score'], inplace=True)
    return data

def eda(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['price'], bins=30, kde=True)
    plt.title('Distribution of Listing Prices')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(data['availability_365'], kde=True, color='green')
    plt.title('Availability Distribution')
    plt.show()

def advanced_visualization(data):
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='room_type', y='price', data=data)
    plt.title('Price Distribution by Room Type')
    plt.xticks(rotation=45)
    plt.show()

def statistical_analysis(data):
    plt.figure(figsize=(12, 8))""

    sns.heatmap(data.corr(), annot=True, fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

file_path = 'listings.csv.gz'

raw_data = load_and_initial_clean(file_path)
clean_data = thorough_clean(raw_data)
eda(clean_data)
advanced_visualization(clean_data)
statistical_analysis(clean_data)

