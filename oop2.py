class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return f"Vroooom!!! I'm driving a {self.make} {self.model}"

    def stop(self):
        return "Sccrrrrrrrrr!!!"

    def play_music(self):
        return "Boom boom!!!"


class ElectricCar(Car):
    def __init__(self, make, model, year):
        Car.__init__(self, make, model, year)

    def charge(self):
        return f"I'm charging my {self.make} {self.model}"


myCar = Car("Electric Car", "Sedan", 2023)

myElectricCar = ElectricCar("Tesla", "Model Y", 2024)

print(myCar.drive())

print(myElectricCar.drive())
print(myElectricCar.charge())
