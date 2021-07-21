# tuples are immutable they can't be changed one initialized

three_numbers = (1, 2, 3)
three_numbers2 = (1, 2, 3, 'Home', True)
strings = ('home', 'land', 'earth')
# tuple constructor
three_numbers3 = tuple(((1, 2, 3, 'Home', True)))

print(strings)

# trying to change the value at a given index
three_numbers[0] = 45
# once printed you get the error: TypeError: 'tuple' object does not support item assignment
print(three_numbers)
