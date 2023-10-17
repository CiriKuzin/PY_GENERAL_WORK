
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('spotify-2023_fixed.csv')

# Задание 1
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='released_year', y='streams')
plt.title('Количество потоков в зависимости от года выпуска песни')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df, x='bpm', y='streams', estimator=sum)
plt.title('Среднее количество потоков в зависимости от темпа песни')
plt.show()

# Задание 2
print('Уникальных значений в столбце "track_name":', len(df['track_name'].unique()))
print('Уникальных значений в столбце "artist(s)name":', len(df['artist(s)_name'].unique()))

# Задание 3
def categorize_bpm(bpm):
    if bpm < 100:
        return 'slow'
    elif bpm >= 100 and bpm <= 140:
        return 'medium'
    else:
        return 'fast'

df['bpm_category'] = df['bpm'].apply(categorize_bpm)

def categorize_valence(valence):
    if valence < 50:
        return 'negative'
    else:
        return 'positive'

df['valence_category'] = df['valence_%'].apply(categorize_valence)

# Задание 4
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='released_year', y='streams', hue='valence_category')
plt.title('Количество потоков в зависимости от года выпуска песни и контента')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df, x='bpm_category', y='streams', hue='valence_category', estimator=sum)
plt.title('Среднее количество потоков в зависимости от темпа песни и контента')
plt.show()

# Задание 5
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='in_spotify_playlists', y='in_apple_playlists', size='streams', sizes=(20, 500))
plt.title('Количество потоков в зависимости от количества плейлистов на Spotify и Apple Music')
plt.show()