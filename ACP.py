
class Customer:
    def __init__(self, name, purchases, payments):
        self.name = name
        self.purchases = purchases
        self.payments = payments

    def calculate_due_amount(self):
        total_purchases = sum(self.purchases)
        total_payments = sum(self.payments)
        return total_purchases - total_payments

def main():

    customer = Customer(
        "John Doe",
        purchases=[100.50, 75.25, 50.00], 
        payments=[150.00, 25.00]           
    )
    
    due_amount = customer.calculate_due_amount()
    print(f"Customer: {customer.name}")
    print(f"Total Purchases: ${sum(customer.purchases):.2f}")
    print(f"Total Payments: ${sum(customer.payments):.2f}")
    print(f"Due Amount: ${due_amount:.2f}")

if __name__ == "__main__":
    main()