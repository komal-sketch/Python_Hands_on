def sum(*args):

    # args will be a tuple of all the values passed to sum
    total = 0  # initialization
    for item in args:
        total += item
    return total

print(sum(342, 2, 7, 9))

#-------------------------------------------------------
#kwargs

def marks(**kwargs):

    # kwargs is a dictionary with all the key value pairs which were passed to marks

    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Jack=35, ryan=57, sameer=97, Anupriya=49)
