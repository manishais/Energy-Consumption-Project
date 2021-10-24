
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 7b - Act 2a
    # Date:         16 Oct, 2021



price = input("Enter three or more prices separated by spaces: ")
price = price.split()         # Splitting string into a list
for i in range(len(price)):
    price[i] = float((price[i] ))
    price[i] = "{:.2f}".format(price[i])
    pricenew = price[i].rjust(7)
    print("$" + pricenew)