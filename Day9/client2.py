import sys
sys.path.append("/home/bandana/Desktop/Automation/SDET QA/Day9/package1")
sys.path.append("/home/bandana/Desktop/Automation/SDET QA/Day9/package1/Package2")

# #Approach1
# import module1
# import module2
# module1.display()
# module2.show()

#Approach2
from module1 import *
from module2 import *
display()
show()