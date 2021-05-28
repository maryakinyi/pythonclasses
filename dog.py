class Dog:
    def __init__(self,color,name,age):
        self.color=color
        self.name=name
        self.age=age
    def  bark(self):
        return f"The {self.color},{self.name} is today {self.age} old"
