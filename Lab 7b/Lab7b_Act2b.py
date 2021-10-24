
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    # Name:         Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 7b - Act 2b
    # Date:         16 Oct, 2021

temp = input("Enter three or more values separated by spaces: ")
separate = input("Enter a two-character separator: ")
temp = temp.split()
for i in range(len(temp)):
    if i == len(temp) - 1:
        print(temp[i] , end = "")
    else:
        print(temp[i] , end =" " + separate + " ")       # Last number does not end with separator

