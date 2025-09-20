#1. Declare an empty list

my_list = []  #using square brackets

my_list = list() # using list constructer

print(my_list)

# 2. Declare a list with more than 5 items.

fruits = ["mango", "apple", "kiwi", "avacado", "oranges", "cherry"]
print(fruits)

# 3. Find the length of your list

print(f"Lenght is : ",len(fruits))

# 4. Get the first item, the middle item and the last item of the list

first_item = fruits[0]
middle_item = fruits[len(fruits) // 2]
last_item = fruits[-1]

print(first_item)
print(middle_item)
print(last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Sameer", 29, 5.11, "single", "Netherlands"]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


it_companies.append("Tesla")   # Add an IT company to it_companies

middle_index = len(it_companies) // 2

it_companies.insert(middle_index, "Netflix") # Insert an IT company in the middle of the companies list

it_companies[1] = it_companies[1].upper()  # Change one of the it_companies names to uppercase (IBM excluded!)

new = '#; '.join(it_companies) # Join the it_companies with a string '#;  '

to_check = "Tesla"

if to_check in it_companies:
    print("company exists in list", it_companies)

else:
    print("company not found")


print(it_companies)
print(len(it_companies))

print(new)

# 7. Sort the list using sort() method

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.sort()  # Sort the list in ascending (alphabetical) order

it_companies.reverse() # Reverse the list in descending order
print(it_companies)


# 8. Slice out the first 3 companies from the list

new_companies = it_companies[:3] # Slice out the first 3 companies from the list

new = it_companies[-3:] # Slice out the last 3 companies from the list

middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index] # middle IT company or companies from the list

print(new_companies)
print(new)
print(middle_company)

# 9. Remove the first IT company from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.pop(0) # Remove the first IT company from the list
middle_index = len(it_companies) // 2
del it_companies[middle_index]   # Remove the middle IT company or companies from the list

it_companies.pop(-1) # Remove the last IT company from the list

it_companies.clear() # Remove all IT companies from the list

del it_companies   # Destroy the IT companies list

# # Trying to print it now will raise an error
# # print(it_companies)  # This will cause NameError

print(it_companies) 


# 10. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end

print(joined_list)

# # 11. After joining the lists in question 10. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = joined_list.copy()

index = full_stack.index("Redux") + 1
full_stack.insert(index, "Python")
full_stack.insert(index + 1, "SQL")

print(full_stack)

'''
Exercises: 
Level 2'''

# 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()

print("sorted ages", ages)

min_age = min(ages)
max_age = max(ages)

print("min age: ", min_age)
print("max age: ", max_age)

# Add the min age and the max age again to the list.

ages.append(min_age)
ages.append(max_age)

print("Appended list is: ", ages)

# Find the median age (one middle item or two middle items divided by two)

n = len(ages)
mid_1 = (n-1) // 2
mid_2 = n // 2

median_age = (ages[mid_1] + ages[mid_2]) / 2

print(median_age)


# Find the average age (sum of all items divided by their number )

avg_age = sum(ages) / len(ages) 

print("Average age is: ", avg_age)

# Find the range of the ages (max minus min)

range = max(ages) - min(ages)

print("Range of ages: ", range)



