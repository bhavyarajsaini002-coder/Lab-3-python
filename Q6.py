a  = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
a = a+b+c
b = a-(b+c)
c = a-(b+c)
a = a-(b+c)
print(f"Rotated values are a: {a}, b: {b}, c: {c}")