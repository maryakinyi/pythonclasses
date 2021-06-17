x=[100,110,120,130,140,150]
for y in x:
        z=y*5
        print(z)

def divisible_by_three(n):
        if n%3==0:
                print(n)

def  greet():
        students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
        for keys in students:
                print(f"Hello, ")
def list():
        x = ['a','b','a','e','d','b','c','e','f','g','h']
        y=x.remove("b")
def divisible_by_7():
        for number in range(100,200):
                if number%7==0:
                        print(number)
class Rectangle:
        def __ini__(self,width,length):
                self.width=width,
                self.length=length,
        def area(self,length,width):
                A=length*width
                return  A
        def perimeter(self,length,width):
                P=2(length+width)
                return P