
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 4b - Prog 4
    # Date:         23 Sept, 2021

import math

A = float(input("Enter the coefficient of x^2: "))
B = float(input("Enter the coefficient of x: "))
C = float(input("Enter C: "))

if A == 0 and B == 0 and C != 0:
    print("Error!")

elif A == 0:
    x1 = -C/B
    print("Root is: ", x1)

else:
    d = (B**2) - (4*A*C)

    if d > 0:                                                         # Roots are real and different
      
        x1 = (-B+math.sqrt(d))/(2*A)
        x2 = (-B-math.sqrt(d))/(2*A)
        print("Roots are: ", x1, x2)
    
    elif d == 0                                                       # Roots are real and equal
        print("2")
        x1 = (-B / (2*A))
        print("Roots are: ", x1, x1)

    else:                                                             # Roots are imaginary
      
        x1 = str(-B/(2*A))+"+"+str(math.sqrt(abs(d)))+"i"
        x2 = str(-B/(2*A))+"-"+str(math.sqrt(abs(d)))+"i"
        print("Roots are: ", x1, x2)
    
