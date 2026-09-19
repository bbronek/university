import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder


def prepare_data(data):
    required = {"HouseType", "Size", "Balcony", "Locality"}
    if not required <= set(data.columns):
        raise ValueError(f"Missing columns: {sorted(required - set(data.columns))}")
    data = data.dropna(subset=["HouseType"])
    features = data.drop(columns="HouseType").copy()
    unknown_sizes = set(features["Size"].dropna()) - {"S", "M", "L"}
    if unknown_sizes:
        raise ValueError(f"Unknown size categories: {sorted(unknown_sizes)}")
    features["Size"] = features["Size"].map({"S": 0, "M": 1, "L": 2})
    labels = LabelEncoder().fit_transform(data["HouseType"])
    train, test, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.2, random_state=42, stratify=labels
    )
    numeric = train.select_dtypes(include="number").columns
    categorical = train.columns.difference(numeric)
    preprocessor = ColumnTransformer(
        [
            (
                "numeric",
                Pipeline(
                    [
                        (
                            "imputer",
                            SimpleImputer(strategy="mean", keep_empty_features=True),
                        ),
                        ("scaler", MinMaxScaler()),
                    ]
                ),
                numeric,
            ),
            (
                "categorical",
                Pipeline(
                    [
                        (
                            "imputer",
                            SimpleImputer(
                                strategy="most_frequent", keep_empty_features=True
                            ),
                        ),
                        (
                            "encoder",
                            OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                        ),
                    ]
                ),
                categorical,
            ),
        ]
    )
    return (
        preprocessor.fit_transform(train),
        preprocessor.transform(test),
        train_labels,
        test_labels,
    )


def evaluate(name, expected, predicted):
    precision, recall, f1, _ = precision_recall_fscore_support(
        expected, predicted, average="weighted", zero_division=0
    )
    print(f"\n{name}")
    print(f"Accuracy: {accuracy_score(expected, predicted):.4f}")
    print(f"Precision: {precision:.4f}\nRecall: {recall:.4f}\nF1 score: {f1:.4f}")


def main():
    parser = argparse.ArgumentParser(description="Compare Swiss house-type classifiers")
    parser.add_argument(
        "dataset",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("house_prices_switzerland.csv"),
    )
    parser.add_argument("--skip-neural-network", action="store_true")
    arguments = parser.parse_args()
    if not arguments.dataset.is_file():
        parser.error(
            f"Dataset not found: {arguments.dataset}. See README.md for the dataset source."
        )
    data = pd.read_csv(arguments.dataset)
    print("Missing values:")
    print(data.isna().sum())
    train, test, train_labels, test_labels = prepare_data(data)
    models = {
        "Logistic regression with L2 regularization": LogisticRegression(
            max_iter=10000
        ),
        "Logistic regression without regularization": LogisticRegression(
            penalty=None, max_iter=10000
        ),
        "Gaussian naive Bayes": GaussianNB(),
    }
    for name, model in models.items():
        model.fit(train, train_labels)
        evaluate(name, test_labels, model.predict(test))
    if not arguments.skip_neural_network:
        from tensorflow import keras

        keras.utils.set_random_seed(42)
        model = keras.Sequential(
            [
                keras.Input(shape=(train.shape[1],)),
                keras.layers.Dense(32, activation="relu"),
                keras.layers.Dense(len(np.unique(train_labels)), activation="softmax"),
            ]
        )
        model.compile(
            loss="sparse_categorical_crossentropy",
            optimizer="adam",
            metrics=["accuracy"],
        )
        model.fit(train, train_labels, epochs=50, batch_size=32, validation_split=0.1)
        evaluate("Neural network", test_labels, model.predict(test).argmax(axis=1))


if __name__ == "__main__":
    main()
