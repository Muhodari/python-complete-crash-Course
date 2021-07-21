number = int(input("Enter your number: "))

if number % 2 == 0:
    print(number, "is Even")
elif number % 2 != 0:
    print(number, "is Odd")
else:
    print("unkwon type of ", number)
