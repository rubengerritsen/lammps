#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 08:54:28 2021

@author: ruben
"""

from rgpytools.orb import Orbitals

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerStem
import matplotlib
from matplotlib import rc
from matplotlib import lines
from tabulate import tabulate
plt.close("all")

def gaussian(x, center, fwhm):
      """ Computes the value of a gaussian with center x and fwhm at position x. """
      # FWHM = 2*sqrt(2 ln2) sigma = 2.3548 sigma
      sigma = fwhm / 2.3548;
      return(np.exp(-0.5 * ((x - center) / sigma)**2) / sigma / np.sqrt(2.0 * np.pi))

def computeSpectrum(x_eng, energies, oscillator):
    fwhm = 0.2
    y_spectrum = []
    for eng in x_eng:   
        level = 0
        for i in range(len(energies)):
            level += oscillator[i] * energies[i] * gaussian(eng, energies[i], fwhm)
        y_spectrum.append(level)
    return( np.array(y_spectrum))


pathToQMMM = "/home/ruben/lammps/QMMM/frame_798500/job_0_ACETONE_0:n/checkpoint_iter_2.hdf5"
pathToVaccuum = "/home/ruben/lammps/vaccuum/acetoneOpt.orb"

qmmm = Orbitals.fromQMMMCpt(pathToQMMM)
vac  = Orbitals.fromOrb(pathToVaccuum)

qmmmEnergy = qmmm.getSingletEnergies()
vacEnergy = vac.getSingletEnergies()

qmmmOSC = qmmm.getOscillatorStrenghts()
vacOSC = vac.getOscillatorStrenghts()

x_eng = np.linspace(0, 15, 1200)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# VACCUUM DATA
vacPlot = ax.stem(vacEnergy, vacOSC, use_line_collection=True, basefmt=" ", markerfmt=" ", linefmt="C0-", label="Oscillator strengths Vaccuum")
vdot = ax.scatter(vacEnergy, np.zeros(12), color='C0', s=20, label="Absorption spectrum Vaccuum")
vSpectrum = ax.plot(x_eng, 0.05 * computeSpectrum(x_eng, vacEnergy, vacOSC), label="Absorption spectrum Vaccuum", color='C0')

# QMMM DATA
ax.plot(np.linspace(4,11.5,100), np.zeros(100),linestyle=':', linewidth=1, color = 'k', zorder=-100) 
qmmmPlot = ax.stem(qmmmEnergy, qmmmOSC, use_line_collection=True, basefmt=" ", markerfmt=" ", linefmt="C1-", label="Oscillator strengths QMMM")
qdot = ax.scatter(qmmmEnergy, np.zeros(12), color='C1', s=20, label="Absorption spectrum QMMM")
qSpectrum = ax.plot(x_eng, 0.05 * computeSpectrum(x_eng, qmmmEnergy, qmmmOSC), label="Absorption spectrum QMMM", color='C1')

# FIGURE STUFF
ax.set_ylabel("Absorption (arb. units)")
#ax.axes.yaxis.set_ticklabels([0,0])
ax.set_xlim([4,12.5])
ax.set_xlabel("Energy (eV)")
fig.show()
ax.legend(handles = [vdot, qdot], loc='upper right', labelspacing=0.15)
#ax.set_aspect(aspect=1.4)

print(tabulate(np.array([ vacEnergy, qmmmEnergy, qmmmEnergy - vacEnergy]).transpose(), 
               headers=["vaccuum", "qmmm", "shift (q-v)"],
               showindex="always"))