import numpy as np
from scipy.constants import e

from pyncband import *

InP = Material.Material(1.34, 0, 0.07, 0.64, 9.6, 'InP')
CdS = Material.Material(2.20, -0.39, 0.21, 0.68, 5.3, 'CdS')

csnc = CoreShellParticle.CoreShellParticle(InP, CdS, 1.23, 1.05, 1.5)

print("Is CSNC type two?", csnc.type_two)
energies = np.array(csnc.calculate_s1_energies()) / e
print(energies)
col_energy = csnc.coulomb_screening_energy()
pol_energy = csnc.interface_polarization_energy()
print('Col:', col_energy, 'Pol:', pol_energy)
print(csnc.bandgap)
print(csnc.bandgap + np.sum(energies) + col_energy[0] + pol_energy[0])