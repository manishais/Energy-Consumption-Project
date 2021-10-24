
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 4b - Prog 2
    # Date:         22 Sept, 2021
    
velo = float(input("Enter the velocity of the flow (m/sec): "))
diameter = float(input("Enter the diameter of the pipe (m): "))
viscosity = float(input("Enter the fluid kinematic viscosity (m^2/sec): "))

reynoldnum = velo * diameter / viscosity

if reynoldnum < 2300:
    print("Reynold number for the pipe flow is," , reynoldnum, "and the flow is laminar.")
elif reynoldnum > 2300 and reynoldnum < 2900:
    print("Reynold number for the pipe flow is," , reynoldnum, "and the flow is in transition.")
else:
    print("Reynold number for the pipe flow is," , reynoldnum, "and the flow is turbulent.")