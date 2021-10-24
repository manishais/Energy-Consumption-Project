
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 4b - Prog 1
    # Date:         22 Sept, 2021
    
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter another number: "))
    
if num2 > num1:
    if num2 > num3:
        print(num2, "is the largest number.")
    else:
        print(num3, "is the largest number.")
else:
    print(num1, "is the largest number.")