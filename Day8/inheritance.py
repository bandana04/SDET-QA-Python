# #Example1 Single inheritance
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")
# bobj = B()
# bobj.m1()
# bobj.m2()

# #Example2 Single inheritance with arguments
# class A:
#     x, y = 100, 200
#     def m1(self):
#         print(self.x + self.y)
# class B(A):
#     a, b = 10, 20
#     def m2(self):
#         print(self.a + self.b)
# bobj = B()
# bobj.m1()
# bobj.m2()

# #Example3 : Multilevel Inheritance
# class A:
#     x, y = 100, 200
#     def m1(self):
#         print(self.x + self.y)
# class B(A):
#     a, b = 10, 20
#     def m2(self):
#         print(self.a + self.b)
# class C(B):
#     c,d = 12, 13
#     def m3(self):
#         print(self.c + self.d)
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# #Example4 : Hierarchy Inheritance
# class A:
#     x, y = 100, 200
#     def m1(self):
#         print(self.x + self.y)
# class B(A):
#     a, b = 10, 20
#     def m2(self):
#         print(self.a + self.b)
# class C(A):
#     c,d = 12, 13
#     def m3(self):
#         print(self.c + self.d)
# cobj = C()
# cobj.m1()
# cobj.m3()
# bobj = B()
# bobj.m1()
# bobj.m2()

# #Example5 : Multiple Inheritance
# class A:
#     x, y = 100, 200
#     def m1(self):
#         print(self.x + self.y)
# class B:
#     a, b = 10, 20
#     def m2(self):
#         print(self.a + self.b)
# class C(A,B):
#     c,d = 12, 13
#     def m3(self):
#         print(self.c + self.d)
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

##Example6 : Using the same class in child class is Overriding
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")    #Using the same m1 method from base class to child class
#         super().m1()        #This will invoke m1 method from base class
# bobj = B()
# bobj.m1()

# #Example7
# class A:
#     a,b = 1,2
# class B(A):
#     i,j = 3,4
#     def m(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
# bobj = B()
# bobj.m(5,6)

# #Example8 : Overriding variables
# class Parent:
#     name = "Bandana"
# class Child(Parent):
#     name = "Limbu"    #Overriding the variable value
# cobj = Child()
# print(cobj.name)

# #Example9: Overriding methods
# class Bank:
#     def rateofinterest(self):
#         return 0
# class XBank(Bank):
#     def rateofinterest(self):
#         return 1
# class YBank(Bank):
#     def rateofinterest(self):
#         return 2
# yobj = YBank()
# print(yobj.rateofinterest())
# xobj = XBank()
# print(xobj.rateofinterest())

# #EXample10 : Overloading (POlymorphism)
# class Human:
#     def sayhello(self, name=None):
#         if name is not None:
#             print("Hello"+name)
#         else:
#             print("Hello")
# h = Human()
# h.sayhello()
# h.sayhello("Rama")

#Example11: Overloading2
class Calculation:
    def add(selfself, a=0, b=0, c=0):
        print(a + b + c)
calobj = Calculation()
calobj.add()
calobj.add(1,2,3)
calobj.add(3,4,5)






