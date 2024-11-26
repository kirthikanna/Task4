#CREATE PROPER MEMBER VARIABLES INSIDE THE TASK IF REQUIRED AND USE THEM WHEN NECESSARY.
#FOR EXAMPLE FOR THIS TASK CREATE A CLASS PRIVATE VARIABLE NAMED PI=3.141
class private:
    def __init__(self,r):
        self.r=r
    def area(self):
        self.__pi=3.141 #creating a private variable in class
        return self.__pi*self.r*self.r
a=private(4)
print("area of a circle by using private variable in class  is",a.area())