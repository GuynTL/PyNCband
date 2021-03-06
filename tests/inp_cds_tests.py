"""This test script verifies the accuracy of the model against Table 1 as seen in:
Dennis, A. M., Mangum, B. D., Piryatinski, A., Park, Y.-S., Hannah, D. C., Casson, J. L., … Hollingsworth, \
J. A. (2012). Suppressed Blinking and Auger Recombination in Near-Infrared Type-II InP/CdS Nanocrystal Quantum Dots. \
Nano Letters, 12(11), 5545–5551. https://doi.org/10.1021/nl302453x

"""

import numpy as np

from pyncband import Material, CoreShellParticle


# @profile
def main():

    inp_effective_electron_mass = 0.073
    InP = Material(1.34, 0, inp_effective_electron_mass, 0.64, 9.6, "InP")
    CdS = Material(2.20, -0.39, 0.21, 0.68, 5.3, "CdS")

    shell_widths = np.array([0.53, 1.05, 1.47, 1.90, 2.76, 3.84])

    experimental_bandgaps = [1.78, 1.46, 1.37, 1.32, 1.26, 1.24]
    print(
        "Using InP electron effective mass: {:0.2f}".format(inp_effective_electron_mass)
    )
    print(
        "Core \t Shell \tExp \t BG \t E(e): E(h): Coulomb: Polarization: Model(Exp-Model):"
    )
    for i, shell_width in enumerate(shell_widths):
        csnc = CoreShellParticle(InP, CdS, 1.23, shell_width, 1.5)
        print(1.23, "\t", shell_width, end="\t")
        # print("Is CSNC type two? h/e?", csnc.type_two, csnc.h_e)
        energies = np.array(csnc.calculate_s1_energies())
        # print(energies)
        plots = False
        col_energy_sectioned = csnc.coulomb_screening_energy(plot_integrand=plots)
        pol_energy_sectioned = csnc.polarization_screening_energy(plot_integrand=plots)
        self_energy = csnc.self_interaction_energy()
        # print(xx_coulomb_sectioned)
        # whole_integral_energy = (
        #     csnc.bandgap + np.sum(energies) + col_energy_whole[0] + pol_energy_whole[0]
        # )
        sectioned_integral_energy = (
            csnc.bandgap
            + np.sum(energies)
            + col_energy_sectioned[0]
            + pol_energy_sectioned[0]  # + self_energy
        )  # + xx_coulomb_sectioned[0]
        # print("Col:", col_energy_whole, col_energy_sectioned, "Pol:", pol_energy)
        # print("NC bandgap:", csnc.bandgap)
        print(experimental_bandgaps[i], end="\t")
        # print(
        #     "{:0.2f}({:0.2f})".format(
        #         whole_integral_energy,
        #         abs(experimental_bandgaps[i] - whole_integral_energy),
        #     ),
        #     end="\t",
        # )
        print(
            "{:0.3f}\t{:0.3f}\t{:0.3f}\t{:0.3f}\t{:0.3f}\t{:0.3f}\t{:0.3f}".format(
                csnc.bandgap,
                energies[0],
                energies[1],
                col_energy_sectioned[0],
                pol_energy_sectioned[0],
                sectioned_integral_energy,
                experimental_bandgaps[i] - sectioned_integral_energy,
            ),
            end="\t",
        )
        print()
        # print(csnc.localization_electron_shell(shell_width))
        # print(csnc.localization_hole_core())


if __name__ == "__main__":
    main()
