#Example1 : Creating tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

#Example2 : access tuple items
mytuple1 = ("apple", "banana", "cherry")
print(mytuple1[0])
print(mytuple1[-1])

#Example3 : range of indexes
mytuple2 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
print(mytuple2[2:5])
print(mytuple2[-4:-1])

#Example4 : Changing the items of tuple
mytuple3 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
myList = list(mytuple3)
myList[1] = "grapes"
myTuple = tuple(myList)
print(myTuple)

#Example5 : Reading tuple items using loop
mytuple4 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
for i in mytuple4:
    print(i)

#Example6 : Check if items exists (searching of item in tuple)
mytuple5 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
if "apple" in mytuple5:
    print("apple is in the list")
else:
    print("apple is not in the list")

#Example7 : Tuple length - counting items in a tuple
mytuple6 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
print(len(mytuple6))

#Example8 : Add items to tuple - not possible because tuple is immutable - cannot change values/items
mytuple7 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
mytuple7[0] = "grapes"  #TypeError: 'tuple' object does not support item assignment
print(mytuple7)

#Example9 : Copy tuple
mytuple8 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
mytuple9 = mytuple8
print(mytuple9)

#Example10 : Removing items from tuple - not possible because tuple is immutable
mytuple10 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
mytuple10.remove("apple")   #invalid / not possible
print(mytuple10)
del mytuple10  #it is possible to delete the tuple

#Example11 : Join/combine tuple
mytuple11 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
mytuple12 = (1,2,3,4,5)
tuple13 = mytuple11 + mytuple12  #Joining/concatenating is possible
print(tuple13)

#Example12 :
mytuple13 = ("apple", "banana", "cherry", "orange", "mango", "kiwi")
mytuple14 = (1,2,3,4,5)
if mytuple13 == mytuple14:
    print("Tuples are equal")
else:
    print("Tuples are not equal")






