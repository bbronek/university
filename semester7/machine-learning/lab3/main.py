from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def cost(theta, features, target):
    return np.mean((features @ theta - target) ** 2) / 2


def gradient(theta, features, target):
    return features.T @ (features @ theta - target) / len(target)


def gradient_descent(
    theta, features, target, learning_rate, tolerance, max_iterations=100000
):
    if learning_rate <= 0 or tolerance <= 0:
        raise ValueError("Learning rate and tolerance must be positive")
    current = cost(theta, features, target)
    history = [current]
    for _ in range(max_iterations):
        theta = theta - learning_rate * gradient(theta, features, target)
        previous, current = current, cost(theta, features, target)
        if not np.isfinite(current) or current > previous:
            raise ValueError("Learning rate causes divergence")
        history.append(current)
        if abs(previous - current) <= tolerance:
            return theta, history
    raise RuntimeError("Gradient descent did not converge")


def main():
    data = pd.read_csv(
        Path(__file__).with_name("fires_thefts.csv"),
        header=None,
        names=["fires", "intrusions"],
    )
    fire_mean = data["fires"].mean()
    fire_scale = data["fires"].std()
    features = np.column_stack(
        (np.ones(len(data)), (data["fires"] - fire_mean) / fire_scale)
    )
    target = data["intrusions"].to_numpy()
    theta, _ = gradient_descent(np.zeros(2), features, target, 0.01, 1e-4)
    print(
        "Optimal parameters:",
        [theta[0] - theta[1] * fire_mean / fire_scale, theta[1] / fire_scale],
    )
    for tolerance in (1e-4, 1e-3, 1e-2, 1e-1):
        _, history = gradient_descent(np.zeros(2), features, target, 0.01, tolerance)
        plt.plot(history, label=f"Tolerance {tolerance:g}")
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.title("Gradient descent convergence")
    plt.legend()
    plt.show()
    fires = np.array([50, 100, 200])
    predictions = (
        np.column_stack((np.ones(len(fires)), (fires - fire_mean) / fire_scale)) @ theta
    )
    for count, prediction in zip(fires, predictions):
        print(
            f"For {count} fires per thousand residents, predicted intrusions: {prediction:.2f}"
        )


if __name__ == "__main__":
    main()
