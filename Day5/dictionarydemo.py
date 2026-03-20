#Example1: creating dictionary
myDict = {101:"x", 102:"y", 103:"z"}
print(myDict)

#Example2 : Access items from dictionary
myDict1 = {
    "brand" : "Hyundai",
    "model" : "Ford",
    "year" : 1964
}
print(myDict1["brand"])
#using get()
print(myDict1.get("model"))

#Example3 : change values in dictionary
myDict2 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(myDict2)
myDict2["year"]=2020
print(myDict2)

#Example4 : Reading items from dictionary using loop
myDict3 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for i in myDict3:
    print(i)           #prints only keys from dictionary
for i in myDict3:
    print(myDict3[i])  #prints only values from dictionary
for i in myDict3.values():
    print(i)
for x,y in myDict3.items():
    print(x,y)          #prints both key and value pairs

#Example5 : Check key exist in dictionary or not
myDict4 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
if "brand" in myDict4:
    print("exist")
else:
    print("not exist")

print("model" in myDict4)       #To check if exist or not without loop

#Example6 : Find number of items in dictionary
myDict4 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(len(myDict4))

#Example7 : Adding items to dictionary
myDict5 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
myDict5["color"] = "red"
print(myDict5)

#Example8 : Remove item from dictionary
myDict6 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
myDict6.pop("year")
print(myDict6)
# del myDict6
# print(myDict6)          #NameError: name 'myDict6' is not defined.
myDict6.clear()
print(myDict6)            #clears the dictionary

#Example9 : Copying Dictionary
myDict7 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
myDict8 = myDict7
print(myDict8)           #copied

myDict9 = myDict7.copy()
print(myDict9)           #using copy()

