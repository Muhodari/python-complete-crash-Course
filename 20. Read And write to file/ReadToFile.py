country_file = open('read.txt', 'r')
print(country_file.readable())
# we can also use for loop to print countries
for country in country_file.readlines():
    print(country)

# print lines as a list
print(country_file.readlines())
country_file.close()
