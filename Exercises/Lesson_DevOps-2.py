# list is a data sructure which can hold multiple values of multiple types.
# array: a data sructure which can hold multiple values of same type.

list_of_cloud = ["AWS", "Azure", "GCP"]

# add a new cloud: IBM and Oracle

list_of_cloud.append("IBM")

# .append takes only one argument at a time at the end of the list

list_of_cloud.append("Oracle")
 
print("list_of_cloud", list_of_cloud)

list_of_cloud.insert(2, "Hiroku") # to insert a specific spot.
print("list_of_cloud", list_of_cloud)  # out: list_of_cloud ['AWS', 'Azure', 'Hiroku', 'GCP', 'IBM', 'Oracle']

print(len(list_of_cloud)) # 6

# insert at 0th index: mycloud
list_of_cloud.insert(0, "mycloud")
print(list_of_cloud)  # output: ['mycloud', 'AWS', 'Azure', 'Hiroku', 'GCP', 'IBM', 'Oracle']

# iteration of the list:

for cloud in list_of_cloud:
    print(cloud)

'''
output: 
mycloud
AWS
Azure
Hiroku
GCP
IBM
Oracle
'''

for i in range(1,11):
    print("Hello Sameer")

    


