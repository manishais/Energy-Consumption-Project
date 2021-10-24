
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 4b - Prog 3
    # Date:         23 Sept, 2021


days = int(input("Enter the number of days: "))
if days <= 10:
    widgets = 10 * days
elif days > 10 and days <= 60:
    widgets = (10*10) + (40*(days-10))
elif days >= 61 and days < 100:
    a = days - 60
    widgets = (10*10) + (40*50) + sum(range(39,39-a,-1))
else:
    a = days - 60
    widgets = (10*10) + (40*50) + sum(range(39,0,-1))

print("The total number of widgets produced by the machine in", days, "days is:", widgets)