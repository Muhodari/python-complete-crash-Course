list1 = [4, 3, 5, 1, 2]
list2 = ['banana', 'Apples', 'mango', 'oranges']
list3 = list2.copy()

# arrange numbers in ascending order
list1.sort()
# combination of two list
list1.extend(list2)
# add element in list
list2.append('pineApple')
# put element at a specific index
list2.insert(1, 'pineApple')
# remove element in the list
list2.remove('banana')
list2.pop(2)
del list2[0]
# count number of occurrence
print(list2.count('pineApple'))
# remove last element from the list
list2.pop()
# delete the whole list
list2.clear()
