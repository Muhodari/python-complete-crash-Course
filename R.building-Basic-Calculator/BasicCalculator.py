Number1 = int(input("Enter the first Number: "))
Number2 = int(input("Enter the second Number: "))
operator = input("Enter the operator(+,-,*,/):")

if operator == '+':
    print("Sum is: ", Number1 + Number2)
elif operator == '-':
    print('remainder is ', Number1 - Number2)
elif operator == '*':
    print("Product is ", Number1 * Number2)
elif operator == '/':
    print('quotient is :', Number1 / Number2)
else:
    print("the operator Not Found")
