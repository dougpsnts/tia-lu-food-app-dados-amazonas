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
        else: 
            self.stock += quantity

    def update_name(self):
        confirm = input(f"You are about to change the name of the product {self.name}\n( 1. Yes / 2. No ) ")
        if confirm == "1":
            new_name = input("Type the new name: ")
            self.name = new_name
            print(f"The name of the item code:{self.code} has changed to {self.name}")
        else:
            print("Operation canceled")
            return
    
    def update_description(self):
        print(f"Current description:\n{self.description}")
        new_description = input("Type a new description: ")
        confirm = input(f"You are about to change the description of the product {self.name}\n( 1. Yes / 2. No ) ")
        if confirm == "1":
            self.description = new_description
            print(f"Description of the item {self.name} has changed")
        else:
            print("Operation canceled")
            return
            

    def __repr__(self):
        return f"Item code= {self.code}\nname= {self.name}\ndescription= {self.description}\nprice= {self.price}\nstock= {self.stock}\n"
    
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        elif item.stock < quantity:
            raise ValueError("Insufficient stock for the requested item.")
        else: 
            item.update_stock(-quantity)
            self.items.append((item, quantity))

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def __repr__(self):
        return f"Order(items={self.items})"
    
catalog = []

def manage_menu_items(catalog):

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
                code = len(catalog) + 1
                name = input("Type a new item name:\n")
                description = input("Type a description:\n")
                price = float(input("Type the new item`s price: \nEx: 8.00 / 12.50\n"))
                stock = int(input("How many items will be add:\n"))
                new_item = Item(code, name, description, price, stock)
                catalog.append(new_item)
            case "2":
                item = input("Type the name of the item:\n")
                for i in catalog:
                    if i.name == item:
                        update_type = ""
                        while update_type != "5":
                            print("1. Update item`s name")
                            print("2. Update item`s description")
                            print("3. Update item`s price")
                            print("4. Update item`s quantity")
                            print("5. Back to previous menu")
                            update_type = input("Choose an option (1 / 2 / 3 / 4 / 5): ")
                        
                            match update_type:
                                case "1":
                                    i.update_name()
                                case "2":
                                    i.update_description()
                                case "3":
                                    print("Test option 3")
                                case "4":
                                    print(f"The item {i.name} has {i.stock} units in stock.")
                                    quantity = int(input("Type the new quantity you want to add or take from stock:\n Use a minus sign (-) decrease stock\n"))
                                    try:
                                        i.update_stock(quantity)
                                        print(f"Stock updated. New stock for {i.name}: {i.stock}")
                                    except ValueError as e:
                                        print(e)
                                case "5":
                                    return
                                case _:
                                    print("Invalid option. Please try again.")
                    else:
                        print("Item not found. Please try again.")
            case "3":
                for i in catalog:
                    print(i)
            case "4":
                print("Returning to Main Menu.")
                return
            case _:
                print("Invalid option. Please try again.")


def main_menu():

    choice = ""
    while choice != "3":
        print("Welcome to the Food Delivery Ordering System!")
        print("1. Manage Menu Items")
        print("2. Manage orders")
        print("3. Exit")
        choice = input("Chose an option(1 / 2 / 3): ")

        match choice:
            case "1":
                manage_menu_items(catalog)
            case "2":
                print("test manage orders")
            case "3":
                print("Exiting the system. Goodbye!")
                return
            case _:
                print("Invalid option. Please try again.")

main_menu()

    

