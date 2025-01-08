import charecter classes


def take_damage(self, damage):
        """Reduces health by the damage taken."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        """Returns True if the character is alive (health > 0)."""
        return self.health > 0

    def attack(self, enemy):
        """Attacks the enemy and reduces its health."""
        print(f"{self.name} attacks {enemy.name} for {self.dmg} damage!")
        enemy.take_damage(self.dmg)

    def display_status(self):
        """Displays the current status (health) of the character."""
        print(f"{self.name} has {self.health} health remaining.")

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        # Show player and enemy health
        player.display_status()
        enemy.display_status()

        # Player's turn to attack
        action = input(f"Do you want to attack {enemy.name}? (yes/no): ").lower()
        if action == "yes":
            player.attack(enemy)
        else:
            print(f"{player.name} chooses not to attack.")

        # Check if enemy is alive
        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy's turn to attack
        if enemy.is_alive():
            print(f"{enemy.name} attacks {player.name}!")
            enemy.attack(player)

        # Check if player is alive
        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break

# Example usage
player = Character(name="Hero", health=100, dmg=20)
enemy = Character(name="Goblin", health=50, dmg=10)

# Start battle
battle(player, enemy)
