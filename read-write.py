import sys
import csv

try:
    file = open("Hello!.txt", "r")

except FileNotFoundError as fnfe:
    print("Unable to open file:", fnfe)

#contents = file.read()
#print(contents)
#print(type(file))

#end="" remove newline from printing

lines = file.readlines()
print(lines)


for line in lines:
    #print(line,end="")
    #sys.stdout.write(line)
    print(line.rstrip("\n"))
