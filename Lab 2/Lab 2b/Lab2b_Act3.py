
"""
x = 1
y = 10
z = 0
x = y
x += 1
y += x
y *= x
z += x
z += y
print(z)

"""
# 1
z = 0
x = 1
z += x
print(z)

# 24
y = 10
z += y
z += y
z += x
z += x
z += x
print(z)

# 321
z = 0
x = y
y *= x
x = 1
x +=1
x +=1
y *= x
z += y
y = 10
x = y
y += x
x = 1
y += x
z += y
print(z)

#10000000000000000
z = 0
y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z += y
print(z)

#1234
z = 0
y = 10
x = y
y *= x
y *= x
z += y
y = 10
x = y
y *= x
x = 1
x += 1
y *= x
z += y
y = 10
x += 1
y *= x
z += y
x = 1
x += 1
x += 1
x += 1
z += x
print(z)






