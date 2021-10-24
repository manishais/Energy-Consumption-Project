# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 6b - Activity 2
    # Date:         6 Oct, 2021
    
total = 0
prod = 1
num = int(input("Enter an integer: "))
newnum = num
while num>0:
    total = total + num             # Finding the sum
    prod = prod * num               # Finding the product
    num = num - 1
print("The sum of all integers from 0 to", newnum, "is", total)
print("The product of all integers from 1 to", newnum, "is", prod)