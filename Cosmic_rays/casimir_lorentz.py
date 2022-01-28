# Compute Casimir of Lorentz transformations

from sympy.functions.special import tensor_functions


# K = [1, 2, 3]
# J = [5, 3, 6]
# K * J = 1 * 5 + 2 * 3 + 3 * 6 = 29

M = [
    [0, 1, 2, 3],
    [-1, 0, 6, -3],
    [-2, -6, 0, 5],
    [-3, 3, -5, 0]
]


total = 0

for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sigma in range(4):
                total += tensor_functions.eval_levicivita(mu, nu, rho, sigma) * M[mu][nu] * M[rho][sigma]

print(total * 0.5)
