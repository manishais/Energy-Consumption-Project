import math

t1 = 30
t2 = 45
dist1 = 50
dist2 = 615
speed = (dist2 - dist1) / (t2 - t1)
starting_point = 50 - (speed * 30)

time = float(input("Enter the time for part 1: "))
dist = (speed * time) + starting_point
print("For Part 1: ")
print("For t =", time,"seconds, the position p = ",dist,"meters")

radius = 500
circumference = (2 * math.pi * radius)

time = float(input("Enter the time for part 2: "))
dist = (speed * time) + starting_point

if dist > circumference:
   dsf = dist % circumference
   print("For",time,"seconds, the position p =",dsf,"meters")
else:
   print("For",time,"seconds, the position p =",dist ,"meters")
