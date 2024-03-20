import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

file_path = "communities.data"
df = pd.read_csv(file_path, header=None, na_values=["?"], skipinitialspace=True)
df = df.dropna()

x = df.iloc[:, 5:-1]
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

model_linear = LinearRegression()
model_linear.fit(X_train_scaled, y_train)
y_pred_linear = model_linear.predict(X_test_scaled)

alpha = 1.0
model_ridge = Ridge(alpha=alpha)
model_ridge.fit(X_train_scaled, y_train)
y_pred_ridge = model_ridge.predict(X_test_scaled)

rmse_linear = mean_squared_error(y_test, y_pred_linear, squared=False)
rmse_ridge = mean_squared_error(y_test, y_pred_ridge, squared=False)

print(f"RMSE for linear regression: {rmse_linear}")
print(f"RMSE for linear regression with regularization: {rmse_ridge}")
