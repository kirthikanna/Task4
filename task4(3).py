#FROM THW GIVEN LIST CREATE TWO CLASS METHODS AREA AND PERIMETER WHICH WILL BE GOING TO CALCULATE
#AREA AND PERIMETER
class list:
    def __init__(self,a):
        self.a=a
        self.pi=3.141
    def area(self):
        print("the area of circle of the given list is")
        for i in range(6):
            print(self.pi*self.a[i]*self.a[i])
    def perimeter(self):
        print("the perimeter of circle of the given list is")
        for i in range(6):
            print(2*self.pi*self.a[i])
b=list(a=[10,501,22,37,100,999,87,351])
print(b.area())
print(b.perimeter())