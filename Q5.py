num = int(input("Enter a 5 digit number: "))
if num < 10000 or num > 99999:
    print("Invalid input")
else:
    n1 = num//10000
    n2 = (num//1000)%10
    n3 = (num//100)%10
    n4 = (num//10)%10
    n5 = num%10
max_val = n1
pos = 1
if n2 > max_val:
    max_val = n2
    pos = 2
if n3 > max_val:
    max_val = n3
    pos = 3
if n4 > max_val:
    max_val = n4
    pos = 4
if n5 > max_val:
    max_val = n5
    pos = 5
print("Maximum value:", max_val)
print("Position of maximum value:", pos)