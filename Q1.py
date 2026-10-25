X1 = float(input("Enter center X1: "))
Y1 = float(input("Enter center Y1: "))
r = float(input("Enter radius r: "))
X2 = float(input("Enter point X2: "))
Y2 = float(input("Enter point Y2: "))
if r <= 0:
    print("Invalid radius")
else:
    distance = ((X2 - X1) * 2 + (Y2 - Y1) * 2) ** 0.5
    if distance < r:
        print("Point is inside the circle")
    elif distance == r:
        print("Point is on the circle")
    else:
        print("Point is outside the circle")