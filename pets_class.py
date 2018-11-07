class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs

class Dog:
    species = "mammals"
    def __init__(self, name, age, is_hungry=True):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def eat(self):
        is_hungry = False
        
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

print (f"I have {len(my_pets.dogs)} dogs")

for dog in my_pets.dogs:
    print (f"{dog.name} is {dog.age}")

print(f"And they are all {dog.species}, of course")

all_are_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        all_are_hungry = True

if all_are_hungry:
    print("My dogs are hungry")
else:
    print ("My dogs are not hungry")