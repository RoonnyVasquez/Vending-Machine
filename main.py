import sys

# 1. Define the Beverage class
class Beverage:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_quantity(self):
        """Decrements the quantity by one after a successful vend."""
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def is_available(self):
        """Checks if the beverage is in stock."""
        return self.quantity > 0

# 2. Define the Vending Machine class
class VendingMachine:
    def __init__(self, inventory):
        self.inventory = inventory
        # Map item numbers to beverage objects for easy selection
        self.menu_map = {str(i + 1): item for i, item in enumerate(self.inventory)}

    def display_menu(self):
        """Displays the current menu and item codes to the user."""
        print("\n--- Welcome to the Vending Machine ---")
        print("Please make a selection:")
        for i, beverage in enumerate(self.inventory):
            status = "In Stock" if beverage.is_available() else "Out of Stock"
            print(f"[{i + 1}] {beverage.name:<15} - ${beverage.price:.2f} ({status})")
        print("[0] Exit the machine")
        print("--------------------------------------")

    def get_selection(self):
        """Prompts the user for a selection and validates the input."""
        while True:
            choice = input("Enter the number of your choice (0 to exit): ").strip()
            if choice == '0':
                print("Exiting the vending machine. Goodbye!")
                sys.exit()
            if choice in self.menu_map:
                selected_item = self.menu_map[choice]
                if selected_item.is_available():
                    return selected_item
                else:
                    print(f"Sorry, {selected_item.name} is out of stock. Please select another item.")
            else:
                print("Invalid selection. Please enter a valid number from the menu.")

    def collect_payment(self, beverage):
        """Manages the payment process for a selected beverage."""
        required_amount = beverage.price
        amount_paid = 0.0
        print(f"The price for {beverage.name} is ${required_amount:.2f}.")

        while amount_paid < required_amount:
            try:
                # Prompt the user to insert money incrementally
                money = float(input(f"Insert money (Remaining: ${required_amount - amount_paid:.2f}): $").strip())
                if money <= 0:
                    print("Please insert a positive amount.")
                    continue
                amount_paid += money
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")

        # Calculate and return change
        change = amount_paid - required_amount
        return change

    def vend_item(self, beverage, change):
        """Vends the item and dispenses change."""
        if beverage.decrease_quantity():
            print(f"\n<<< Vending {beverage.name}. Enjoy! >>>")
            if change > 0:
                print(f"<<< Your change is ${change:.2f}. >>>")
        else:
            # This case should ideally not be reached if checks are working
            print("Error: Could not vend item. Item might be out of stock.")

    def run(self):
        """The main loop for the vending machine operation."""
        while True:
            self.display_menu()
            selected_beverage = self.get_selection()
            change = self.collect_payment(selected_beverage)
            self.vend_item(selected_beverage, change)
            print("\nTransaction complete. Returning to main menu...")

# 3. Initialize the vending machine and run the simulation
if __name__ == "__main__":
    # Create the 6 initial beverage objects
    coke = Beverage("Coke", 1.50, 5)
    diet_coke = Beverage("Diet Coke", 1.50, 3)
    sprite = Beverage("Sprite", 1.25, 10)
    water = Beverage("Water", 1.00, 20)
    dr_pepper = Beverage("Dr Pepper", 1.75, 5)
    fanta = Beverage("Fanta", 1.25, 0) # Example of an out-of-stock item

    # Load the beverages into the vending machine
    beverage_inventory = [coke, diet_coke, sprite, water, dr_pepper, fanta]
    machine = VendingMachine(beverage_inventory)

    # Start the simulation loop
    machine.run()
