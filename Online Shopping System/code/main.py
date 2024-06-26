from users.account import Account, Address
from users.customer import Customer
from orders.cart import Cart
from orders.order_item import OrderItem
from orders.order import Order
from payments.payment import Payment
from payments.credit_card_payment import CreditCardPayment
from products.product import Product
from products.category import ProductCategory
from catlog.catlog import Catalog

def main():
    # Setup categories and products
    electronics = ProductCategory(name="Electronics", description="Electronic devices and gadgets.")
    clothing = ProductCategory(name="Clothing", description="Apparel and accessories.")

    product1 = Product(product_id=1, name="Laptop", description="A high-performance laptop.", price=1500.00, category=electronics, available_item_count=10)
    product2 = Product(product_id=2, name="Jeans", description="Comfortable denim jeans.", price=50.00, category=clothing, available_item_count=50)

    # Setup catalog
    catalog = Catalog()
    catalog.add_product(product1)
    catalog.add_product(product2)

    # Create user account
    address = Address(street_address="123 Main St", city="Anytown", state="Anystate", zip_code=12345, country="Country")
    account = Account(username="johndoe", password="password", name="John Doe", email="john.doe@example.com", phone="123-456-7890", shipping_address=address)
    customer = Customer(account=account)

    # Member adds items to cart
    cart = Cart()
    order_item1 = OrderItem(product=product1, quantity=1, price=product1.price)
    order_item2 = OrderItem(product=product2, quantity=2, price=product2.price)
    cart.add_item(order_item1)
    cart.add_item(order_item2)

    # Member places an order
    order = Order(order_id=1, customer_id=1, order_items=cart.items)
    customer.place_order(order)

    # Member makes a payment
    payment_method = CreditCardPayment()
    payment = Payment(amount=order_item1.price * order_item1.quantity + order_item2.price * order_item2.quantity, method=payment_method)
    payment_success = payment.method.process_payment(payment.amount)

    if payment_success:
        print("Payment successful!")
    else:
        print("Payment failed!")

if __name__ == "__main__":
    main()