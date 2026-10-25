num =int(input("Enter a 4 digit number: "))
if num <1000 or num >9999:
    print("Invalid input")
else:
    d1 = num // 1000
    d2 = (num // 100) % 10
    d3 = (num // 10) % 10
    d4 = num % 10
    sum_first_two = d1 + d2
    sum_last_two = d3 + d4
    print("sum of first two digits:", sum_first_two)
    print("sum of last two digits:", sum_last_two)
    if sum_first_two == sum_last_two:
        print("the two sums are equal")
    else:
        print("the two sums are not equal")