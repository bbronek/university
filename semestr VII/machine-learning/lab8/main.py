import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('flats_for_clustering.tsv', sep='\t')
df = df[df['cena'] > 0]
df['Liczba pięter w budynku'].fillna(df['Liczba pięter w budynku'].median(), inplace=True)

features = ['cena', 'Powierzchnia w m2', 'Liczba pokoi', 'Liczba pięter w budynku']

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(df_scaled)

pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

plt.scatter(df_pca[:, 0], df_pca[:, 1], c=df['cluster'], cmap='viridis')
plt.title('PCA clustering and downsizing')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()
