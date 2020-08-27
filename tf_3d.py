# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:52:01 2020

@author: Ana
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.figure import Figure
from matplotlib import rcParams

#3D:

def dBofHz(inputHz):

    outValue = 20*np.log10( inputHz )
    print(outValue, " dB")
    return outValue

def calculateForZ(Coefficient_Array = [-0.2,0.3,0.1],Z_Input = 0.3-0.3j):
    
    summR = 0
    summI = 0
    for index in range(len(Coefficient_Array)):
        #print("x[n] ", Coefficient_Array[index])
        z_n_value = pow(Z_Input,-index)
        print("z^-n = ", z_n_value)
        print("np.real(Coefficient_Array[index] * z_n_value ", np.real(Coefficient_Array[index] * z_n_value))
        print("np.imag(Coefficient_Array[index] * z_n_value ", np.imag(Coefficient_Array[index] * z_n_value))
        summR += np.real(Coefficient_Array[index] * z_n_value)
        summI += np.imag(Coefficient_Array[index] * z_n_value)
    print("summR ", summR)
    print("summI ", summI)
    H_z = np.sqrt((summR**2) + (summI**2))
    print(H_z, " H_z")
    return H_z

def zplot(x=[-0.2,0.3,0.1]):
   

    # Kreiranje mreze u polarnim koordinatama i izracunavanje Z
    radiusArray = np.linspace(0, 1, 50)
    freqArray = np.linspace(0, 2*np.pi,120)

    magnitudeArrayMesh, phaseangleArrayMesh = np.meshgrid(radiusArray, freqArray)
    #print("radiusArrayMesh ", radiusArrayMesh)
    #print("freqArrayMesh ", freqArrayMesh)
    coordinateX = magnitudeArrayMesh * np.cos(phaseangleArrayMesh)
    coordinateY = magnitudeArrayMesh * np.sin(phaseangleArrayMesh)
    #print("coordinateX ", coordinateX)
    #print("coordinateY ", coordinateY)

    Z = magnitudeArrayMesh*(np.e**(1j*phaseangleArrayMesh))
    #print("Z ", Z)
    H_z = 0 + 0j
    for index in range(len(x)):
        H_z += x[index] * (Z**-index)
    #print("H_z ", H_z)
    H_z_real = np.real(H_z)
    H_z_imag = np.imag(H_z)
    #print("H_z_real ", H_z_real)
    #print("H_z_imag ", H_z_imag)
    FreqZ = []
    Z_dB = 20*np.log10(np.sqrt((H_z_real**2) + (H_z_imag**2)))
    for row in Z_dB:
        FreqZ.append(row[len(row)-1])
    #print("Z_dB ", Z_dB)

     # Plotovanje 3D povrsine
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(coordinateX, coordinateY, Z_dB, rstride=1, cstride=1, alpha=0.8, cmap='brg', vmin=-24., vmax=24.)
    # Dodavanje trake boja koja mapira vrednsoti sa bojama
    fig.colorbar(surf, shrink=0.5, aspect=10)
    # Prilagodjavanje z osa
    ax.view_init(45, -120)
    ax.set_zlim(-36, 36)
    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])
    ax.zaxis.set_major_locator(LinearLocator(9))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("Magnitude [dB]")
    plt.savefig('ZSurfaceSide.png')


    # Plotovanje 3D povrsine
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(coordinateX, coordinateY, Z_dB, rstride=1, cstride=1, alpha=0.8, cmap='brg', vmin=-24., vmax=24.)
    # Dodavanje trake boja koja mapira vrednsoti sa bojama
    fig.colorbar(surf, shrink=0.5, aspect=10)
    # Prilagodjavanje z osa
    ax.view_init(90, -90)
    ax.set_zlim(-36, 36)
    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])
    ax.zaxis.set_major_locator(LinearLocator(9))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("Magnitude [dB]")
    plt.savefig('ZSurfaceTop.png')
    plt.show()
    #frekvencijski odziv
    fig, ax1 = plt.subplots()
    ax1.set_title('Digital filter frequency response')
    ax1.plot(freqArray,FreqZ, 'b')
    ax1.set_ylabel('Amplitude [dB]')
    ax1.set_ylim([-24, 12])
    ax1.set_xlabel('Frequency [rad/sample]')
    ax1.set_xlim([0, (np.pi)])
    plt.savefig('ZFreq.png')
    plt.grid()
    plt.show()

    return

x=[-0.2,0.3,0.1]
zplot(x=x)
v = calculateForZ()
dBofHz(v)