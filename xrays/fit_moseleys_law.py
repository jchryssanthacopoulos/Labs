"""Find peaks in a spectrum."""

import argparse
from typing import List
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def lin_fit(x: List, y: List) -> Tuple:
    X = np.array(x).reshape(len(x), 1)
    y = np.array(y).reshape(len(y), 1)

    reg = LinearRegression().fit(X, y)

    return reg.coef_[0][0], reg.intercept_[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get fit between atomic number and energy (i.e., Moseley's Law)")
    parser.add_argument("--z", type=str, help="Atomic numbers") 
    parser.add_argument("--energies", type=str, help="Energies") 
    parser.add_argument("--sigma", type=str, help="Energy sigmas") 
    parser.add_argument("--xrange", type=str, help="Range of x in plot")
    parser.add_argument("--yrange", type=str, help="Range of y in plot")
    args = parser.parse_args()

    atomic_num = [int(c) for c in args.z.split(",")]
    energies = [float(e) for e in args.energies.split(",")]
    sigma = [float(s) for s in args.sigma.split(",")]
    xmin, xmax = [float(x) for x in args.xrange.split(",")]
    ymin, ymax = [float(y) for y in args.yrange.split(",")]

    x = [(z - 1)**2 for z in atomic_num]
    y = energies
    m, b = lin_fit(x, energies)

    # get R^2
    y_fit = [m * x_i for x_i in x]
    r2 = r2_score(y, y_fit)

    print(f"X = {x}")
    print(f"Y = {y}")
    print(f"Slope = {m}")
    print(f"Intercept = {b}")
    print(f"R^2 = {r2}")

    plt.rcParams.update({'font.size': 20})

    plt.figure(figsize=(9, 7))
    plt.errorbar(x, y, yerr=sigma, fmt='.', c='b')
    x_interp = np.linspace(x[0] - 10, x[-1] + 10, 100)
    y_interp = [m * x_i + b for x_i in x_interp]
    plt.plot(x_interp, y_interp, c='k')
    plt.grid()
    plt.xlim([xmin, xmax])
    plt.ylim([ymin, ymax])
    # plt.xticks(range(600, 875, 50), fontsize=20)
    # plt.yticks(np.arange(6, 8.75, 0.5), fontsize=20)
    plt.xlabel("$(Z-1)^2$", fontsize=20)
    plt.ylabel("Energy (keV)", fontsize=20)
    plt.title("$R^2 = {:.2f}$".format(r2))
    plt.show()
