from data import load_data
from sklearn.metrics import accuracy_score


def main():
    from tensorflow import keras

    keras.utils.set_random_seed(42)
    train, test, train_labels, test_labels, classes = load_data()
    model = keras.Sequential(
        [
            keras.Input(shape=(train.shape[1],)),
            keras.layers.Dense(64, activation="relu"),
            keras.layers.Dense(len(classes), activation="softmax"),
        ]
    )
    model.compile(
        loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )
    model.fit(train, train_labels, batch_size=64, epochs=10, validation_split=0.1)
    predicted = model.predict(test).argmax(axis=1)
    print(f"Accuracy: {accuracy_score(test_labels, predicted):.4f}")


if __name__ == "__main__":
    main()
