from typing import List
x = [100,110,120,130,140,150]
multiplied_list = [element * 5 for element in x]
print(multiplied_list)


x= [[1,2,],[3,4,],[5, 6,]]
y = []
for sublist in x:
    for num in y:
        y.append(y)

print(y)


def smallest( list ):
        num = list[ 0 ]
        for x in list:
          if x < num:
            num = x
        return num
print(smallest([3,6,8,2,4,1,5,7]))


x = ['a','b','a','e','d','b','c','e','f','g','h']
y = []
for i in x:
    if i not in y:
        y.append(i)
x = y


def divisible_by_seven():
    y=[]
    for  x in range(100, 200):
      if (x%7==0):
        y.append(str(x))
print (x)


# def student():
#     details=[{"age": 19, "name": "Eunice"},
#     {"age": 21},"name": "Agnes"},
#     {"age": 18, "name": "Teresa"},
#     {"age": 22, "name": "Asha"}],
# print(hello {name} you were born in {age-year of birth} .format(name,age))
# student()

class Rectangle():
    def __init__(self, width,length):
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2(self.length+self.width)

theRectangle = Rectangle(20, 40)
print(theRectangle.area())





