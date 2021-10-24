
# To calculate sheer stress using τ=𝜎𝑡𝑎𝑛𝑡𝑎𝑛(φ)+ 𝑐

import math

print("This program calculates sheer stress")
normal_stress = float(input("Please enter the normal stress (lbf/in^2): "))                                                             
cohesion = float(input("Please enter the cohesion (lbf/in^2): "))                                                               
angle_fric = float(input("Please enter the angle of friction (degrees): "))                                                              
angle_fric_rad = 35 * (math.pi / 180)                                          
sheer_stress = normal_stress * math.tan(angle_fric_rad) + cohesion             
print("Sheer stress =" , sheer_stress , "lbf/in^2")