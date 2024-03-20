import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
from tensorflow import keras
from tensorflow.keras import layers

data = pd.read_csv('avocado_data.csv')

features = data.drop(['Date', 'type', 'region', 'AveragePrice'], axis=1)
labels = data['type']

data = data.dropna()

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(labels)
y_categorical = keras.utils.to_categorical(y_encoded)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_categorical, test_size=0.2, random_state=42)

num_classes = len(label_encoder.classes_)
input_shape = (X_train.shape[1],)
x_train = X_train
x_test = X_test

model = keras.Sequential(
    [
        layers.Dense(64, input_shape=input_shape, activation="relu"),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=64, epochs=10, validation_split=0.1)

y_pred_proba = model.predict(x_test)
y_pred = label_encoder.inverse_transform(y_pred_proba.argmax(axis=1))

df_results = pd.DataFrame({'true_label': label_encoder.inverse_transform(y_test.argmax(axis=1)),
                            'predicted_label': y_pred})

accuracy = accuracy_score(df_results['true_label'], df_results['predicted_label'])
print(f'Accuracy: {accuracy}')
