# #Example1
# print("This is starting point of the program")
# print("This is starting point of the program")
# print("This is starting point of the program")
# try:
#     print(x)
# except:
#     print("NameError exception occured")
# print("This is ending point of the program")
# print("This is ending point of the program")
# print("This is ending point of the program")

# #Example2
# print("This is starting point of the program")
# print("This is starting point of the program")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("ZeroDivisionError exception occured and handled")
# print("This is ending point of the program")

# #Example3 : Multiple except blocks - try, except else, finally
# try:
#     num1, num2 = 10, 2
#     result = num1/num2
#     print("result: ", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError")
# except NameError:
#     print("Thrown NameError")
# except TypeError:
#     print("Thrown TypeError")
# except SyntaxError:
#     print("Thrown SyntaxError")
# else:
#     print("No exceptions occured")
# finally:
#     print("Always executing")

#Example4 : Using our own exceptions
def enterage(num):
    if num<0:
        raise ValueError("The age should be a positive number")
    if num%2==0:
        print("THe age is even number")
    else :
        print("The age is odd number")
num = -1
try:
    enterage(num)
except ValueError:
    print("Value error exception occured and handled..")



