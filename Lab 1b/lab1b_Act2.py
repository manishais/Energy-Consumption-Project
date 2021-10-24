import math
import numpy
import matplotlib


# Mass is 2kg and acceleration is 5m/s^2. Force will be the product of mass and acceleration

print("Force is",2*5,"N")

# 𝑛𝜆=2𝑑𝑠𝑖𝑛θ ; distance = 0.025 nm ;  angle = 25 degrees ; n = 1

print("Wavelength is",((2*0.025)*math.sin(25))/1,"nm")

"""Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial amount 
 of 3 g and a half-life of 3.8 days. The equation for radioactive decay is 𝑁(𝑡)=𝑁02―𝑡/𝑡1/2"""

print("Radon-222 left is",3*2**(-5/3.8),"g")

"""Calculate the pressure of 5 moles of an ideal gas with a volume of 0.15 m^3, and temperature of 
425 K. The Ideal Gas Law is the equation of state of a hypothetical ideal gas and is a good 
approximation of the behavior of gases under many conditions. Use a value of 8.314 m^3Pa/K·mol 
for the gas constant. The standard unit of pressure in the SI system is kilopascals (kPa)."""

# PV = nRT

print("Pressure is", ((5*8.314*425)/0.15)*10**-3 , "kPa")