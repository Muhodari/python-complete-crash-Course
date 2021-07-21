def Add_numbers():
    return 5 + 6


def Add_Numbers(number1, number2):
    return number1 + number2


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))

sumUp = Add_numbers()
sumUp2 = Add_Numbers(number1, number2)

print(sumUp2)
print(sumUp)
