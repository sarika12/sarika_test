from collections import OrderedDict
func_dict = dict(add=lambda x, y: x + y, substract=lambda x, y: x-y )
add1=func_dict["add"](9,3)
print(add1)
d = OrderedDict.fromkeys('abcde')
d.move_to_end("b")
b=''.join(d.keys())
print (b)
d.move_to_end('b', last=False)
b=''.join(d.keys())
print (b)

list1 = ['biju', 'prahallad', 'vandana', 'sundar', 'rohit']
list2 = ['biju', 'prahallad', 'vandana']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)

import sys

list1 = ['Sahaj', 'Madhu', 'Rohit', 'Anand', 'Sarika']
print("size of list = ", sys.getsizeof(list1))

name = 'Prathyusha'
print("size of name = ", sys.getsizeof(name))

listOne = [20, 20, 20, 20]
print("All element are duplicate in listOne", listOne.count(listOne[0]) == len(listOne))
print (listOne.count(listOne[0]))
#Tip and Trick 2: Convert Mutable into Immutable
# my_list = [1, 2, 3, 4, 5]
# my_list = frozenset(my_list)
# my_list[3] = 7
# print(my_list)

#Tip and Trick 3: Merging Two Dictionaries in Python

# dict_1 = dict(one=1,two=2)
# dict_2 = dict(two=2,three=3)
# dictionary = dict(**dict_1, **dict_2)
# print(dictionary)

list_1 = ['a','b','c']
list_2 = [1, 2, 3]
for x, y in zip(list_1, list_2):
    print(x, y)



