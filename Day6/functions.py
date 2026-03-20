#Example1 : Function doesn't take arguments, doesn't return any value
def myfunc():                #declaration of function
    print("Hello World")
myfunc()                     #calling the function

#Example2 : Function takes arguments but doesn't return value
def myfunc1(name):           #declaration of function
    print("Hello ", name)
myfunc1("Bandana")           #calling the function with value

#Example3 : Function takes arguments and also returns value
def myfunc2(a,b):
    return (a+b)
sum = myfunc2(10,20)
print(sum)

#Example4 : Returns None value
def func():
    return
print(func())                 #will return None

def func1():
    i = 10
print(func1())                #will return None

#Example5: Function doesn't take arguments but returns some value
def get_number():
    return 10
result = get_number()
print(result)






