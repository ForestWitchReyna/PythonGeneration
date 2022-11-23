import random
# nums = range(11)
# for num in nums:
#     print(num)

# i=0
# while i <= 10:
#     print (i)
#     i+=1

# nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
# for num in nums:
#     print (num)

# nums = range(11)
# for num in nums:
#     print(num)
# else:
#     print("Done!")


# list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
# list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
# for item1 in list1:
#     for item2 in list2:
#         if item1 == item2:
#             print(item1)

i = random.randint(1,100)
while i % 5 != 0:
    if i % 3 == 0:
        print("This number was a multiple of 3")
    else:
        continue
    print(i)