x=[100,110,120,130,140,150]
a=[]
for y in x:
        z=y*5
        a.append(z)

def divisible_by_three(n):
       c=range(n+1)
       d=[]
       for u in c:
        if u%3==0:
            d.append(u)
            print(d)

def  greet():
        students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
        for keys in students:
                print(f"Hello, ")
def list():
        x = ['a','b','a','e','d','b','c','e','f','g','h']
        y=x.remove("b")
        print(y)
def divisible_by_7():
        for number in range(100,200):
                if number%7==0:
                        print(number)
class Rectangle:
        def __ini__(self,width,length):
                self.width=width
                self.length=length
        def area(self):
                A=self.length*self.width
                return  A
        def perimeter(self):
                P=2(self.length+self.width)
                return P