class Product:
    def __init__(self, name, price, stock=100):
        self.name = name
        self.price = price
        self.quantity = stock

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

class Customer:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Customer Name: {self.name}")

class Order:
    def __init__(self, product, customer, quantity_ordered):
        self.product = product    # The order contains a Product object
        self.customer = customer  # The order belongs to a Customer object
        self.quantity_ordered = quantity_ordered
        self.total_price = 0
        
        # Check stock logic
        if quantity_ordered <= self.product.quantity:
            self.total_price = self.product.price * self.quantity_ordered
            self.product.quantity -= self.quantity_ordered
        else:
            raise ValueError(f"Ordered quantity ({quantity_ordered}) exceeds available stock ({self.product.quantity}).")

    def order_summary(self):
        print("\n--- Order Summary ---")
        print(f"Customer: {self.customer.name}")
        print(f"Product: {self.product.name}")
        print(f"Price per unit: ${self.product.price:.2f}")
        print(f"Quantity Ordered: {self.quantity_ordered}")
        print(f"Total Price: ${self.total_price:.2f}")
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

    # 3. Create the Order (Linking Product and Customer)
    qty = int(input("Enter quantity to order: "))
    order1 = Order(product1, customer1, qty)

    # 4. Show Summary
    order1.order_summary()

except ValueError as e:
    print(f"Error: {e}")