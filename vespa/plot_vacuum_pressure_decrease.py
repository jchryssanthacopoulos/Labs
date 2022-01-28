"""Plot vacuum pressure."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.optimize import curve_fit


def func(x, p_0, tau):
    return (0.00032 - p_0) * np.exp(-x/tau) + p_0


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


# data for pressure decrease phase
time_pressure_decrease = np.array([
    0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360,
    390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900
])
pressure_pressure_decrease = np.array([
    0.00032, 0.00024, 0.00017, 0.00012, 0.000096, 0.000086, 0.00008, 0.000075, 0.00007, 0.000068, 0.000067,
    0.000064, 0.000062, 0.00006, 0.000058, 0.000057, 0.000056, 0.000055, 0.000054, 0.000053, 0.000052,
    0.000052, 0.000051, 0.00005, 0.00005, 0.00005, 0.000049, 0.000049, 0.000048, 0.000048, 0.000048, 0.000048,
    0.000047, 0.000047, 0.000047, 0.000047, 0.000046, 0.000046
])


# exponential fit
popt, pcov = curve_fit(func, time_pressure_decrease, pressure_pressure_decrease)
x_interp = np.linspace(time_pressure_decrease[0] - 10, time_pressure_decrease[-1] + 10, 100)
y_interp = func(x_interp, *popt)

print(f"p_0 = {popt[0]}")
print(f"tau = {popt[1]}")


plt.rcParams.update({'font.size': 17})

plt.plot(time_pressure_decrease, 100 * pressure_pressure_decrease, 'bo', markersize=3, linewidth=2)
plt.plot(x_interp, 100 * y_interp, 'r-', linewidth=2)

plt.grid()
plt.xticks()
plt.yticks()
plt.ylabel("Pressure (Pa)")
plt.xlabel("Time (s)")
plt.ylim([0, 0.08])
# plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.0e"))

plt.savefig("figures/vacuum_pressure_decrease_2.pdf", dpi=1000, bbox_inches="tight")
