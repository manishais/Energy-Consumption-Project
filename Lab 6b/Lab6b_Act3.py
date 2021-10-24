
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 6b - Activity 3
    # Date:         9 Oct, 2021


input = input("Enter a four-digit integer: ")

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
    count = 0
    while(int(diff) != 6174):
        print(str(int(diff)) + " >", end = " ")
        count += 1

        if(len(str(diff)) == 3):      # if diff has 3 digits, add a 0 
            diff = '0'+ str(diff)
            
        ascending = "".join(sorted(str(diff)))
        descending = "".join(sorted(str(diff), reverse = True))
        diff = int(descending) - int(ascending)

        if diff == 0 :              # Edge case
            print(diff)
            break

        if diff == 6174:
            print(diff)

    
    print(str(int(input)) + " reaches " + str(diff) + " via Kaprekar's routine in "+ str(count)+" iterations")