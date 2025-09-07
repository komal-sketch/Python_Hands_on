
# changing cases
'''text =" hello world "
 print(text.upper()) # Output: " HELLO WORLD "
 print(text.lower()) # Output: " hello world "
 print(text.strip()) # Output: "hello world"
 print(text.replace("world","Python"))# Output: " hello Python "
 print(text.split()) # Output: ['hello', 'world']
 print(text.capitalize) # output: Hello world'''

# stings are immutable means original string in memory wont change

name = "python world"
a = len(name)
print(name.upper())
print(name.upper(), name) #output: PYTHON WORLD Python world which indicates that original string in memory wont change.

print(name.capitalize()) # 1st letter will be capitalized
print(name.title()) # 1st letter of each word will be titled: Python World


# Removing whitespace

'''  text ="  hello world  "
 print(text.strip()) # Output: "hello world"
 print(text.lstrip())# Output: "hello world  "
 print(text.rstrip())# Output: "  hello world"'''

# Finding and Replacing

''' text ="Python is fun"
 print(text.find("is")) # Output: 7
 print(text.replace("fun","awesome")) # Output: "Python is awesome'''

# Splitting and Joining

''' text ="apple,banana,orange"
 fruits = text.split(",")
 print(fruits) # Output: ['apple', 'banana', 'orange']
 new_text =" - ".join(fruits)
 print(new_text) # Output: "apple - banana - orange"'''

# Checking String Properties

''' text ="Python123"
 print(text.isalpha()) # Output: False
 print(text.isdigit()) # Output: False
 print(text.isalnum()) # Output: True
 print(text.isspace()) # Output: False'''








