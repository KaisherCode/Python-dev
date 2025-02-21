# Float

x = 3.3
y = 1.1 + 2.2

print(f"el valor de x es: ",x)
print(f"el valor de y es: ",y)

print(f"X es igual que Y: ",x == y)

y_str = format(y,".2g")
print('Str', y_str)
print(y_str==str(x))

print('*'*10)

print(f"Valor de Y and X: ",y,x)

tolerance = 0.00001
print(abs(x-y)<tolerance)