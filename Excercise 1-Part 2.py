# num = int(input("enter a number to see if it's odd or even: "))

# if (num % 2) == 0:  
#    print (num, "is an even number") 

# if (num % 4) == 0: 
#     print ("It's also a multiple of 4")
# else:  
#     print (num, "is an odd number")  


# num2 = int(input("enter a number: "))
# if (num2 % 3) == 0:
#     print ("fizz")
# elif (num2 % 5) == 0:
#     print ("buzz")

# temp_type = input("c for Celsius-Fahrenheit, f for vice versa ")

# if temp_type != ("c" or "f"):
#     print ("Invalid Input")
# else:
#     if temp_type == ("c" or "f"):
#         temp = int(input("Enter the temperature: "))
#         if temp_type == "c":
#             temp_con = (temp*1.8) + 32
#             print (f"{temp}C in F is {temp_con}F")
#         elif temp_type == "f":
#             temp_con = (temp-32) * (5/9)
#             print (f"{temp}F in C is {temp_con}C")
#         #else:
#         #    print ("Unaccepted input")
#     else:
#         print ("Invalid Input")

temp_type = ""
temp = 0
while temp_type != ("c" or "f"):
    temp_type = input("c for Celsius-Fahrenheit, f for vice versa ")
    if temp_type == ("exit"):
        print ("Exiting program")
        break
    elif temp_type != ("c" or "f"):
        print ("Invalid Input please enter c or f")
    
if temp_type == ("c" or "f"):
    #while temp_con != int:
    #while finished != True:
    while True:
        try:
            temp = int(input("Enter the temperature: "))
        except ValueError:
            print ("Invalid temperature, please enter only integers")
            continue
        else:
            break

    if temp_type == "c":
        temp_con = (temp*1.8) + 32
        print (f"{temp}C in F is {temp_con}F")
    elif temp_type == "f":
        temp_con = (temp-32) * (5/9)
        print (f"{temp}F in C is {temp_con}C")
        #else:
        #    print ("Unaccepted input")
    else:
        print ("Invalid Input")