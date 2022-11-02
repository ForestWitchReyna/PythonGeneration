import csv
import json
# filename = "ford_escort.csv"

#read file as Dict

# with open(filename) as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)


# with open("people_excercise.csv", mode='w') as file:
#     writer = csv.writer(file, delimiter=",")

#     writer.writerow(["name","surname","age"])
#     writer.writerow(['Joe', 'Bloggs', 40])
#     writer.writerow(['Jane', 'Smith', 50])

#append to existing file
# with open("people_excercise.csv", mode="a") as file:
#     writer = csv.writer(file)
#     writer.writerow(['Mike', 'Wazowski', 40])


#filename="example.json"
#json read
file = open("example.json")

with open('example.json') as file:
    data = json.load(file)
    print(data)

with open('example.json', 'r') as file:
    data = json.load(file)
    for item in data['menu']['items']:
        print(item['id'])