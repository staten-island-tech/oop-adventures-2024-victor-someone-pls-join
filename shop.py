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
                print(f"\nYou bought {item} for {price} gold, you have {self.gold} left")
            else:
                print("\nYou don't have enough gold for that item.")
        else:
            print("\nInvalid item.")

    def open_shop(self):
        """Open the shop, allowing the user to interact with it."""
        while True:
            self.show_balance()  # Show the player's balance
            self.show_items()    # Show available items

            print("\nEnter the name of the item you want to buy (or 'q' to quit):")
            choice = input("Your choice: ").strip().lower()

            if choice == 'q':
                print("\nExiting the shop. Thank you for visiting!")
                break
            
            else:
                matched_item = None
                for item in self.items:
                    if choice == item.lower(): 
                        matched_item = item
                        break

                if matched_item:
                    self.buy_item(matched_item)
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



# else:
#                 # Normalize the choice input to match item names (case insensitive)
#                 matched_item = None
#                 for item in self.items:
#                     if choice == item.lower():  # Match user input with lowercased item names
#                         matched_item = item
#                         break

#                 if matched_item:
#                     self.buy_item(matched_item)  # Call buy_item with the correctly cased item name
#                 else:
#                     print("\nInvalid choice. Please try again.")