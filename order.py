class Product:
    def __init__(self, name, price, quantity=100):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.quantity}"

    def reduce_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return True
        return False

class Customer:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Customer Name: {self.name}")

class Order:
    # An Order NEEDS a customer and a product to exist
    def __init__(self, customer, product, quantity_ordered):
        self.customer = customer
        self.product = product
        self.quantity_ordered = quantity_ordered
        self.total_price = 0
        self.status = "Pending"
        
        self.process_order()

    def process_order(self):
        # Check if product has enough stock
        if self.product.reduce_stock(self.quantity_ordered):
            self.total_price = self.product.price * self.quantity_ordered
            self.status = "Confirmed"
        else:
            self.status = "Failed"
            raise ValueError(f"Order failed: Not enough stock for {self.product.name}")

    def order_summary(self):
        print("\n--- Order Summary ---")
        self.customer.display_info()
        print(f"Product: {self.product.name}")
        print(f"Quantity Ordered: {self.quantity_ordered}")
        print(f"Total Price: ${self.total_price:.2f}")
        print(f"Order Status: {self.status}")
        print(f"Remaining Stock: {self.product.quantity}")

# --- Main Execution ---

try:
    # 1. Create the Product
    p_name = input("Enter product name: ")
    p_price = float(input("Enter product price: "))   
    product1 = Product(p_name, p_price)

    # 2. Create the Customer
    c_name = input("Enter customer name: ")
    customer1 = Customer(c_name)

    # 3. Create the Order (Linking Customer and Product)
    qty = int(input("Enter quantity to order: "))
    
    # We pass the objects (customer1, product1) into the order
    order1 = Order(customer1, product1, qty)
    
    # 4. Show Result
    order1.order_summary()

except ValueError as e:
    print(f"\nError: {e}")