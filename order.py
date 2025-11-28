class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 100
    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
class order(product):
    def __init__(self, name, price, quantity_ordered):
        super().__init__(name, price)
        self.quantity_ordered = quantity_ordered
        if quantity_ordered <= self.quantity:
            self.total_price = self.price * self.quantity_ordered
            self.quantity -= self.quantity_ordered
        else:
            raise ValueError("Ordered quantity exceeds available stock.")

    def order_summary(self):
        print(f"Order Summary:\nProduct: {self.name}\nQuantity Ordered: {self.quantity_ordered}\nTotal Price: ${self.total_price:.2f}\nRemaining Stock: {self.quantity}")
class  customer(order):
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def customer_info(self):
        print(f"Customer Name: {self.customer_name}")
    
name = input("Enter product name: ")
price = float(input("Enter product price: "))   
quantity_ordered = int(input("Enter quantity to order: "))
order1 = order(name, price, quantity_ordered)
order1.order_summary()
customer_name = input("Enter customer name: ")
customer1 = customer(customer_name)
customer1.customer_info()