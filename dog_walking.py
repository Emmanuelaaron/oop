class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs
    
    def walk(self):
        for dog in self.dogs:
            print (dog.walk())

class Dog:
    species = "mammals"
    def __init__(self, name, age, is_hungry=True):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def eat(self):
        is_hungry = False

    def walk(self):
        return (f"{self.name} is walking")
        
class Sniffer(Dog): #inherits from dog class
    def __init__(self, name, age):
        super().__init__(name, age)

class Bulldog(Dog): #inherits from dog class
    def __init__(self, name, age):
        super().__init__(name, age)

class Hunter(Dog): #inherits from dog class
    def __init__(self, name, age):
        super().__init__(name, age)

Tom = Sniffer("Tom", 6)
Fletcher = Bulldog("Fletcher", 7)
Larry = Hunter("Larry", 9)

my_dogs = [Tom, Fletcher, Larry]

my_pets = Pets(my_dogs)

my_pets.walk()