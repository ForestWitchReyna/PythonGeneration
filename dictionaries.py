car = {
    # key   #value
    "make": "Jaguar",
    "model": "XF",
    "year": 2019,
    "isNew": False,
}

# car["colour"] = "Red" #add new pair
# del car ["colour"]    #delete pair
# car ["owner"] = "Tim"
# print(car)

# info = input("what info would you like? ")
# print(car.get(info))
# print(car.get("make"))

print(car.items())#retursn key pairs

car.keys() #returns list of keys
car.values() #returns list of values


#car.clear() #empties a dictionairy
#"colour" in car
for key in car.keys():
    print ("the ", key, " is ", car[key])