"""Plot paschen curve."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# cm
# d = 10e-4

# def func(x, a, b, c):
#     return b*x*d/(np.log(a*x*d)-c) 
# def func(x, a, b, c):
#     return b*np.exp(x)/(np.log(a*d) + x - c)
def func(x, a, b):
    return a*np.exp(x)/(b + x) 


# Pa
pressure = 100 * np.array([
    4.50E-03, 9.60E-03, 4.00E-02, 1.00E-01, 2.00E-01, 3.00E-01, 4.00E-01, 7.00E-01, 1, 3, 5
])
voltage = np.array([
    5.76, 4.72,	3.48, 3.48, 3.6, 3.68, 3.26, 4.32, 4.92, 6.32, 8.08
])
pressure_dc = 100 * np.array([
    5.70E-05, 3.40E-04, 8.60E-04, 1.60E-03, 2.50E-03, 4.00E-03, 8.10E-03, 2.00E-02, 4.00E-02
])
voltage_dc = np.array([
    22.81, 19.48, 18.23, 17.81, 17.08, 17.4, 18.02, 18.02, 18.75
])


# popt, pcov = curve_fit(func, pressure, voltage, p0=[100, 2700])
# x_interp = np.linspace(pressure[0] - 0.1, pressure[-1] + 0.1, 100)
# y_interp = func(x_interp, *popt)

# print(f"a = {popt[0]}")
# print(f"b = {popt[1]}")
# print(f"c = {popt[2]}")


plt.rcParams.update({'font.size': 17})

# plt.figure(figsize=(7, 5))
plt.plot(np.log10(pressure), voltage, 'bo-', markersize=7, linewidth=2, label="RF")
# plt.plot(pressure_dc, voltage_dc, 'ro-', markersize=3, linewidth=2, label="DC")
# plt.plot(np.exp(x_interp), y_interp, 'r-', linewidth=2)

plt.grid()
plt.xticks()
plt.yticks()
# plt.legend()
plt.xlim([-0.5, 3])
plt.ylabel("Voltage (V)")
plt.xlabel("Log$_{10}$ Pressure (Pa)")

plt.savefig("figures/paschen_curve_rf.pdf", dpi=1000, bbox_inches="tight")
