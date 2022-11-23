# print ("HelloWorld")
# print ("from me")
# menu = '''
# Menu
# 1. Hello 
# 2. Goodbye'''
# print (menu)

# amount = 12.40
# merchant = "Amazon"
# transaction_str = f"You spent £{amount:.2f} at {merchant}"
# print (transaction_str)

# empty_list = []
# numbers = [1, 2, 3, 4, 5]
# people = ["Lydia", "flamingo", "bonazai"]
# print (numbers[3])

# #if statements + else if
# a = 140
# if a < 10:
#     print("A is greater than 10!")

# elif a>120:
#     print("A is bigger than 120")

# else:
#     print ("who knows")

# print("The End")

def add_numbers (result_text, a, b):
    print("Adding numbers", result_text, a+b)
    return a + b

result = add_numbers(a=100, b=200, result_text="REsult is")
result = add_numbers("The result is", 100, 200)