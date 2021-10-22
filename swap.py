x = 10
y = 20
temp = x
x = y
y = temp
print("x = ", x)
print("y = ", y)

x, y = y, x
print("x = ", x)
print("y = ", y)

# using xor
x = x ^ y
y = x ^ y
x = x ^ y

print("x = ", x)
print("y = ", y)

x = x + y
y = x - y
x = x - y

print("x = ", x)
print("y = ", y)

 