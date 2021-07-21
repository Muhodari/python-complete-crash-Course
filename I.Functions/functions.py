def greetings_function(name, age):
    print("Welcome " + name + ".your are " + str(age) + " old")


# when number of parameters are unknown
def greetings2_function(*names):
    print('Welcome ' + names[1])


name = input("Enter your Names: ")
age = int(input("Enter your age: "))

# by dynamic values
greetings_function(name, age)
# by static values
greetings_function(name="John", age=45)

greetings2_function("John", 'Tim', 'Tom', 45)
