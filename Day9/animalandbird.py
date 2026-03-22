# #Approach1
# import animal
# import birds
#
# animal.fly()
# animal.color()
#
# birds.fly()
# animal.color()

# #Approach2
# from animal import *
# from birds import *
# fly()
# color()                  #This way, functions will be called from birds only

#Approach2
from animal import *
fly()
color()
from birds import *
fly()
color()


