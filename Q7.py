num = int(input("Enter a 3 digit number: "))
if num < 100 or num > 999:
    print("Invallid input")
else:
    d1 =num//100
    d2 = (num//10)%10
    d3 =num%10
    digit_sum = d1+d2+d3
    if num%digit_sum == 0:
        print(f"{num} is a Harshad number")
    else:
        print(f"{num} is not a Harshad number")