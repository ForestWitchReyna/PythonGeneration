age = int(input("enter your age: "))
salary = int(input("enter your salary: "))

if age > 21 and salary >= 21000:
    if age > 30 and salary >= 35000:        
        if age > 30 and salary >= 50000:
            print ("You can borrow up to £100,000")
        print ("You can borrow up to £75,000")
    print ("You can borrow up to £50,000")
else:
    print ("I'm afraid we cannot offer you a loan")


# if age > 21 and salary >= 21000:
#     print ("You can borrow up to £50,000")
# elif age > 30 and salary >= 35000:
#     print ("You can borrow up to £75,000")
# elif age > 30 and salary >= 50000:
#     print ("You can borrow up to £100,000")
# else:
#     print ("I'm afraid we cannot offer you a loan")