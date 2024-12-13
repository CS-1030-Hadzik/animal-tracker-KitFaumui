
from animal import Animal 
"""
    Derived class representing a dog, which is a type of Animal.
    """
    # TODO: Initialize the Dog class and add the breed attribute.
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    # The constructor should accept name, species, and breed as parameters
    # TODO: Override the __str__ method to include the breed.
    # Example output:
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    def __str__(self):
        return f"Kingdom: 'Animalia', Name: '{self.name}', Species: '{self.species}', Breed: '{self.breed}'"
    
    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.
    def speak(self):
        return "The dog barks."
dog_instance = Dog(name="Buddy", species="Canine", breed="Golden Retriever")

print(dog_instance.speak())
