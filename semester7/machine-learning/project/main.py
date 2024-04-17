import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv('house_prices_switzerland.csv')

X = data.drop(['HouseType'], axis=1)
y = data['HouseType']

size_mapping = {'S': 0, 'M': 1, 'L': 2}
X['Size'] = X['Size'].map(size_mapping)

X_encoded = pd.get_dummies(X, columns=['Balcony', 'Locality'], drop_first=True)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

missing_values = X_encoded.isnull().sum()
print("Brakujące dane:")
print(missing_values)

numeric_features = X_encoded.select_dtypes(include=['float64', 'int64']).columns
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', MinMaxScaler())
])

categorical_features = X_encoded.select_dtypes(include=['object']).columns
categorical_transformer = SimpleImputer(strategy='most_frequent')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

X_imputed = preprocessor.fit_transform(X_encoded)

X_train, X_test, y_train, y_test = train_test_split(X_imputed, y_encoded, test_size=0.2, random_state=42)

model_logistic_reg = LogisticRegression(penalty='l2')
model_logistic_reg.fit(X_train, y_train)
y_pred_logistic_reg = model_logistic_reg.predict(X_test)

model_logistic_no_reg = LogisticRegression(penalty='none')
model_logistic_no_reg.fit(X_train, y_train)
y_pred_logistic_no_reg = model_logistic_no_reg.predict(X_test)

model_nb = GaussianNB()
model_nb.fit(X_train, y_train)
y_pred_nb = model_nb.predict(X_test)

model_nn = Sequential()
model_nn.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model_nn.add(Dense(len(label_encoder.classes_), activation='softmax'))

model_nn.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model_nn.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=1)

y_pred_nn = model_nn.predict(X_test).argmax(axis=1)

accuracy_logistic_reg = accuracy_score(y_test, y_pred_logistic_reg)
precision_logistic_reg = precision_score(y_test, y_pred_logistic_reg, average='weighted')
recall_logistic_reg = recall_score(y_test, y_pred_logistic_reg, average='weighted')
f1_logistic_reg = f1_score(y_test, y_pred_logistic_reg, average='weighted')

accuracy_logistic_no_reg = accuracy_score(y_test, y_pred_logistic_no_reg)
precision_logistic_no_reg = precision_score(y_test, y_pred_logistic_no_reg, average='weighted')
recall_logistic_no_reg = recall_score(y_test, y_pred_logistic_no_reg, average='weighted')
f1_logistic_no_reg = f1_score(y_test, y_pred_logistic_no_reg, average='weighted')

accuracy_nb = accuracy_score(y_test, y_pred_nb)
precision_nb = precision_score(y_test, y_pred_nb, average='weighted')
recall_nb = recall_score(y_test, y_pred_nb, average='weighted')
f1_nb = f1_score(y_test, y_pred_nb, average='weighted')

accuracy_nn = accuracy_score(y_test, y_pred_nn)
precision_nn = precision_score(y_test, y_pred_nn, average='weighted')
recall_nn = recall_score(y_test, y_pred_nn, average='weighted')
f1_nn = f1_score(y_test, y_pred_nn, average='weighted')

print('Ewaluacja Regresji Logistycznej z Regularyzacją:')
print(f'Accuracy: {accuracy_logistic_reg:.4f}')
print(f'Precision: {precision_logistic_reg:.4f}')
print(f'Recall: {recall_logistic_reg:.4f}')
print(f'F1 Score: {f1_logistic_reg:.4f}')
print('\n')

print('Ewaluacja Regresji Logistycznej bez Regularyzacji:')
print(f'Accuracy: {accuracy_logistic_no_reg:.4f}')
print(f'Precision: {precision_logistic_no_reg:.4f}')
print(f'Recall: {recall_logistic_no_reg:.4f}')
print(f'F1 Score: {f1_logistic_no_reg:.4f}')
print('\n')

print('Ewaluacja Naiwnego Klasyfikatora Bayesowskiego:')
print(f'Accuracy: {accuracy_nb:.4f}')
print(f'Precision: {precision_nb:.4f}')
print(f'Recall: {recall_nb:.4f}')
print(f'F1 Score: {f1_nb:.4f}')
print('\n')

print('Ewaluacja Modelu Sieci Neuronowej:')
print(f'Accuracy: {accuracy_nn:.4f}')
print(f'Precision: {precision_nn:.4f}')
print(f'Recall: {recall_nn:.4f}')
print(f'F1 Score: {f1_nn:.4f}')
