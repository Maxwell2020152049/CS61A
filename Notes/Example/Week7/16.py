# Inventory tracking
add_product(name, price, nutrition)
get_label(product)
get_nutrition_info(product)
increase_inventory(product, amount)
reduce_inventory(product, amount)


# Customer tracking
signup_customer(name, address)
get_greeting(customer)
get_formatted_address(customer)


# Purchase tracking
order(customer, product, quantity, cc_info)
track(order_number)
refund(order_number, reason)

# Inventory tracking
Product(name, price, nutrition)
Product.get_label()
Product.get_nutrition_info()
Product.increase_inventory(amount)
Product.reduce_inventory(amount)
Product.get_inventory_report()

# Customer tracking
Customer(name, address)
Customer.get_greeting()
Customer.get_formatted_address()
Customer.buy(product, quantity, cc_info)

# Purchase tracking
Order(customer, product, quantity, cc_info)
Order.ship()
Order.refund(reason)


# Define a new type of data
class Product:

    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self._name = name
        self._price = price
        self._nutrition_info = nutrition_info
        self._inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self._inventory += amount

    def reduce_inventory(self, amount):
        self._inventory -= amount

    def get_label(self):
        return "Foxolate Shop: " + self._name

    def get_inventory_report(self):
        if self._inventory == 0:
            return "There are no bars!"
        return f"There are {self._inventory} bars."
        
pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])

pina_bar.increase_inventory(2)



        
    