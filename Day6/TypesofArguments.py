#Example1
def func(i,j):
    print(i,j)
func(1,2)           #positional arguments
func(j=4,i=5)            #keyword arguments

#Example2 : default values assigned to positional arguments
def func2(i, j=10):
    print(i,j)
func2(2)

#Example3: keyword arguments
def greetings(name,greeting):
    print(greeting + " " + name)
greetings(name="Bandana",greeting="Hello")

#Example4:
def my_function(a,b,c):
    print(a,b,c)
my_function(10,20,30)     #positional arguments
my_function(a=10,b=20,c=30)        #keyword arguments
my_function(0,b=20,30)          #This will give error because positional argument must appear before any keyword argument
my_function(10,30,b=30)      #This is having logical error

#Example5:
def largest(a,b):
    if a > b:
        return a,b
    else:
        return b,a
print(largest(20,30))
