"""Find peaks in a spectrum."""

import argparse
from typing import List
from typing import Tuple

import numpy as np
from sklearn.linear_model import LinearRegression


def lin_fit(x: List, y: List) -> Tuple:
    X = np.array(x).reshape(len(x), 1)
    y = np.array(y).reshape(len(y), 1)

    reg = LinearRegression().fit(X, y)

    return reg.coef_[0][0], reg.intercept_[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get coefficients of linear regression for energy calibration")
    parser.add_argument("--counts", type=str, help="Channel values of peaks") 
    parser.add_argument("--thickness", type=str, help="Reference energy of peaks") 
    args = parser.parse_args()

    counts = [float(c) for c in args.counts.split(",")]
    thickness = [float(e) for e in args.thickness.split(",")]

    x = thickness
    y = [np.log(counts[0]) - np.log(c) for c in counts]
    m, b = lin_fit(x, y)

    print(f"X = {x}")
    print(f"Y = {y}")
    print(f"Slope = {m}")
    print(f"Intercept = {b}")
