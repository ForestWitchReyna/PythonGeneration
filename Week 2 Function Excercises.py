# def add_numbers(*args):
#     result = 0

#     for num in args:
#         result += num
#     return result

# print(add_numbers(2,3,4,6))

#Pass an arbitrary amount of named arguments to a function and create a dictionary.
#The keys will be the names of the arguments and the values are assigned values 
# of the named arguments.

def mult_numbers(**kwargs):
    result = 1
    #print(kwargs, type(kwargs))

    for arg in kwargs.values():
        result *= arg
    return result

print(mult_numbers(val1=5, val2=2, val3=10, val4=2))

def add_numbers(**kwargs):
    result = 0
    #print(kwargs, type(kwargs))

    for arg in kwargs.values():
        result += arg
    return result

print(add_numbers(val1=5, val2=2, val3=10, val4=2))

def add_numbers(*args):
    result = 0

    for num in args:
        result += num
    return result

numbs = input("Please enter numbers to be added seperated by spaces, such as '25 1 6 72' ")
print(add_numbers(2,3,4,6))


