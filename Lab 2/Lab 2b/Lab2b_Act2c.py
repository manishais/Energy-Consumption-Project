
t1 = 13
t2 = 84
x1 = 1
y1 = 3
z1 = 7
x2 = 23
y2 = -5
z2 = 10

xslope = (x2 - x1) / (t2 - t1)
yslope = (y2 - y1) / (t2 - t1)
zslope = (z2 - z1) / (t2 - t1)

starting_point = 20
ending_point = 50
space = (ending_point - starting_point)/4
time = starting_point

print("At", time , "seconds: ")
x = (xslope * (time - t1) + 1)
y = (yslope * (time - t1) + 3)
z = (zslope * (time - t1) + 7)

print("x0 =" , x , "m")
print("y0 =" , y , "m")
print("z0 =" , z , "m")

print("------------------")

time += space

print("At", time , "seconds: ")
x = (xslope * (time - t1) + 1)
y = (yslope * (time - t1) + 3)
z = (zslope * (time - t1) + 7)

print("x0 =" , x , "m")
print("y0 =" , y , "m")
print("z0 =" , z , "m")

print("------------------")

time += space

print("At", time , "seconds: ")
x = (xslope * (time - t1) + 1)
y = (yslope * (time - t1) + 3)
z = (zslope * (time - t1) + 7)

print("x0 =" , x , "m")
print("y0 =" , y , "m")
print("z0 =" , z , "m")

print("------------------")

time += space

print("At", time , "seconds: ")
x = (xslope * (time - t1) + 1)
y = (yslope * (time - t1) + 3)
z = (zslope * (time - t1) + 7)

print("x0 =" , x , "m")
print("y0 =" , y, "m")
print("z0 =" , z , "m")

print("------------------")

time += space

print("At", time , "seconds: ")
x = (xslope * (time - t1) + 1)
y = (yslope * (time - t1) + 3)
z = (zslope * (time - t1) + 7)

print("x0 =" , x , "m")
print("y0 =" , y , "m")
print("z0 =" , z , "m")