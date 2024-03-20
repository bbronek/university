import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support

titanic_data = pd.read_csv('titanic.tsv', sep='\t')

titanic_data["Sex"] = titanic_data["Sex"].map({'male': 0, 'female': 1})
titanic_data["Embarked"] = titanic_data["Embarked"].map({'S': 0, 'C': 1, 'Q': 2})
titanic_data["Sex"] = pd.to_numeric(titanic_data["Sex"], errors="coerce")
titanic_data["Embarked"] = pd.to_numeric(titanic_data["Embarked"], errors="coerce")

FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
LABEL = "Survived"

data = titanic_data[FEATURES + [LABEL]].dropna()

data_train, data_test = train_test_split(data, test_size=0.2, random_state=42)

y_train = pd.DataFrame(data_train[LABEL])
x_train = pd.DataFrame(data_train[FEATURES])
model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train.values.ravel())

y_expected = pd.DataFrame(data_test[LABEL])
x_test = pd.DataFrame(data_test[FEATURES])
y_predicted = model.predict(x_test)

precision, recall, fscore, support = precision_recall_fscore_support(y_expected, y_predicted, average="binary")

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-score: {fscore}")

score = model.score(x_test, y_expected)
print(f"Model score: {score}")
