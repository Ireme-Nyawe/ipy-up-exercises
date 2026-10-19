
class Dog:
    def __init__(self, name, age):
        # self refers to the specific object being created
        self.name = name
        self.age = age


dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name, dog1.age)  # Rex 3
print(dog2.name, dog2.age)  # Bella 5

