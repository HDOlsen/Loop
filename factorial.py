

number = int(input("Enter an integer."))

def factorial(number):
    num = 1
    while number >= 1:
        num = num * number
        number = number - 1
    return num

factorial = factorial(number)
print(f"The factorial for {number} is {factorial}.")





