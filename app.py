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
        return f"\nItem code: {self.code}\nname: {self.name}\ndescription: {self.description}\nprice: R${self.price}\nstock: {self.stock}\n"
    
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

all_orders = []
pending_orders = []
accepted_orders = []
making_orders = []
ready_orders = []
waiting_delivery_orders = []
delivering_orders = []
delivered_orders = []
canceled_orders = []
rejected_orders = []

def manage_orders(orders):
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
                print(catalog)
                choice = ""
                code = len(orders) + 1
                status = 'Waiting Aproval' 
                costumer = input('\nWhat is the name of the costumer? ')
                items_order = []
                payment = 'Paid'
                #order = [f"Code: {code} / Costumer: {costumer} / Items: {items_order} / Status: {status}  / Payment: {payment}"]
                order = [code, costumer, items_order, status, payment]
                #discount = total_price * 0,10
                while choice != 3:
                    print('1. Insert a new item')
                    print('2. Finish order')
                    print('3. Return to menu')
                    choice = input('\nChoose an option (1 / 2 / 3): ')

                    match choice:
                        case "1":
                            catalog_code = int(input('Choose a item by code: '))
                             #criar uma condição para que só possa escolher um numero do tamanho do array.
                             #mostrar catalogo novamente
                            for item in catalog:
                                if item.code == catalog_code and item.stock > 0:
                                    print(f'\nItem {catalog_code} added with sucess')
                                    items_order.append(catalog_code)
                                    print(f'\n{costumer}`s order items are: {items_order}')
                                    item.update_stock(-1)

                                    
                                elif item.code != catalog_code:
                                        print('Item not found')

                                elif item.stock <= 0:
                                    print('Stock insuficient')
                                    #exibir a quantidade de stock disponivel no futuro.
                                else:
                                    print('Verify informations.')
                            
                        case "2":
                            if len(items_order) > 0:
                                print(f'\n{costumer}`s order added with sucess.')
                                                        
                            # while choice != 2:
                            #     choice = input('\nWould you like to apply a discount cupon of 10%? ( 1. Yes / 2. No ) ')
                                
                            #     match choice:
                            #         case '1':
                            #             order.total_price = order.total_price - discount
                            #             return
                                        
                            #         case "2":
                            #             print('Cupon not applied.')
                            #             return

                                pending_orders.append(order)
                                all_orders.append(order)
                                print(f'\nResume of the order: {order}')
                                print('Returning to manage orders.') #deixar opção para manage pending orders
                                manage_orders(orders)
                            else:
                                print('\nOrder must have items!\n')
                        
                        case "3":
                            print("\nReturning to menu.")
                            return
                            
                        case _:
                            print("Invalid option. Please try again.")
            case "2":
                print("\nManaging pending order:")
                print(pending_orders[0])
                while choice != 3:
                    print('1. Accept order')
                    print('2. Reject order')
                    print('3. Return to manage orders')
                    choice = input('\nChoose an option (1 / 2 / 3): ')

                    match choice:
                        case "1":
                            print(f'Order {pending_orders[0]} accepted')
                            new_order = pending_orders.pop(0)
                            accepted_orders.append(new_order)
                            return
                           
                        case "2":
                            print(f'Order {pending_orders[0]} rejected')
                            rejected_orders.append(pending_orders[0])
                            pending_orders.pop(0)
                            #criar função para atualizar o status para rejeitado.
                            
                            print('Returning to manage orders')
                            return                       
                        
                        case "3":
                            print('Returning to manage orders')
                            return
                        
                        case _:
                            print("Invalid option. Please try again.")
                            return                      

            case "3":
                print("Printing all orders")
                print(orders)
            case "4":
                print("Printing Accepted orders")
                print(accepted_orders)
            case "5":
                print("Printing rejected orders")
                print(rejected_orders)
                
            case "6":
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
                manage_orders(all_orders)
            case "3":
                print("Exiting the system. Goodbye!")
                return
            case _:
                print("Invalid option. Please try again.")

main_menu()

    

# Para mostrar todos os pedidos
# print(all_orders)
# Para mostrar apenas os pedidos aceitos
# print(accepted_orders)
# Para mostrar apenas os pedidos rejeitados
# print(rejected_orders)
# Para mostrar apenas os pedidos prontos: 
# print(ready_orders)
# Para mostrar apenas os pedidos cancelados:
# canceled_orders()
