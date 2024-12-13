from animal import Animal 
from dog import Dog 

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animal_instance = Animal(name="Generic", species="Unkown")
    # TODO: Print the Animal instance
    print(animal_instance)
    # TODO: Call the method to make a generic animal sound
    animal_instance.speak()
    # TODO: Create an instance of the Dog class
    dog_instance = Dog(name="Buddy", species="Canine", breed="Golden Retriever")
    # TODO: Print the Dog instance
    print(dog_instance)
    # TODO: Call the method to make the dog-specific sound
    dog_instance.speak()
    # TODO print out all the animals
    all_animals_list = Animal.all_animals
for animal in all_animals_list:
    print(animal)