from character import Character, barbarian, Mage, Archer, Thief

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player.display_status()
        enemy.display_status()

        action = input(f"Do you want to attack {enemy.name}? (yes/no): ").lower()
        if action == "yes":
            player.attack(enemy)
        else:
            print(f"{player.name} chooses not to attack.")

        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        if enemy.is_alive():
            print(f"{enemy.name} attacks {player.name}!")
            enemy.attack(player)

        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break


def create_character():
    name = input("Enter the character's name: ")
    char_type = input("Enter the character's type (warrior, mage, archer, thief): ").lower()

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

    character.display_character()
    return character

if __name__ == "__main__":
    player = create_character()
    if player:
        battle(player, enemy)
