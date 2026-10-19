
class Dog:
    def __init__(self, name, age):
        # self refers to the specific object being created
        self.name = name
        self.age = age


dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name, dog1.age)  # Rex 3
print(dog2.name, dog2.age)  # Bella 5


class Dog:  # noqa: F811 (redefinition on purpose, to show the commit step)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def birthday(self):
        self.age += 1

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"


rex = Dog("Rex", 3)
print(rex.bark())   # Rex says woof!
rex.birthday()
print(rex)          # Dog(name=Rex, age=4)

