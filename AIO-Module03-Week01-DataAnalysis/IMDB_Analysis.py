import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_path = 'AIO-Homework/AIO-Module03-Week01-DataAnalysis/Dataset/IMDB-Movie-Data.csv'
data = pd.read_csv(dataset_path)

data_indexed = pd.read_csv(dataset_path, index_col='Title')
# print(data.head())
# print(data_indexed.head())

# Some basic info about data
# print(data.info())
# print(data.describe())

# Tách cột thành series
# genre = data['Genre']
# print(genre)

# Tách cột thành DataFrame
# print(data[['Genre']])

# Slicing
print(data.iloc[10:20][['Title', 'Rating', 'Metascore']])

# Filtering
print(data[((data['Year'] >= 2010) & (data['Year'] <= 2015)) & (data['Rating'] < 6.0) & (
    data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))])

# Groupby
print(data.groupby('Director')[['Rating']].mean().head())
# Sorting
print(data.groupby('Director')[['Rating']].mean(
).sort_values(['Rating'], ascending=False).head())

# Missing values
print(data.isnull().sum())

# Drop function
print(data.drop('Metascore', axis=1).head())
# Can use dropna for column

# Missing values - Filling
revenue_mean = data['Revenue (Millions)'].mean()
print("The mean revenue is: ", revenue_mean)

data['Revenue (Millions)'].fillna(revenue_mean, inplace=True)

# Classify movies based on rating use apply function
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'
    
data['Rating_Category'] = data['Rating'].apply(rating_group)
print(data[['Title', 'Director', 'Rating', 'Rating_Category']].head(10))