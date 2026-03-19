#Example1 : how to create list
myList1 = [10, 20, 30, 40, 50]
myList2 = ["apple", "banana", "cherry"]
myList3 = ["apple",10, "banana",20, "cherry"]
myList4 = list()  #empty list
print(myList1)
print(myList2)
print(myList3)
print(myList4)

#Example2: Accessing items from the list
myList5 = ["apple", "banana", "cherry"]
print(myList5[0])
print(myList5[1])
print(myList5[2])
print(myList5[-1])
print(myList5[-2])

#Example3 : Range of indexes
myList6 = ["apple", "banana", "cherry", "mango", "orange"]
print(myList6[1:4])
print(myList6[-3:-1])

#Example4: change item value
myList7 = ["apple", "banana", "cherry"]
myList7[0] = "mango"
print(myList7)

#Example5 : read the list items using loop
myList8 = ["apple", "banana", "cherry", "mango", "orange"]
for item in myList8:
    print(item)

#Example6 : check if the item exist in the list or not
myList9 = ["apple", "banana", "cherry"]
if "apple" in myList9:
    print("Apple is in the list")
else:
    print("Apple is not in the list")

#Example7 : List length (counting number of items in a list)
myList10 = ["apple", "banana", "cherry"]
print(len(myList10))

#Example8 : Add item on the list : append() insert()
myList11 = ["apple", "banana", "cherry"]
myList11.append("mango")
myList11.insert(2, "orange")
print(myList11)

#Example9 : Remove item from the list : pop() remove() del() clear()
myList12 = ["apple", "banana", "cherry"] #pop
myList12.pop(0)
print(myList12)
myList13 = ["apple", "banana", "cherry"] #del
del myList13[1]
print(myList13)
myList14 = ["apple", "banana", "cherry"] #clear
myList14.clear()
print(myList14)
myList15 = ["apple", "banana", "cherry"] #remove
myList15.remove("apple")
print(myList15)

#Example10 : Copy list
myList16 = ["apple", "banana", "cherry"]
myList17 = list(myList16)   #1st approach of copying list
print(myList17)
myList18 = myList16.copy()  #2nd approach of copying list
print(myList18)

#Example11 : combine/join lists
#using + operator
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#using loop statement
list4 = ["apple", "banana", "cherry"]
list5 = [1, 2, 3]
for i in list5:
    list4.append(i)
print(list4)

#using extend function
list6 = ["apple", "banana", "cherry"]
list7 = [1,2,3,4,5,6]
list6.extend(list7)
print(list6)



