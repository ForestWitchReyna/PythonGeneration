car = {
'brand': 'Ford',
'model': 'Mustang',
'year' : 1964,
'isNew': False
}


car["colour"] = "Red" #add new pair
print(car.get('colour'))

carUp = {'model': "Junker"}
print("Dictionary before update: ", car)
car.update(carUp)
print("Dictionary after update: ", car)

del car ["model"]
print(car)

print(car.items())

for key, value in car.items():
    print({key:value})
