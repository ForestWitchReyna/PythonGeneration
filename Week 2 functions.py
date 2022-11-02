def add_numbers (result_text, a, b):
    print("Adding numbers", result_text, a+b)
    return a + b

result = add_numbers(a=100, b=200, result_text="REsult is")
result = add_numbers("The result is", 100, 200)

def get_name():
    return "Alice"

result = add_numbers (10, 5)
print("Result is", result)

def multiply_numbers (a, b, c):
    print("Multiplying numbers", a, b, c)
    return a * b * c

result2 = multiply_numbers(10, 4, 7)
print("Result is", result2)

def print_menu():
    print("Main Menu")
    print("Option 1")
    print("Option 2")
    print("Option 3")
    print("Option 4")
    #return not necessary

print_menu()

def my_function(*people):
    for person in people:
        print(person)

my_function("Alice", "bob", "dog")

def concatenate(**kwargs):
    result = ""

    for arg in kwargs.values():
        result += arg
    print (result)