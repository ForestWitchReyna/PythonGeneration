#def prime()


def trunc (integer):
    print("calculating answer")
    
    s_int = str(integer)
    
    if 0 in s_int:
        return False
    elif integer < 2:
        return False
    elif integer > 1:
        for i in range(2, integer**0.5 + 1):
            if not integer%i:
                return False

result = trunc(integer=1234567890)
#result = fib("The result is", 100, 200)
print (result)