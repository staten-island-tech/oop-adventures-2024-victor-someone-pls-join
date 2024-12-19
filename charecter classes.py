# charecter creator and stat generator
import random

# class charecters():
#     def __init__(self, character_types):
#         self.character_types = character_types
#     character_types = {
#     "warrior": {"strength": (10, 20), "agility": (5, 15), "intelligence": (3, 7)},
#     "mage": {"strength": (3, 8), "agility": (5, 12), "intelligence": (15, 25)},
#     "archer": {"strength": (5, 15), "agility": (10, 20), "intelligence": (5, 12)},
#     "thief": {"strength": (5, 10), "agility": (13, 20), "intelligence": (8, 15)},
# }

# def generate_stats(character_type):
#     if character_type not in character_type:
#         print("Invalid")
#         return None
    
#     stats = {}
#     for stat, (min_value, max_value) in character_type[character_type].items():
#         stats[stat] = random.randint(min_value, max_value) 
#     return stats

# def create_character():
#     name = input("Enter the character's name: ")
#     char_type = input("Enter the character's type (warrior, mage, archer, thief): ").lower()
    
#     stats = generate_stats(char_type)
    
#     if stats: 
#         print(f"\nCharacter: {name}")
#         print(f"Type: {char_type.capitalize()}")
#         for stat, value in stats.items():
#             print(f"{stat.capitalize()}: {value}")
#     else:
#         print("Please enter a valid character type.")

# if __name__ == "__main__":
#     create_character()











# import json
# import os



# import random
# cookie = input("charecter name:")
# alcholism = {"alcholism": (0,11)}
# class merchant():
#     def __init__(self, cookie, alcholism):
#         self.cookie = cookie
#         self.alcholism = alcholism

#         alcholism = {}
#         for key, (min_value, max_value) in self.alcholism.items():
#             self.alcholism[key] = random.randint(min_value, max_value) 

# newmerchant = merchant(cookie, alcholism)

# print(newmerchant.cookie)



# with open("./json/data.json", "r") as f:
#     # Serialize the updated Python list to a JSON string
#     data = json.load(f)
#     ##Call classes in here
#     data.append(newmerchant.__dict__)

# #No code needed below this line
# # Creates a new JSON file with the updated data
# new_file = "updated.json"
# with open(new_file, "w") as f:
#     # Serialize the updated Python list to a JSON string
#     json_string = json.dumps(data)

#     # Write the JSON string to the new JSON file
#     f.write(json_string)

# # Overwrite the old JSON file with the new one
# os.remove("data.json")
# os.rename(new_file, "data.json")






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

# Warrior subclass
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "warrior"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (10, 20), "agility": (5, 15), "intelligence": (3, 7), "health": (100, 150)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

# Mage subclass
class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "mage"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (3, 8), "agility": (9, 12), "intelligence": (15, 25), "health": (60, 80)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

# Archer subclass
class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "archer"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (5, 15), "agility": (15, 25), "intelligence": (5, 12), "health": (70, 100)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

# Thief subclass
class Thief(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_type = "thief"
        self.generate_stats()

    def generate_stats(self):
        character_types = {"Dmg": (5, 10), "agility": (13, 20), "intelligence": (8, 15), "health": (100, 100)}
        self.stats = {stat: random.randint(min_val, max_val) for stat, (min_val, max_val) in character_types.items()}

def create_character():
    # Get user input for the character name and type
    name = input("Enter the character's name: ")
    char_type = input("Enter the character's type (warrior, mage, archer, thief): ").lower()

    # Create the character object based on the type
    if char_type == "warrior":
        character = Warrior(name)
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
