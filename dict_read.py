people = {}
#names = {"john" : 2, "sally": 3}

file = open("recursive_people.txt")
lines = file.readlines()
print(lines)

for name in lines:
    name = name.rstrip()
    print(name)
    #people[name] = 1
    if name in people:
        people[name]+=1
    else:
        people[name] = 1

print(people)








# with open ("recursive_people.txt", "r") as file:
#         for lines in file:
#             lines = file.read()
#             names = lines.split()

#             #(key) = lines#.split()
#             i=+1
#             (val) = i

#             #people[int(key)] = val
#             #file.write(f"{person}\n")

# print (people)