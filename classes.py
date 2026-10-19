
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


class Dog:  # noqa: F811
    species = "Canis familiaris"  # shared by all dogs (class attribute)

    def __init__(self, name, age):
        self.name = name        # unique per dog (instance attribute)
        self.age = age          # goes through the setter below

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value

    def bark(self):
        return f"{self.name} says woof!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"


print(Dog.species)              # Canis familiaris
try:
    Dog("Ghost", -1)
except ValueError as e:
    print("Error:", e)          # Error: age cannot be negative



class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)  # reuse the parent's setup
        self.toy = toy

    def bark(self):  # overrides Dog.bark
        return f"{self.name} says yip yip!"

    def play(self):
        return f"{self.name} plays with {self.toy}"


pup = Puppy("Biscuit", 1, "ball")
print(pup.bark())                    # Biscuit says yip yip!
print(pup.play())                    # Biscuit plays with ball
print(isinstance(pup, Dog))          # True
