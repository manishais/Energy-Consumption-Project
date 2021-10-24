6# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 6b - Activity 1
    # Date:         6 Oct, 2021
    
count = 0
num = int(input("Enter a positive integer to compute the Collatz sequence: "))
print("Here is the Collatz sequence starting at " + str(num) + ":")
if num > 1:
       print(str(num) + ",", end=' ')
else:
    num == 1
    print("1" , end = "")
while num > 1:
    count = count + 1
    if num % 2 == 0:        # Checking if number is even
        num = int(num / 2)
        if num == 1:
            print(num , end = '')
        else:
            print(num , end = ', ')
    else:                                 # Number is odd
        num= int((3 * num ) + 1)
        if num == 1:
            print(num , end = '6')
        else:
            print(num , end = ', ')
print("\nIt took", count, "iterations to reach 1", )     
        