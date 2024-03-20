import numpy as np


def main():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    A_inv = A**-1

    # calculates the inverse of each element
    print(A_inv)

    M = np.matrix([[1, 2], [2, 1]], dtype=float)
    M_inv = M**-1

    # correctly determines the inverse matrix
    print(M_inv)

if __name__ == "__main__":
    main()