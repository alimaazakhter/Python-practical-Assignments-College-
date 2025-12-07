from abc import ABC, abstractmethod

# ----------------------------------
# 1. Product Interface
# ----------------------------------
class ProductInterface(ABC):

    @abstractmethod
    def check_availability(self):
        pass

    @abstractmethod
    def update_stock(self, quantity):
        pass

    @abstractmethod
    def get_price(self):
        pass


# ----------------------------------
# 2. Product Base Class
# ----------------------------------
class Product(ProductInterface):

    total_products = 0   # Static variable

    def __init__(self, name, category, price, stock):
        Product.total_products += 1
        self.__product_id = Product.total_products     # Private ID
        self.name = name
        self.category = category
        self.__price = price                            # Private price
        self.__stock_quantity = stock                   # Private stock

    def update_stock(self, quantity):
        self.__stock_quantity += quantity

    def check_availability(self):
        print("Available Stock:", self.__stock_quantity)

    def get_price(self):
        return self.__price

    def reduce_stock(self, quantity):
        if quantity <= self.__stock_quantity:
            self.__stock_quantity -= quantity
            return True
        else:
            print("Insufficient stock for", self.name)
            return False

    def show_product_info(self):
        print("\nProduct ID:", self.__product_id)
        print("Name:", self.name)
        print("Category:", self.category)
        print("Price:", self.__price)
        print("Stock:", self.__stock_quantity)

    @staticmethod
    def get_total_products():
        return Product.total_products

    @classmethod
    def update_total_products(cls, value):
        cls.total_products = value


# ----------------------------------
# 3. Electronics Product
# ----------------------------------
class ElectronicsProduct(Product):

    def __init__(self, name, price, stock, warranty):
        super().__init__(name, "Electronics", price, stock)
        self.warranty_period = warranty

    def get_warranty_info(self):
        print("Warranty Period:", self.warranty_period, "years")

    # Polymorphism (extra warranty charge)
    def get_price(self):
        return super().get_price() + 500


# ----------------------------------
# 4. Clothing Product
# ----------------------------------
class ClothingProduct(Product):

    def __init__(self, name, price, stock, size, fabric):
        super().__init__(name, "Clothing", price, stock)
        self.size = size
        self.fabric = fabric

    def get_clothing_info(self):
        print("Size:", self.size)
        print("Fabric:", self.fabric)


# ----------------------------------
# 5. Abstract User Class
# ----------------------------------
class User(ABC):

    total_users = 0

    def __init__(self, name):
        User.total_users += 1
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.reduce_stock(quantity):
            self.cart.append((product, quantity))
            print(product.name, "added to cart")

    def remove_from_cart(self, product):
        for item in self.cart:
            if item[0] == product:
                self.cart.remove(item)
                product.update_stock(item[1])
                print(product.name, "removed from cart")

    def view_cart(self):
        print("\nCart Items:")
        for item in self.cart:
            print(item[0].name, "Qty:", item[1])

    @abstractmethod
    def checkout(self):
        pass

    @staticmethod
    def get_total_users():
        return User.total_users


# ----------------------------------
# 6. Regular User
# ----------------------------------
class RegularUser(User):

    def __init__(self, name):
        super().__init__(name)
        self.discount_rate = 0

    def checkout(self):
        order = Order(self, self.cart)
        order.calculate_total(self.discount_rate)
        self.cart.clear()
        return order


# ----------------------------------
# 7. Premium User
# ----------------------------------
class PremiumUser(User):

    def __init__(self, name):
        super().__init__(name)
        self.discount_rate = 10
        self.free_shipping = True

    def checkout(self):
        order = Order(self, self.cart)
        order.calculate_total(self.discount_rate)
        print("Free Shipping Applied!")
        self.cart.clear()
        return order


# ----------------------------------
# 8. Order Class
# ----------------------------------
class Order:

    total_orders = 0

    def __init__(self, user, items):
        Order.total_orders += 1
        self.order_id = Order.total_orders
        self.user = user
        self.items = items
        self.__total_amount = 0
        self.order_status = "Pending"

    def calculate_total(self, discount):
        total = 0
        for item in self.items:
            total += item[0].get_price() * item[1]

        discount_amount = total * discount / 100
        self.__total_amount = total - discount_amount

        print("\nOrder ID:", self.order_id)
        print("Customer:", self.user.name)
        print("Total Amount:", self.__total_amount)

    def update_status(self, status):
        self.order_status = status
        print("Order Status Updated:", status)

    @staticmethod
    def get_total_orders():
        return Order.total_orders


# ----------------------------------
# ✅ MAIN PROGRAM (DEDemo)
# ----------------------------------

print("\n--- PRODUCTS ---")
p1 = ElectronicsProduct("Laptop", 60000, 5, 2)
p2 = ClothingProduct("T-Shirt", 1200, 10, "L", "Cotton")

p1.show_product_info()
p2.show_product_info()

print("\n--- USERS ---")
u1 = RegularUser("Ali")
u2 = PremiumUser("Rohan")

print("\n--- SHOPPING ---")
u1.add_to_cart(p1, 1)
u1.add_to_cart(p2, 2)
u1.view_cart()

order1 = u1.checkout()
order1.update_status("Shipped")

print("\n--- PREMIUM USER SHOPPING ---")
u2.add_to_cart(p1, 1)
order2 = u2.checkout()
order2.update_status("Delivered")

print("\n--- FINAL COUNTS ---")
print("Total Products:", Product.get_total_products())
print("Total Users:", User.get_total_users())
print("Total Orders:", Order.get_total_orders())
