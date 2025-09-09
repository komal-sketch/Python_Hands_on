''' Dictionaries store key-value pairs 
and allow fast lookups.
* Lists are not hashable
'''
# Creating a Dictionary:

marks = {"Jack": 33, "Ryan": 34, "Sameer": 94}

print(marks, type(marks)) # output: {'Jack': 33, 'Ryan': 34, 'Sameer': 94} <class 'dict'>


#  Accessing & Modifying Values:

print(marks["Sameer"]) # output: 94

marks["Jack"] = 59  # updating value
print(marks)

marks["Jack Ryan"] = "Detective"    # adding new key value
print(marks)


#  Common Dictionary Methods:

print(marks.keys())  # output: dict_keys(['Jack', 'Ryan', 'Sameer', 'Jack Ryan'])

print(marks.values())  # output: dict_values([59, 34, 94, 'Detective'])

print(marks.items())  # output: dict_items([('Jack', 59), ('Ryan', 34), ('Sameer', 94), ('Jack Ryan', 'Detective')])

marks.pop("Jack")  # "Jack" key will be removed
print(marks)   

marks.clear()  # Empties dictionary
print(marks)

# Dictionary comprehension

table_of_5 = {i: 5*i for i in range(1, 11)}
print(table_of_5)

squares = {x: x**2 for x in range(5)}
print(squares)












