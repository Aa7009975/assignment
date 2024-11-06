def sum_digits(num):
    num = abs(num)
    return sum(int(digit) for digit in str(num))

user_input = int(input("Enter an integer: "))

print("The sum of the digits is:", sum_digits(user_input))

