a1 = int(input("Enter the first angle: "))
a2 = int(input("Enter the second angle: "))
a3 = int(input("Enter the third angle: "))
if a1 <= 0 or a2 <= 0 or a3 <= 0 or (a1 + a2 + a3) != 180:
    print("Invalid angle")
else:
    if a1 > 90 or a2 > 90 or a3 > 90:
        print("Obtuse triangle")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Right triangle")
    else:
        print("Acute triangle")