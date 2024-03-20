import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("fires_thefts.csv", header=None, names=["fires", "intrusions"])

def J(theta, X, y):
    m = len(y)
    h = X.dot(theta)
    return (1 / (2 * m)) * np.sum((h - y) ** 2)

def dJ(theta, X, y):
    m = len(y)
    h = X.dot(theta)
    gradient = (1 / m) * X.T.dot(h - y)
    return gradient

def gradient_descent(fJ, fdJ, theta, X, y, alpha, eps):
    current_cost = fJ(theta, X, y)
    history = [current_cost]
    while True:
        theta = theta - alpha * fdJ(theta, X, y)
        current_cost, prev_cost = fJ(theta, X, y), current_cost
        if abs(prev_cost - current_cost) <= eps:
            break
        if current_cost > prev_cost:
            print("The step length (alpha) is too big!")
            break
        history.append(current_cost)
    return theta, history

theta_initial = np.zeros(2)
alpha = 0.00001
eps = 0.0001

X = np.vstack((np.ones(data.shape[0]), data["fires"])).T
y = data["intrusions"]

theta_start = np.zeros(X.shape[1])
theta_best, _ = gradient_descent(J, dJ, theta_start, X, y, alpha, eps)

print("Optimal theta parameters:")
print(theta_best)

def plot_cost_history(cost_history):
    plt.plot(range(len(cost_history)), cost_history)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost')
    plt.title('Dependence of cost on the number of iterations')
    plt.show()

eps_values = [1e-4, 1e-3, 1e-2, 1e-1]
cost_history_list = []

for eps in eps_values:
    theta_start = np.zeros(X.shape[1])
    _, cost_history = gradient_descent(J, dJ, theta_start, X, y, alpha, eps)
    cost_history_list.append(cost_history)

for i, eps in enumerate(eps_values):
    plot_cost_history(cost_history_list[i])


pozary_to_predict = np.array([50, 100, 200])
X_predict = np.vstack((np.ones(len(pozary_to_predict)), pozary_to_predict)).T
predicted_thefts = X_predict.dot(theta_best)

for i in range(len(pozary_to_predict)):
    print(f"For {pozary_to_predict[i]} fires for thousand inhabitants, expected intrusions number {predicted_thefts[i]:.2f} for thousand inhabitants.")
