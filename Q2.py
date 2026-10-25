s = float(input("Enter the side length of the  regular pentagon: "))
if s <= 0:
    print("Invalid side length")
else:
    area = (5 * s * 2) / (4 * (3 * 0.5))
    print(f"The area of the regular pentagon is: {area:.2f}")