# i =0
# while i < 5:
#     print(i)
#     i += 1

adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# for adj in adjectives:
#     for fruit in fruits:
#         print(adj, fruit)

# for fruit in fruits:
#     for adj in adjectives:
#         print(adj, fruit)

stuff = [1,2,3,4,5]     #pulling from list
for x in stuff:
    print(stuff[x])

try:
    for x in stuff:
        print(stuff[x]) 
except Exception as e:  #exception function
    print(e)

for adj in adjectives:
    print("ADJ: ", adj)
    for fruit in fruits:
        print(adj, fruit)
    print ("ADJ is still:", adj)