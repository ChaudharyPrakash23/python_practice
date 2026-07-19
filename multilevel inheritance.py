class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Bark!")


class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing.")

p = Puppy("Tommy")

p.eat()
p.bark()
p.play()