import math

x0 = float(input("Please enter value of point x of the observer: "))
y0 = float(input("Please enter value of point y of the observer: "))
z0 = float(input("Please enter value of point z of the observer: "))

x1 = float(input("Please enter value of point x of the first point: "))
y1 = float(input("Please enter value of point y of the first point: "))
z1 = float(input("Please enter value of point z of the first point: "))

x2 = float(input("Please enter value of point x of the second point: "))
y2 = float(input("Please enter value of point x of the second point: "))
z2 = float(input("Please enter value of point x of the second point: "))

# vector 1
vector1x = x1 - x0
vector1y = y1 - y0
vector1z = z1 - z0
vector1 = (x1 - x0, y1 - y0, z1 - z0)

# vector 2
vector2x = x2 - x0
vector2y = y2 - y0
vector2z = z2 - z0
vector2 = (x2 - x0, y2 - y0, z2 - z0)

#normalize vector 1 
normvector1x = vector1x / math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2) + ((z1 - z0) ** 2))
normvector1y = vector1y / math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2) + ((z1 - z0) ** 2))
normvector1z = vector1z / math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2) + ((z1 - z0) ** 2))

#normalize vector 2
normvector2x = vector2x / math.sqrt(((x2 - x0) ** 2) + ((y2 - y0) ** 2) + ((z2 - z0) ** 2))
normvector2y = vector2y / math.sqrt(((x2 - x0) ** 2) + ((y2 - y0) ** 2) + ((z2 - z0) ** 2))
normvector2z = vector2z / math.sqrt(((x2 - x0) ** 2) + ((y2 - y0) ** 2) + ((z2 - z0) ** 2))


dotprod = (normvector1x * normvector2x) + (normvector1y * normvector2y) + (normvector1z * normvector2z)
theta= math.degrees(math.acos(dotprod))
print(theta)



