"""Plot excitation energies."""

import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(9, 6))
plt.rcParams.update({'font.size': 12})

pairing_energy = 5 * 25 / 90

x = [1, 2, 3, 4]
energies = [1.50951, 1.43071, 1.41531, 1.3951]
energies_2 = [2.28261, 2.1866, 2.09901, 2.0828]


plt.plot(x, energies, 'bx', label="$2^+$", markersize=7, linewidth=10)
plt.plot(x, energies_2, 'rx', label="$4^+$", markersize=7)
plt.plot(range(6), np.ones(6) * pairing_energy, label="Pairing")

plt.grid()
plt.legend(loc="lower right")
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.xlim([0, 5])
plt.ylim([0, 2.5])
plt.xticks([0, 1, 2, 3, 4, 5], ["", "${^{92}Mo}$", "${^{94}Ru}$", "${^{96}Pd}$", "${^{98}Cd}$", ""])
plt.ylabel("Excitation Energy (MeV)", fontsize=17)
plt.show()
