"""
lists are ordered
changeable
and
allow duplicate
"""

list = ["ram", 'janu', 25, 12, 3.0, False]
print(list)
print(list[1:3])
print(len(list))
print(type(list))
list[3]='jessi'
print(list)
list.insert(2,36)
list.append('car')
list.remove(25)
print(list)