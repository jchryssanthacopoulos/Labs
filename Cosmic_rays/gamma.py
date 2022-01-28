"""Gamma contraction exercises."""

import numpy as np


gamma = [
    # gamma_0
    np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, -1]
    ]),
    # gamma_1
    np.array([
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, -1, 0, 0],
        [-1, 0, 0, 0]
    ]),
    # gamma_2
    np.array([
        [0, 0, 0, complex(0, -1)],
        [0, 0, complex(0, 1), 0],
        [0, complex(0, 1), 0, 0],
        [complex(0, -1), 0, 0, 0]
    ]),
    # gamma_3
    np.array([
        [0, 0, 1, 0],
        [0, 0, 0, -1],
        [-1, 0, 0, 0],
        [0, 1, 0, 0]
    ])
]


def lower_gamma(u):
    if u == 0:
        return gamma[u]
    else:
        return -gamma[u]

def sigma(u, v):
    return complex(0, 0.5) * (np.matmul(gamma[u], gamma[v]) - np.matmul(gamma[v], gamma[u]))

def lower_sigma(u, v):
    return complex(0, 0.5) * (np.matmul(lower_gamma(u), lower_gamma(v)) - np.matmul(lower_gamma(v), lower_gamma(u)))


def prob_a():
    res = np.zeros((4, 4), dtype='complex128')
    for mu in range(4):
        res += np.matmul(lower_gamma(mu), gamma[mu])
    return res

def prob_b(v):
    res = np.zeros((4, 4), dtype='complex128')
    for mu in range(4):
        mat = np.matmul(np.matmul(lower_gamma(mu), gamma[v]), gamma[mu])
        res += mat
    return res

def prob_c(v, p):
    res = np.zeros((4, 4), dtype='complex128')
    for mu in range(4):
        res += np.matmul(np.matmul(lower_gamma(mu), gamma[v]), np.matmul(gamma[p], gamma[mu]))
    return res

def prob_d():
    res = np.zeros((4, 4), dtype='complex128')
    for mu in range(4):
        for nu in range(4):
            res += np.matmul(lower_sigma(mu, nu), sigma(mu, nu))
    return res
