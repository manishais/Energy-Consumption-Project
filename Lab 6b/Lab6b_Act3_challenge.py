
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 6b - Prog 3 Challenge
    # Date:         9 Oct, 2021

count = 0
for input in range(1,10000):
    input = str(input)
    if len(input) == 1:       # Making number four digits
        input = '000' + input
    elif len(input) == 2:
        input = '00' + input
    elif len(input) == 3:
        input = '0' + input
    
    elif len(input) > 4:
        print("Wrong output")
    
    
    if len(input) == 4:
        diff = input
     
    while(int(diff) != 6174):
        count += 1
    
        if(len(str(diff)) == 3):      # if diff has 3 digits, add a 0 
            diff = '0'+ str(diff)
            
        ascending = "".join(sorted(str(diff)))
        descending = "".join(sorted(str(diff), reverse = True))
        diff = int(descending) - int(ascending)
    
        if diff == 0 :              # Edge case
            break
print("Kaprekar's routine takes" , count, "total iterations for all four-digit numbers")
