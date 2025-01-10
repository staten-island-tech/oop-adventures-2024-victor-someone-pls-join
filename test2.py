class Player:
    def __init__(self, name):
        self.name = name
        self.health = 0  # Starting health
        self.gold = 1000     # Starting gold

    def heal(self, amount):
        """Heals the player by a certain amount."""
        self.health += amount
        if self.health > 100:
            self.health = 100  # Max health cap
        print(f"\n{self.name} healed for {amount} points. Current health: {self.health}")

    def show_status(self):
        """Show the player's current health and gold."""
        print(f"\n{self.name} - Health: {self.health}, Gold: {self.gold}")

class Shop:
    def __init__(self, player):
        self.items = {
            "Beer": 5,       # Beer costs 10 gold
            "Pork": 20,       # Pork costs 20 gold
            "Chicken": 15,    # Chicken costs 15 gold
            "Beef": 25,        # Beef costs 25 gold
            "turducken": 100  # turducken costs 100 gold
        }
        self.player = player  # Reference to the player instance

    def show_balance(self):
        """Show the player's current gold balance."""
        print(f"\nYou have {self.player.gold} gold.\n")

    def show_items(self):
        """Show available items with their prices."""
        print("Available items for purchase:")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

    def buy_item(self, item):
        """Handle the purchase of an item."""
        if item in self.items:
            price = self.items[item]
            if self.player.gold >= price:
                self.player.gold -= price
                print(f"\nYou bought {item} for {price} gold, you have {self.player.gold} gold left.")

                # If the item is food, heal the player
                if item in ["Pork", "Chicken", "Beef", "Beer", "Turducken"]:
                    heal_amount = {"Pork": 15, "Chicken": 10, "Beef":20 , "Beer": 20, "Turducken": 100}.get(item, 1)
                    self.player.heal(heal_amount)
            else:
                print("\nYou don't have enough gold for that item.")
        else:
            print("\nInvalid item.")

    def open_shop(self):
        """Open the shop, allowing the user to interact with it."""
        while True:
            self.player.show_status()  # Show the player's balance and health
            self.show_items()    # Show available items

            print("\nEnter the name of the item you want to buy (or 'q' to quit):")
            choice = input("Your choice: ").strip().lower()

            if choice == 'q':
                print("\nExiting the shop. Thank you for visiting!")
                break
            
            else:
                matched_item = None
                for item in self.items:
                    if choice == item.lower():  # Match user input with lowercased item names
                        matched_item = item
                        break

                if matched_item:
                    self.buy_item(matched_item)
                else:
                    print("\nInvalid choice. Please try again.")

def main():
    # Create the player instance
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    # Create the shop instance
    shop = Shop(player)

    # Wait for the user to press '0' to open the shop
    print("Press '0' to open the shop.")
    while True:
        key = input("Press '0' to open the shop: ").strip()
        if key == '0':
            shop.open_shop()  # Open the shop
            break  # Exit after the shop interaction

if __name__ == "__main__":
    main()

