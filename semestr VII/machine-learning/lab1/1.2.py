import numpy as np


def main():
    X = np.array([[1, 2, 3], [1, 3, 6]])
    y = np.array([5, 6])

    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    print(f"theta = {theta}")


if __name__ == "__main__":
    main()
    