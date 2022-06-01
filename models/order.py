class Order:
    def __init__(
        self, customer_name, order_date, quantity, location, description, completed
    ):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.location = location
        self.description = description
        self.completed = completed
