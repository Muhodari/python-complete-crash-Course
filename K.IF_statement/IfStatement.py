a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

if a > b:
    print(str(a) + " is grater than " + str(b))
elif a < b:
    print(str(b) + " is greater than " + str(a))

else:
    print(str(a) + " is equal to " + str(b))

boy = True
short = True

if boy == True or short == True:
    print("He is a boy or he is short")
elif boy==False:
    print("She is a girl")
else:
    print("none of the two")



