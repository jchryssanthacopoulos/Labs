"""Plot vacuum pressure."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# volume
# diameter = 40 cm = 0.4 m => radius = 0.2 m
# length = 80 cm = 0.8 m
# V = pi * r^2 * d = 0.1 m^3


def lin_fit(x, y):
    X = np.array(x).reshape(len(x), 1)
    y = np.array(y).reshape(len(y), 1)
    reg = LinearRegression().fit(X, y)
    return reg.coef_[0][0], reg.intercept_[0]


class MathTextSciFormatter(mticker.Formatter):
    def __init__(self, fmt="%1.2e"):
        self.fmt = fmt
    def __call__(self, x, pos=None):
        s = self.fmt % x
        decimal_point = '.'
        positive_sign = '+'
        tup = s.split('e')
        significand = tup[0].rstrip(decimal_point)
        sign = tup[1][0].replace(positive_sign, '')
        exponent = tup[1][1:].lstrip('0')
        if exponent:
            exponent = '10^{%s%s}' % (sign, exponent)
        if significand and exponent:
            s =  r'%s{\times}%s' % (significand, exponent)
        else:
            s =  r'%s%s' % (significand, exponent)
        return "${}$".format(s)


# data for pressure increase phase
time_pressure_increase = np.array([
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 210, 240, 270,
    300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600
])
pressure_pressure_increase = 100 * np.array([
    6e-5, 7.4e-5, 8.8e-5, 1e-4, 1.2e-4, 1.4e-4, 1.5e-4, 1.7e-4, 2e-4, 2.2e-4, 2.3e-4, 2.5e-4, 2.6e-4, 2.8e-4,
    2.9e-4, 3e-4, 3.1e-4, 3.2e-4, 3.2e-4, 3.4e-4, 3.7e-4, 3.9e-4, 4.2e-4, 4.4e-4, 4.7e-4, 5e-4, 5.3e-4, 5.6e-4,
    6e-4, 6.3e-4, 6.6e-4, 6.9e-4, 7.1e-4
])



# linear fit
m, b = lin_fit(time_pressure_increase, pressure_pressure_increase)
y_fit = [m * x_i for x_i in time_pressure_increase]
r2 = r2_score(pressure_pressure_increase, y_fit)
x_interp = np.linspace(time_pressure_increase[0] - 10, time_pressure_increase[-1] + 10, 100)
y_interp = [m * x_i + b for x_i in x_interp]

print(f"Slope = {m}")
print(f"Intercept = {b}")
print(f"R^2 = {r2}")


plt.rcParams.update({'font.size': 17})

plt.plot(time_pressure_increase, pressure_pressure_increase, 'bo', markersize=3, linewidth=2)
plt.plot(x_interp, y_interp, 'r-', linewidth=2)

plt.grid()
plt.xticks()
plt.yticks()
plt.ylabel("Pressure (Pa)")
plt.xlabel("Time (s)")
plt.ylim([0, 0.08])
# plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.0e"))

plt.savefig("figures/vacuum_pressure_growth_2.pdf", dpi=1000, bbox_inches="tight")
