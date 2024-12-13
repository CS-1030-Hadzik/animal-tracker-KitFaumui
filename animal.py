
class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects
    all_animals = []
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    # TODO create the initializer for Animal with name and species as attributs
        Animal.all_animals.append(self)
    # TODO: Add a method to make a generic sound 
    def speak(self):
        return "The animal makes a noise"
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""
    def speak(self):
        return "The animal makes a noise"
    # TODO __str__ method for string representation
    # Example output
    # Kingdom: 'kingdom attribute', Name: 'name attribute' Species: 'species attribute'
    def __str__(self): return f"Kingdom: 'Animalia', Name: '{self.name}', Species: '{self.species}'"
    
animal1 = Animal(name="Generic", species="Unknown")
animal2 = Animal(name="Lion", species="Panthera leo")
    
print(animal1.speak())
print(animal2.speak())
    
for animal in Animal.all_animals:
    print(animal)