#Example1 : Creating set
mySet = {"apple", "banana", "cherry"}
print(mySet)

#Example2 : Accessing items from set
mySet1 = {"apple", "banana", "cherry"}
for i in mySet:
    print(i)

#Example3 : Value exists in set or not
mySet2 = {"apple", "banana", "cherry"}
print("banana" in mySet2)
print("apple" in mySet2)

#Example4 : Adding items to set : add()--> single item       update()--> add multiple items
mySet3 = {"apple", "banana", "cherry"}
mySet3.add("orange")
print(mySet3)
mySet3.update({1,2, "mango"})
print(mySet3)

#Example5 : Find number of items in a set
mySet4 = {"apple", "banana", "cherry"}
print(len(mySet4))

#Example6 : Remove items from set : remove()    discard()
mySet5 = {"apple", "banana", "cherry"}
mySet5.remove("banana")
print(mySet5)
mySet5.remove(2)    #This will give keyerror
print(mySet5)
mySet5.discard("apple")
print(mySet5)
mySet5.discard(8)     #This will not throw any error
print(mySet5)

#Example7 : Clear all items from set
mySet6 = {"apple", "banana", "cherry"}
mySet6.clear()
print(mySet6)

#del mySet
del mySet6
print(mySet6)   #NameError: name 'mySet6' is not defined.

#Example8 : Joining 2 sets - union()
set1 = {"apple", "banana", "cherry"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)





