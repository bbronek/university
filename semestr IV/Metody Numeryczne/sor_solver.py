import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    step = 0
    phi = initial_guess[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b)  # Initial residual

    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i, j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
        step += 1
        print("Step {} Residual: {:10.6g}".format(step, residual))
        
    return phi

residual_convergence = 1e-10
omega = 1.2  # Relaxation factor

A = np.array([[4, 1, -1],
              [1, 3, 0],
              [-1, 0, 3]])

b = np.array([3, -1, 1])

initial_guess = np.zeros(3)

phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)
