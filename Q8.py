v= float(input("Enter initial water volume v(litres): "))
n = int(input("Enter number of days n: "))
if v < 0 or n < 0:
    print("Invalid input")
else:
    final_volume = v*(0.95*n)+10((1-(0.95**n))/0.05)
    print(f"water quantity after {n} days is: {final_volume:.2f} litres")