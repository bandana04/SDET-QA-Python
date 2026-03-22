import sys
sys.path.append('/home/bandana/Desktop/Automation/SDET QA/Day9/packA')
sys.path.append('/home/bandana/Desktop/Automation/SDET QA/Day9/packB')

# #Approach1
# import Emp
# empobj = Emp.Employee(1,"Ram", 10000)
# empobj.displayemp()
# import stu
# stuobj = stu.Student(1, "shyam", 4)
# stuobj.displaystu()

#Approach2
from Emp import Employee
empobj = Employee(101,"John",40000)
empobj.displayemp()

from stu import Student
stuobj = Student(101,"John",4)
stuobj.displaystu()




