
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    ## Name:        Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 7b - Act 1
    # Date:         16 Oct, 2021

name = input("What is your name? ")
temp = list(name)
newname = name
vowels = ["A" , "E" , "I" , "O" , "U" , "a" , "e" , "i" , "o" , "u" ]

if temp[0] in vowels:                 # If name begins with a vowel
    newname = newname.lower()
    rhymef = "F" + newname
    rhymeb = "B" + newname
    rhymem = "M" + newname

else:
    if temp[1] in vowels:
        rhymef = "F" + name[1:]
        rhymeb = "B" + name[1:]
        rhymem = "M" + name[1:]
    else:
        rhymef = "F" + newname[2:]
        rhymeb = "B" + newname[2:]
        rhymem = "M" + newname[2:]

print(name + ", " + name + ", " + "Bo-" + rhymeb)
print("Banana-Fana Fo-" + rhymef)
print("Me Mi Mo-" + rhymem)
print(name + "!")
