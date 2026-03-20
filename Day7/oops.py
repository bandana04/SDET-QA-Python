#Example1:
class myclass:                      #class creation
    def myfunc(self):               #self means that this function belongs to myclass class
        pass                        #pass means None
    def display(self):
        print("john")
mc1 = myclass()                     #object creation
mc1.myfunc()
mc1.display()

#or
class myclass1:
    def myfunc1(self):
        pass
    def display1(self,name):
        print(name)
mc2 = myclass1()
mc2.myfunc1()
mc2.display1("Bandana")

#Example2
class myclass2:
    def m1(self):
        print("This is instance method")
    @staticmethod
    def m2(self,num):
        print(num)
mc3 = myclass2()
mc3.m1()
mc3.m2(10,20)
myclass2.m2(100,200)




