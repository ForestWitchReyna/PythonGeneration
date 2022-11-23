import traceback
nullVal = 0
divVal = 10

# try:
#     finVal = divVal / nullVal
#     print (f"The answer is {finVal}")
# except Exception as e:
#     e="Woops, there was an error"
#     print (e)

try:
    finVal = divVal / nullVal
    print (f"The answer is {finVal}")
except Exception as e:
    e="Woops, there was an error"
    print (e)
    traceback.print_exception()
    try:
        notInt = int(input("Enter a string"))
    except ValueError:
        print ("The input can only accept whole numbers")

