class Parent:
    def __init__(self, age, height, name):
        self.__age = age
        self.__height = height
        self.name = name

    def eat(self):
        return 'I love food!'

    def drive(self):
        return 'I drive a Probox!'

    def start(self, car):
        car.drive()


class Child(Parent):
    def __init__(self, age, height, name):
        Parent.__init__(self, age, height, name)
        self.age = age
        self.height = height


myParent = Parent(29, 169, "Jack Doe")

myChild = Child(20, 165, "John Doe")

# print(myParent.age)
# print(myParent.height)
print(myParent.name)
print(myParent.eat())
print(myParent.start(myParent))

print(myChild.drive())
