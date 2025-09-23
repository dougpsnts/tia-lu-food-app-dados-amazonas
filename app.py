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
        confirm = input(f"You are about to change the name of the product {self.name}\n(Confirm? 1. Yes / 2. No ) ")
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
        confirm = input(f"You are about to change the description of the product {self.name}\n(Confirm? 1. Yes / 2. No ) ")
        if confirm == "1":
            self.description = new_description
            print(f"Description of the item {self.name} has changed")
        else:
            print("Operation canceled")
            return

    def update_price(self):
        print(f"Current price:\n{self.price}")  
        new_price = input("Type a new price: ")
        confirm = input(f"You are about to change the price of the product {self.name} to R${new_price}\n(Confirm? 1. Yes / 2. No ) ")
        if confirm == "1":
            self.price = new_price
            print(f"Price of the item {self.name} has changed to R${self.price}")
        else:
            print("Operation canceled")
            return

    def __repr__(self):
        return f"\nItem code: {self.code}\nname: {self.name}\ndescription: {self.description}\nprice: R${self.price}\nstock: {self.stock}\n"
    
class Order:
    def __init__(self, code, costumer, items_order=[], status="Pending", payment="Paid"):
        self.code = code 
        self.costumer = costumer
        self.items_order = items_order
        self.status = status
        self.payment = payment
        self.order_total_price = None

    def total_price(self):
        return sum(item.price for item in self.items_order)

    def apply_discount(self):
        if not self.items_order:
            raise ValueError("It's not possible to apply discount in a empty order.")
        discount_value = self.total_price() * (10 / 100)
        self.order_total_price = self.total_price() - discount_value
        return self.order_total_price

    def finalize(self):
        if self.order_total_price is None:
            self.order_total_price = self.total_price()
        return self.order_total_price
        
    def __repr__(self):
        total = self.order_total_price if self.order_total_price is not None else self.total_price()
        items_list = ", ".join(item.name for item in self.items_order) if self.items_order else "No items"
        return (
            f"\n📦 Order: {self.code}\n"
            f"👤 Costumer: {self.costumer}\n"
            f"🛒 Items: {items_list}\n"
            f"💰 Total: R${total:.2f}\n"
            f"📌 Status: {self.status}\n"
        )
   
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
                print('Item added with sucess')
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
                                    i.update_price()
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
                if not catalog:
                    print("⚠️ No items on the menu.")
                    continue

                print("\n📋 Menu list of items:")
                print("-" * 40)
                for item in catalog:
                    print(f"📦 Code: {item.code}")
                    print(f"📝 Name: {item.name}")
                    print(f"🖊️ Description: {item.description}")
                    print(f"💰 Price: R${item.price:.2f}")
                    print(f"📦 Stock: {item.stock}")
                    print("-" * 40)

            case "4":
                print("Returning to Main Menu.")
                return
            case _:
                print("Invalid option. Please try again.")

all_orders = []

def get_orders_by_status(status):
    return [o for o in all_orders if o.status == status]

