# 1. Check if Coding For All string contains a word Coding using the method index, find or other methods.

test = "Coding For All"

result = test.index('Coding')
print(result)

#or

result = "Coding" in test
print(result)

 # 2. Replace the word coding in the string 'Coding For All' to Python.

old = "coding for all"
new = old.replace('coding', 'Python')
print(new)

 # 3. Split the string 'Coding For All' using space as the separator (split()) .

string =  'Coding For All'
new_string = string.split()
print(new_string)

 # 4. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

a = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
b = a.split(' , ')
print(b)

 # 5. What is the character at index 0 in the string Coding For All.

z = "coding for all"
print(z[0])

 # 6. What is the last index of the string Coding For All.

q = 'Coding for all' 
print(q[-1])

 # 7. Create an acronym or an abbreviation for the name 'Python For Everyone'.

text =  "Python For Everyone"
acro = "".join(word[0] for word in text.split())
print(acro)

 # 8. Create an acronym or an abbreviation for the name 'Coding For All'.

text1 = 'Coding For All'
acron = "".join(word[1] for word in text1.split())
print(acron)

 # 9. Use index to determine the position of the first occurrence of C in Coding For All.

text2 = "coding for all"
occ = text2.index('c')
print(occ)
occ1 = text2.index('f')
print(occ1)

 # 10. Use rfind to determine the position of the last occurrence of l in Coding For All People.

text3 =  "Coding For All People"
print(text3.rfind('l'))

 # 11. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text4 = 'You cannot end a sentence with because because because is a conjunction'
print(text4.find('because'))

print(text4.rindex('because')) # last occurance


 # 12. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence =  'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because'
start = sentence.find(phrase)

new_sentence = sentence[:start] + sentence[start+len(phrase)+1:]
print(new_sentence)

# or

new_sentence = sentence.replace("because because because", '')
print(new_sentence.strip())

 # 13. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sent =  'You cannot end a sentence with because because because is a conjunction'

print(sent.find('because'))

 # 14. Does ''Coding For All' start with a substring Coding?

k = "coding for all"
if k.startswith("coding"):
    print('yes, it does')
else:
    print("No")

 # 15. '   Coding For All      '  , remove the left and right trailing spaces in the given string.

o = ' coding for all ' 
print(o.strip())

 # 16. Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

 # 17. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

names =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
name_new = " - ".join(names)
print(name_new)

 # 18. Use the new line escape sequence to separate the following sentences.
#  I am enjoying this challenge.
# I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")

 # 19. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
    #   The area of a circle with radius 10 is 314 meters square. 

print(f"The area of a circle with radius {radius} is {area} meters square")    

 # 20. Make the following using string formatting methods: 8 + 6 = 14

g = 8
h = 6
print(f"{g} + {h} = {g+h}")
