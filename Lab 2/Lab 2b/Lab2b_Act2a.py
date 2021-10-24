
t1 = 13
t2 = 84
x1 = 1
y1 = 3
z1 = 7
x2 = 23
y2 = -5
z2 = 10


xslope = (x2 - x1)/(t2 - t1)
yslope = (y2 - y1)/(t2 - t1)
zslope = (z2 - z1)/(t2 - t1)

print("At 50 seconds: ")
x0 = (xslope * (50-t1) + 1)
y0 = (yslope * (50-t1) + 3)
z0 = (zslope * (50-t1) + 7)

print("x0 =" , x0 , "m")
print("y0 =" , y0 , "m")
print("z0 =" , z0 , "m")









