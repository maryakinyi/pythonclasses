class Car:
    color="white"
    def __init__(self,make,model,registration,mileage):
        self.make=make
        self.model=model
        self.registration=registration
        self.mileage=mileage
    def move(self):
      return f"The new { self.make},{self.color} {self.model} with registration of {self.registration} has a mileage of{self.mileage} "
    def start_engine(self):
        return f"To start the {self.make} insert the key"
    def wash_car(self):
        return f"To clean the {self.model} use clean water and detergent"
    def drive(self):
        return f"To drive {self.model} that has registration of {self.registration} you should be a trained driver. "
