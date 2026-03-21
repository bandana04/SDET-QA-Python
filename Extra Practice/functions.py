def calculate_mean(a,b):
    mean = (a+b)/2
    print(mean)
calculate_mean(1,2)
calculate_mean(3,4)

def students(name,age,height,weight):
    print("User's name :", name)
    print("User's Age :",age)
    print("User's Height :",height)
    print("User's Weight :",weight)
Name = input("Enter your name:")
Age = int(input("Enter your age:"))
Height = float(input("Enter your height:"))
Weight = float(input("Enter your weight:"))
students(Name,Age,Height,Weight)

