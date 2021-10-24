
import math

# Ohm's Law states that Voltage = Current * Resistance

res = 20                                                                       # ohms
current = 5                                                                    # amperes
volt = res * current                                                           # volts
print("Voltage is",volt,"volts.")

# Kinetic energey = (0.5) * Mass * Velocity^2

mass = 100                                                                     # kilograms
velo = 21                                                                      # m/s
energy = (0.5) * mass * math.pow(velo,2)                                       # joules
print("Kinetic energy is",energy,"J")

# To calculate radioactive decay

initial_amt = 3                                                                # grams
time = 5                                                                       # days
half_life = 3.8                                                                # days
final_amt = initial_amt * math.pow(2 , -time/half_life)                        # grams
print("Radon-222 left is" , final_amt , "g")

# To calculate sheer stress using τ=𝜎𝑡𝑎𝑛𝑡𝑎𝑛(φ)+ 𝑐

normal_stress = 20                                                             # lbf/in^2
cohesion = 2                                                                   # lbf/in^2
angle_fric = 35                                                                # degrees
angle_fric_rad = 35 * (math.pi / 180)                                          # radians
sheer_stress = normal_stress * math.tan(angle_fric_rad) + cohesion             # lbf/in^2 
print("Sheer stress is" , sheer_stress , "lbf/in^2")