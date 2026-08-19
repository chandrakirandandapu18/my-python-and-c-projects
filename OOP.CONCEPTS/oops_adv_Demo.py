class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Cat meows")


dog = Dog("Bruno", "Labrador")
cat = Cat("Kitty", "White")

print("Dog Name:", dog.name)
print("Breed:", dog.breed)
dog.sound()

print()

print("Cat Name:", cat.name)
print("Color:", cat.color)
cat.sound()
