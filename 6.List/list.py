countries = ['Rwanda', 'Ghana', 'Nigeria', 'Australia']
# using list constructor
Nations = list(('Rwanda', 45, False))

print(countries)
print(countries[0])
print(countries[0][3])
# print from a given index up to the end  and range
print(countries[1:])
print(countries[1:3])

# get variable type
print(type(countries))

# update element in list
countries[0] = 'united Kingdom'
print(countries)
# length of the list
print(len(countries))

print(Nations)