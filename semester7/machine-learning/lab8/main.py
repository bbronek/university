from pathlib import Path


import pandas as pd


from sklearn.cluster import KMeans


from sklearn.decomposition import PCA


from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt


def main():
    df = pd.read_csv(Path(__file__).with_name("flats_for_clustering.tsv"), sep="\t")
    df = df[df["price"] > 0]
    df["building_floors"] = df["building_floors"].fillna(df["building_floors"].median())
    features = ["price", "area_m2", "rooms", "building_floors"]
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[features])
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(df_scaled)
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df_scaled)
    plt.scatter(df_pca[:, 0], df_pca[:, 1], c=df["cluster"], cmap="viridis")
    plt.title("PCA clustering and downsizing")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.show()


if __name__ == "__main__":
    main()
