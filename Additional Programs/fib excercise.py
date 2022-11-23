

def fib (position):
    print("calculating answer")
    x = 0
    y = 1
    z = 0
    i = 0
    while i < position:
        
        #print(x)
        #print(y)

        z = x + y
        x = y
        y = z

        i += 1
    return x

result = fib(position=10)
#result = fib("The result is", 100, 200)
print (result)

# def add_numbers (result_text, a, b):
#     print("Adding numbers", result_text, a+b)
#     return a + b

# result = add_numbers(a=100, b=200, result_text="REsult is")
# result = add_numbers("The result is", 100, 200)