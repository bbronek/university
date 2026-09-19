from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data(path=Path(__file__).with_name("avocado_data.csv")):
    data = pd.read_csv(path).dropna()
    features = data.drop(columns=["Date", "type", "region", "AveragePrice"])
    encoder = LabelEncoder()
    labels = encoder.fit_transform(data["type"])
    train, test, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.2, random_state=42, stratify=labels
    )
    scaler = StandardScaler()
    return (
        scaler.fit_transform(train),
        scaler.transform(test),
        train_labels,
        test_labels,
        encoder.classes_,
    )
