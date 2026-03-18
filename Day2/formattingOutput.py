name, age, sal = "John", 21, 10000.0

#Approach1
print(name, age, sal)

#Approach2
print("Name is : ", name)
print("Age is : ", age)
print("Salary is : ", sal)

#Approach3
print("Name is : %s Age is : %d Salary is : %g"%(name, age, sal))

#Approach4
print("Name is :{} Age is :{} Salary is :{}".format(name, age, sal))

#Approach5
print("Age is :{age} Salary is :{sal} Name is {name}".format(name=name, age=age, sal=sal))