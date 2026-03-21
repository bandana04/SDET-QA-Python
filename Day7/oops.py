# #Example1:
# class myclass:                      #class creation
#     def myfunc(self):               #self means that this function belongs to myclass class
#         pass                        #pass means None
#     def display(self):
#         print("john")
# mc1 = myclass()                     #object creation
# mc1.myfunc()
# mc1.display()
#
# #or
# class myclass1:
#     def myfunc1(self):
#         pass
#     def display1(self,name):
#         print(name)
# mc2 = myclass1()
# mc2.myfunc1()
# mc2.display1("Bandana")
#
# #Example2
# class myclass2:
#     def m1(self):
#         print("This is instance method")
#     @staticmethod
#     def m2(self,num):
#         print(num)
# mc3 = myclass2()
# mc3.m1()
# mc3.m2(10,20)
# myclass2.m2(100,200)
#
# #Example3
# class myclass3:
#     a,b = 10,20
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc4 = myclass3()
# mc4.add()
# mc4.mul()
#
# #Exampl4
# i,j = 15,20                    #global variables
# class myclass4:
#     p,q = 10,20                #class variables
#     def add(self,x,y):
#         print(x+y)             #x and y are local variables
#         print(self.p+self.q)
#         print(i+j)             #i and j are global variables
# mc5 = myclass4()
# mc5.add(150, 120)
#
# #Example5
# k,l = 15,25
# class myclass5:
#     k,l = 10,20
#     def add1(self,k,l):
#         print(k+l)
#         print(self.k+self.l)
#         print(globals()['k']+globals()['l'])
# mc6 = myclass5()
# mc6.add1(110,120)
#
# #Example6 : one class can have multiple objects
# class myclass6:
#     def display(self,name):
#         print("This is display method.....")
#         print(name)
# obj1 = myclass6()
# obj1.display("Bandana")
# obj2 = myclass6()
# obj2.display("Limbu")
#
# #Example7 : Constructor example
# class myclass7:
#     def __init__(self):
#         print("This is constructor....")
#     def m3(self):
#         print("This is mc7")
# mc7 = myclass7()                        #Invoke constructor automatically
# mc7.m3()                                #method we have call explicitly by using object
# print(mc7.m3(12,23))

#Example8
class newclass:
    name = "John"
    def __init__(self,name):
        print(name)
        print(self.name)
obj = newclass("Bandana")

# #Example9
# #Requirement Employee : constructor : eid, ename, sal    display(): print eid, ename and sal
# class Employee:
#     eid = ""
#     ename = ""
#     sal = ""
#     def __init__(self,eid,ename,sal):
#         self.eid = eid           #class variables
#         self.ename = ename
#         self.sal = sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# e1 = Employee(100, "Ram", 10000)
# e1.display()
# e2 = Employee(200, "Raman", 20000)
# e2.display()

#Example10
#Requirement Employee : constructor : eid, ename, sal    display(): print eid, ename and sal
class Employee:
    eid = ""
    ename = ""
    sal = ""
    def __init__(self,eid,ename,sal):
        self.eid = eid           #class variables
        self.ename = ename
        self.sal = sal
    def __str__(self):
        return(self.ename)
e1 = Employee(100, "Ram", 10000)
print(e1)