def manage_orders(all_orders, catalog):
    choice = ""
    while choice != "5":
        print("\nMenu Orders Management")
        print("1. Create a new Order")
        print("2. Manage Pending Orders")
        print("3. Update Orders Status")
        print("4. Cancel Order")
        print("5. Return to main menu")
        choice = input("Chose an option(1 / 2 / 3 / 4 / 5): ")
        
        match choice:
            case "1":
                code = len(all_orders) + 1
                costumer = input('\nWhat is the name of the costumer? ')
                items_order = []
                status = "" 
                payment = 'Paid'
                order = Order(code, costumer, items_order, status, payment)
                choice = ""
                while choice != "3":
                    print('1. Insert a new item')
                    print('2. Finish order')
                    print('3. Cancell order creation')
                    choice = input('\nChoose an option (1 / 2 / 3): ')

                    match choice:
                        case "1":
                            if catalog == []:
                                print('The menu is empty, please add some items to proceed.')
                                return
                            
                            print("\n📋 Menu list of items:")
                            print("-" * 40)
                            for item in catalog:
                                print(f"📦 Code: {item.code}")
                                print(f"📝 Name: {item.name}")
                                print(f"🖊️ Description: {item.description}")
                                print(f"💰 Price: R${item.price:.2f}")
                                print(f"📦 Stock: {item.stock}")
                                print("-" * 40)
                            catalog_code = int(input('Choose a item by code: '))

                            for item in catalog:
                                if item.code == catalog_code and item.stock > 0:
                                    print(f'\nItem {catalog_code} added with sucess')
                                    items_order.append(item)
                                    print(f'\n{costumer}`s order items are: {[i.name for i in items_order]}')
                                    item.update_stock(-1)
                                    print(f'The current stock for this item is: {item.stock}')
                                    print(f"\nAdded {item.name} with price R${item.price:.2f}")

                                    
                                elif catalog_code != item.code:
                                    print('Item not found')  ##### ainda está retornando item not found mesmo quando está com estoque e o codigo esta correto. ######
                                    break

                                elif item.stock <= 0:
                                    print('Stock insuficient')
                                    print(f'The current stock for this item is: {item.stock}\n')
                                    break
                                else:
                                    print('Verify informations.')
                            
                        case "2":
                            if len(items_order) == 0:
                                print("Order must have at least one item!")
                                continue

                            print(f"The current value of the order is: R${order.total_price():.2f}")

                            discount_choice = input("Would you like to apply a discount coupon of 10%? (1. Yes / 2. No): ")

                            match discount_choice:
                                case "1":
                                    order.apply_discount() 
                                    print(f"\nCoupon applied successfully. New total: R${order.order_total_price:.2f}")
                                case "2":
                                    order.finalize()  
                                    print(f"\nNo discount applied. Total: R${order.order_total_price:.2f}")
                                case _:
                                    print("Invalid option. Proceeding without discount.")
                                    order.finalize()

                            order.status = "Pending"
                            all_orders.append(order)

                            print("\n✅ Order added with sucess!")
                            print("-" * 40)
                            print(f"Code: {order.code}")
                            print(f"Costumer: {order.costumer}")
                            print(f"Items: {', '.join([item.name for item in order.items_order])}")
                            print(f"Status: {order.status}")
                            print(f"Total: R${order.order_total_price:.2f}")
                            print("-" * 40)
                            print("\nReturning to manage orders.\n")
                            break 
                        
                        case "3":
                            print("Cancelling order creation.")
                            break
                            
                        case _:
                            print("Invalid option. Please try again.")
                            continue
            case "2":
                pending_orders = get_orders_by_status("Pending")
                if not pending_orders:
                    print("No pending orders.")
                    continue
                
                order = pending_orders[0]
                print("\n📦 Pending Order:")
                print(order)

                print("1. Accept order")
                print("2. Reject order")
                print("3. Return to manage orders")
                choice = input("Choose an option (1 / 2 / 3): ")

                if choice == "1":
                    order.status = "Accepted"
                    print("\n✅ Order accepted with sucess!")
                    print(order)

                elif choice == "2":
                    order.status = "Rejected"
                    print("\n❌ Order rejected.")
                    print(order)                        

                elif choice == "3":
                    print("Returning to manage orders.")
                    
                else:
                    print("Invalid option.") 
                            

            case "3":
                if not all_orders:
                    print("⚠️ No avaliable order for update.")
                    continue

                print("\n📋 Orders avaliables:")
                for idx, order in enumerate(all_orders, start=1):
                    print(f"{idx}. Código: {order.code} | Cliente: {order.costumer} | Status: {order.status}")

                try:
                    order_index = int(input("\nSelect a order by code: ")) - 1
                    order = all_orders[order_index]
                except (ValueError, IndexError):
                    print("❌ Invalid Selection.")
                    continue

                print("\n📦 Selected order:")
                print(order)

                print("🔄 Choose the new status:")
                print("1. Accepted")
                print("2. Making")
                print("3. Ready")
                print("4. Waiting Delivery")
                print("5. Delivering")
                print("6. Delivered")
                print("7. Canceled")
                print("8. Rejected")

                status_choice = input("Choose an option (1-8): ")

                if status_choice == "1":
                    order.status = "Accepted"
                elif status_choice == "2":
                    order.status = "Making"
                elif status_choice == "3":
                    order.status = "Ready"
                elif status_choice == "4":
                    order.status = "Waiting Delivery"
                elif status_choice == "5":
                    order.status = "Delivering"
                elif status_choice == "6":
                    order.status = "Delivered"
                elif status_choice == "7":
                    order.status = "Canceled"
                elif status_choice == "8":
                    order.status = "Rejected"
                else:
                    print("❌ Invalid option.")
                    continue

                print("\n✅ Order updated with sucess!")
                print(order)

            case "4":
                if not all_orders:
                    print("⚠️ No orders avaliable.")
                    continue

                cancellable_orders = [o for o in all_orders if o.status in ("Pending", "Accepted")]

                if not cancellable_orders:
                    print("⚠️  No orders avaliable for cancelling.")
                    continue

                print("\n📋 Orders avaliable for cancelling:")
                for idx, order in enumerate(cancellable_orders, start=1):
                    print(f"{idx}. Code: {order.code} | Costumer: {order.costumer} | Status: {order.status}")

                try:
                    order_index = int(input("\nSelecione a order by code: ")) - 1
                    order = cancellable_orders[order_index]
                except (ValueError, IndexError):
                    print("❌ Invalid selection.")
                    continue

                print("\n📦 Selected order:")
                print(order)

                print("❗ Choose action:")
                print("1. Cancel order")
                print("2. Exit")
                cancel_choice = input("Choose an option (1 / 2): ")

                if cancel_choice == "1":
                    order.status = "Canceled"
                    print(f"\n✅ Order {order.code} canceled with sucess!")
                    print(order)
                elif cancel_choice == "2":
                    print("🔙 Returning to menu orders.")
                    continue
                else:
                    print("❌ Invalid option.")
                    continue

            case "5":
                print("Returning to Main Menu.")
                return
            case _:
                print("Invalid option. Please try again.")

def main_menu():

    choice = ""
    while choice != "3":
        print("\nWelcome to the Food Delivery Ordering System!")
        print("1. Manage Menu Items")
        print("2. Manage orders")
        print("3. Exit")
        choice = input("Chose an option(1 / 2 / 3): ")

        match choice:
            case "1":
                manage_menu_items(catalog)
            case "2":
                manage_orders(all_orders, catalog)
            case "3":
                print("Exiting the system. Goodbye!")
                return
            case _:
                print("Invalid option. Please try again.")

main_menu()

# comentarios:

# O documento pede para criar uma seção de relatorio diario. mas para isso precisaria colocar data nos pedidos.
# seria bom ter uma seção de filtrar pedidos. Tendo opção: todos os pedidos | filtrar pedidos por status