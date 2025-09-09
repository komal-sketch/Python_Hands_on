# List Methods

marks = [2, 3, 4, 5, 21, 45]
print(marks)   #output: [2, 3, 4, 5, 21, 45]

marks.append(65) # this will change the original list
print(marks) # output: [2, 3, 4, 5, 21, 45, 65]

marks = [23, 34, 45, 56]
extra_marks = [67, 78, 89]

marks.extend(extra_marks)

print(marks)  # output: [23, 34, 45, 56, 67, 78, 89]

marks.sort()
print(marks)

marks.reverse()
print(marks)

marks.copy()
print(marks)

marks.pop()  # removes last element
print(marks)

marks.insert(2, 9) # insert 9 at position 2
print(marks)

marks.remove(45) 
print(marks)

''' List Comprehensions 
(Efficient list creation)
'''
#Create a list containing the table of 5

a = 5
table = []

for i in range(1, 11):
    table.append(5*i)

print(table)

# Alternate method is list comprehension

table = [5*i for i in range(1, 11)]
print(table)

