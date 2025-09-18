class Item:
    def __init__(self, code, name, description, price, stock):
        self.code = code
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Insufficient stock to remove the requested quantity.")
        self.stock += quantity

    def __repr__(self):
        return f"Item code= {self.code}\nname= {self.name}\ndescription= {self.description}\nprice= {self.price}\nstock= {self.stock}\n"
    
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if item.stock < quantity:
            raise ValueError("Insufficient stock for the requested item.")
        item.update_stock(-quantity)
        self.items.append((item, quantity))

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def __repr__(self):
        return f"Order(items={self.items})"
    

def manage_menu_items():

    choice = ""
    while choice != "4":
        print("\nMenu Item Management")
        print("1. Add Item")
        print("2. Update Item Stock")
        print("3. View All Items")
        print("4. Back to Main Menu")
        choice = input("Choose an option (1 / 2 / 3 / 4): ")

        match choice:
            case "1":
                print("test add item")
            case "2":
                print("test upodate stock")
            case "3":
                print("test view all items")
            case "4":
                print("Returning to Main Menu.")
                return
            case _:
                print("Invalid option. Please try again.")

def main_menu():
    choice = ""
    while choice != "3":
        print("Welcome to the Food Delivery Ordering System!")
        print("1. Manege Menu Items")
        print("2. Manage orders")
        print("3. Exit")
        choice = input("Chose an option(1 / 2 / 3): ")

        match choice:
            case "1":
                manage_menu_items()
            case "2":
                print("test manage orders")
            case "3":
                print("Exiting the system. Goodbye!")
                return
            case _:
                print("Invalid option. Please try again.")

main_menu()

    

