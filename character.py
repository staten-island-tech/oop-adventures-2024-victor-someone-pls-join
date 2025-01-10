import random

# Parent class
class Character:
    def __init__(self, name):
        self.name = name
        self.stats = {}

    def generate_stats(self):
        raise NotImplementedError("Subclasses should implement this method")

    def display_character(self):
        print(f"\nCharacter: {self.name}")
        for stat, value in self.stats.items():
            print(f"{stat.capitalize()}: {value}")

# Warrior 
class barbarian(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "warrior"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (15, 25), "agility": (5, 15), "intelligence": (3, 7), "health": (100, 150), "alcholism": (0, 15)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

# Mage 
class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "mage"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (5, 10), "agility": (9, 12), "intelligence": (15, 25), "health": (60, 80), "alcholism": (0,5)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

# Archer 
class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "archer"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (10, 15), "agility": (15, 25), "intelligence": (5, 12), "health": (70, 100), "alcholism": (0,10)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

# Thief 
class Thief(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "thief"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (5, 10), "agility": (15, 25), "intelligence": (8, 15), "health": (100, 100), "alcholism": (0,10)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

def create_character():
    # Get user input for the character name and type
    name = input("Enter the character's name: ")
    char_type = input("Enter the character's type (warrior, mage, archer, thief): ").lower()

    # Create the character object based on the type
    if char_type == "barbarian":
        character = barbarian(name)
    elif char_type == "mage":
        character = Mage(name)
    elif char_type == "archer":
        character = Archer(name)
    elif char_type == "thief":
        character = Thief(name)
    else:
        print("Invalid character type!")
        return

    # Display the character
    character.display_character()

if __name__ == "__main__":
    create_character()
