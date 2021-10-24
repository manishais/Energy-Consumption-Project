
# Kinetic energey = (0.5) * Mass * Velocity^2

import math

print("This program calculates the kinetic energy given mass and velocity.")
mass = float(input("Please enter the mass (kg): "))                                                                     # kilograms
velo = float(input("Please enter the velocity (m/s^2): "))                                                                     # m/s
energy = (0.5) * mass * math.pow(velo,2)                                       # joules
print("Kinetic Energy =",energy,"J")