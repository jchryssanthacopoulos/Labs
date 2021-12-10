"""Calibrate time."""

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
    parser = argparse.ArgumentParser(description="Get coefficients of linear regression for time calibration")
    parser.add_argument("--channel", type=str, help="Channel values of peaks") 
    parser.add_argument("--time", type=str, help="Reference time of peaks") 
    parser.add_argument("--channel_sigma", type=str, help="Channel sigma values of peaks") 
    args = parser.parse_args()

    channel_values = [float(c) for c in args.channel.split(",")]
    time_values = [float(e) for e in args.time.split(",")]

    if args.channel_sigma:
        channel_sigma_values = [float(c) for c in args.channel_sigma.split(",")]
    else:
        channel_sigma_values = None

    x = channel_values
    y = time_values
    m, b = lin_fit(x, y)

    # get R^2
    y_fit = [m * x_i for x_i in x]
    r2 = r2_score(y, y_fit)

    print(f"Slope = {m}")
    print(f"Intercept = {b}")
    print(f"R^2 = {r2}")

    plt.figure(figsize=(9, 6))
    if channel_sigma_values:
        plt.errorbar(x, y, xerr=channel_sigma_values, fmt='.', c='b')
    else:
        plt.plot(x, y, 'b.', markersize=30)

    x_interp = np.linspace(x[0] - 10, x[-1] + 10, 100)
    y_interp = [m * x_i + b for x_i in x_interp]

    plt.rcParams.update({'font.size': 17})

    label = "m = {:.2e}, b = {:.2f}".format(m, b)
    plt.plot(x_interp, y_interp, c='k', label=label)
    plt.grid()
    plt.legend()
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    plt.xlabel("Channel", fontsize=17)
    plt.ylabel("Delay (ns)", fontsize=17)
    plt.title("$R^2 = {:.2f}$".format(r2))
    # plt.tight_layout()
    plt.show()
    plt.savefig("figures/up_time_calibration.pdf")
