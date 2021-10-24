
# To calculate the production of a well 

import math

print("This program calculates the production of a well.")
days = float(input("Please enter the number of days: "))
prod_rate = float(input("Please enter the initial production rate (barrels/day): "))
decline_rate = float(input("Please enter the initial decline rate (barrels/day): "))        
hyperbolic = float(input("Please enter the hyperbolic constant: "))
production =  prod_rate / (math.pow(1 + (hyperbolic * decline_rate * days) , (1/hyperbolic)))  
print("The production of a well =" , production)                  