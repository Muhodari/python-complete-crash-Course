list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'Apples', 'mango', 'oranges']

# combination of two list
list1.extend(list2)
print(list1)
# add element in list
list2.append('pineApple')
print(list2)
# put element at a specific index
list2.insert(1, 'pineApple')
print(list2)
# remove element in the list
list2.remove('banana')
print(list2)
# count number of occurrence
print(list2.count('pineApple'))


# delete the whole list
list2.clear()
print(list2)
