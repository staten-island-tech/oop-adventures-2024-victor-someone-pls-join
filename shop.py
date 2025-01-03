class Shop:
    def __init__(self):
        self.items = {
            "Beer": 10,       # Beer costs 10 gold
            "Pork": 20,       # Pork costs 20 gold
            "Chicken": 15,    # Chicken costs 15 gold
            "Beef": 25        # Beef costs 25 gold
        }
        self.gold = 50      # Starting gold

    def show_balance(self):
        """Show the player's current gold balance."""
        print(f"\nYou have {self.gold} gold.\n")

    def show_items(self):
        """Show available items with their prices."""
        print("Available items for purchase:")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

    def buy_item(self, item):
        """Handle the purchase of an item."""
        if item in self.items:
            price = self.items[item]
            if self.gold >= price:
                self.gold -= price
                print(f"\nYou bought {item} for {price} gold!")
            else:
                print("\nYou don't have enough gold for that item.")
        else:
            print("\nInvalid item.")

    def open_shop(self):
        """Open the shop, allowing the user to interact with it."""
        while True:
            self.show_balance()  # Show the player's balance
            self.show_items()    # Show available items

            print("\nEnter the number of the item you want to buy (or 'q' to quit):")
            choice = input("Your choice: ").strip().lower()

            if choice == 'q':
                print("\nExiting the shop. Thank you for visiting!")
                break

            item_map = {
                'beer': 'Beer',
                'pork': 'Pork',
                'chicken': 'Chicken',
                'beef': 'Beef'
            }

            if choice in item_map:
                self.buy_item(item_map[choice])
            else:
                print("\nInvalid choice. Please try again.")

def main():
    # Create the shop instance
    shop = Shop()

    # Wait for the user to press '0' to open the shop
    print("Press '0' to open the shop.")
    while True:
        key = input("Press '0' to open the shop: ").strip()
        if key == '0':
            shop.open_shop()  # Open the shop
            break  # Exit after the shop interaction

if __name__ == "__main__":
    main()
