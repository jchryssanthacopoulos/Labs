"""Plot time calibration."""

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


# TAC UP
tac_up_x = [1387.4, 2048.4, 2953.2, 5341.5, 11845.5, 15176.8, 20224.2, 24752.3, 31401.2]
tac_up_y = [3, 4, 5, 8, 16, 20, 26, 32, 40]
m_tac_up, b_tac_up = lin_fit(tac_up_x, tac_up_y)
y_fit = [m_tac_up * x_i + b_tac_up for x_i in tac_up_x]
r2_tac_up = r2_score(tac_up_y, y_fit)

# TAC DOWN
tac_down_x = [5502.3, 6336.5, 7082.1, 9625.5, 15936.6, 19134.1, 24006.8, 29084.8]
tac_down_y = [3, 4, 5, 8, 16, 20, 26, 32]
m_tac_down, b_tac_down = lin_fit(tac_down_x, tac_down_y)
y_fit = [m_tac_down * x_i + b_tac_down for x_i in tac_down_x]
r2_tac_down = r2_score(tac_down_y, y_fit)

# TAC UP-DOWN
tac_up_down_x = [4624.2, 5436.7, 6188.5, 8569.6, 14835.9, 17949.6, 22630.1, 27435.7, 31761.5]
tac_up_down_y = [3, 4, 5, 8, 16, 20, 26, 32, 40]
m_tac_up_down, b_tac_up_down = lin_fit(tac_up_down_x, tac_up_down_y)
y_fit = [m_tac_up_down * x_i + b_tac_up_down for x_i in tac_up_down_x]
r2_tac_up_down = r2_score(tac_up_down_y, y_fit)

plt.figure(figsize=(9, 6))
plt.rcParams.update({'font.size': 12})

plt.plot(tac_up_x, tac_up_y, 'kx', markersize=10)
label = "TAC UP: m = {:.2e}, b = {:.2f} ($R^2$ = {:.2f})".format(m_tac_up, b_tac_up, r2_tac_up)
x_interp = np.linspace(tac_up_x[0] - 10, tac_up_x[-1] + 10, 100)
y_interp = [m_tac_up * x_i + b_tac_up for x_i in x_interp]
plt.plot(x_interp, y_interp, c='k', label=label)

plt.plot(tac_down_x, tac_down_y, 'rx', markersize=10)
label = "TAC DOWN: m = {:.2e}, b = {:.2f} ($R^2$ = {:.2f})".format(m_tac_down, b_tac_down, r2_tac_down)
x_interp = np.linspace(tac_down_x[0] - 10, tac_down_x[-1] + 10, 100)
y_interp = [m_tac_down * x_i + b_tac_down for x_i in x_interp]
plt.plot(x_interp, y_interp, c='r', label=label)

plt.plot(tac_up_down_x, tac_up_down_y, 'bx', markersize=10)
label = "TAC UP-DOWN: m = {:.2e}, b = {:.2f} ($R^2$ = {:.2f})".format(m_tac_up_down, b_tac_up_down, r2_tac_up_down)
x_interp = np.linspace(tac_up_down_x[0] - 10, tac_up_down_x[-1] + 10, 100)
y_interp = [m_tac_up_down * x_i + b_tac_up_down for x_i in x_interp]
plt.plot(x_interp, y_interp, c='b', label=label)

plt.grid()
plt.legend()
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.xlabel("Channel", fontsize=17)
plt.ylabel("Delay (ns)", fontsize=17)
plt.show()
