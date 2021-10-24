
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

print("At 50 seconds: ")
x_50 = (xslope * (50 - t1) + 1)
y_50 = (yslope * (50 - t1) + 3)
z_50 = (zslope * (50 - t1) + 7)

print("x0 =" , x_50 , "m")
print("y0 =" , y_50 , "m")
print("z0 =" , z_50 , "m")

print("------------------")

print("At 51 seconds: ")
x_51 = (xslope * (51 - t1) + 1)
y_51 = (yslope * (51 - t1) + 3)
z_51 = (zslope * (51 - t1) + 7)

print("x0 =" , x_51 , "m")
print("y0 =" , y_51 , "m")
print("z0 =" , z_51 , "m")