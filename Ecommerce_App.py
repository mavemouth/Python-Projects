import json

class EcommerceApp:
    def __init__(self):
        self.users = {}
        self.products = {
            1: {'name': 'laptop', 'price': 800, 'stock': 5},
            2: {'name': 'phone', 'price': 500, 'stock': 10},
            3: {'name': 'headphones', 'price': 50, 'stock': 20}
        }
        self.cart = {}
        self.orders = []
        self.current_user = None

    def register_user(self):
        username = input("Enter username: ")
        if username in self.users:
            print("Username already exists!")
            return
        password = input("Enter Password: ")
        self.users[username] = password
        print("User registered successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter Password: ")
        if self.users.get(username) == password:
            self.current_user = username
            print("Login successful!")
        else:
            print("Invalid credentials!")

    def show_products(self):
        print("Available products:")
        for pid, details in self.products.items():
            print(f"{pid}. {details['name']} - ${details['price']} ({details['stock']} in stock)")

    def add_to_cart(self):
        if not self.current_user:
            print("Login first!")
            return
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        if product_id in self.products and self.products[product_id]['stock'] >= quantity:
            self.cart[product_id] = self.cart.get(product_id, 0) + quantity
            print("Product added to cart!")
        else:
            print("Invalid selection or insufficient stock!")

    def checkout(self):
        if not self.current_user:
            print("Please login first!")
            return
        if not self.cart:
            print("Cart is empty!")
            return
        total = sum(self.products[pid]['price'] * qty for pid, qty in self.cart.items())
        print(f"Total amount: ${total}")
        confirm = input("Confirm order? (yes/no): ").lower()
        if confirm == 'yes':
            self.orders.append({'user': self.current_user, 'items': self.cart.copy()})
            for pid, qty in self.cart.items():
                self.products[pid]['stock'] -= qty
            self.cart.clear()
            print("Order placed successfully!")
        else:
            print("Order cancelled!")

    def run(self):
        while True:
            print("\n1. Register \n2. Login \n3. View products \n4. Add to cart \n5. Checkout \n6. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.show_products()
            elif choice == '4':
                self.add_to_cart()
            elif choice == '5':
                self.checkout()
            elif choice == '6':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    app = EcommerceApp()
    app.run()
