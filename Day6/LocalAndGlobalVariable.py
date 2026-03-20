#Example1
global_var = 20        #global variable

def func():
    local_var = 30     #local variable
    print(local_var)
    print(global_var)
func()

print(local_var)       #invalid because local variable is local variable of func()
print(global_var)

#Example2
xy = 100
def cool():
    xy = 200
    print(xy)          #if local and global variable are same then function will call local variable only
cool()

#Example3
ab = 100
def cool1():
    global ab
    print(ab)
cool1()                 #to use the global variable, use "global" keyword

#Example4:
x = 100
def cool2():
    global x
    x = 200
    print(x)
cool2()

#Example5:
#There is no need to declare global variables outside the function
#You can declare them global inside the function - global
def cool3():
    global x
    x = 100
    print(x)
cool3()



