from character class import character
 
def take_damage(self, damage):
    """Reduces health by the damage taken."""
    self.health -= damage
    if self.health < 0:
    self.health = 0

def is_alive(self):
    return self.health > 0

def attack(self, enemy):
    print(f"{self.name} attacks {enemy.name} for {self.dmg} damage!")
    enemy.take_damage(self.dmg)

def display_status(self):
    print(f"{self.name} has {self.health} health remaining.")

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player.display_status()
        enemy.display_status()

        action = input(f"Do you want to attack {enemy.name}? (yes/no): ").lower()
        if action == "yes":
            player.attack(enemy)
        else:
            print(f"{player.name} does not attack.")

        if not enemy.is_alive():
            print(f"{enemy.name} has perished")
            break

        if enemy.is_alive():
            print(f"{enemy.name} attacks {player.name}!")
            enemy.attack(player)

        if not player.is_alive():
            print(f"{player.name} died")
            break

player = Character(name="Hero", health=100, dmg=20)
enemy = Character(name="Goblin", health=50, dmg=10)

battle(player, enemy)
