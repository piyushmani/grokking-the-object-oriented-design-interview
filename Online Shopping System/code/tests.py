import unittest
from datetime import date
from dataclasses import replace
from users.account import Account, AccountStatus, Address
from users.customer import Customer
from orders.order import Order
from products.product import Product, ProductCategory
from shipment.shipment import Shipment
from shipment.shipment import  ShipmentLog
from notification.notification import Notification
from catlog.catlog import Catalog

class TestCustomer(unittest.TestCase):
    def setUp(self):
        # Create a sample Address for the Account
        self.shipping_address = Address(street_address="123 Main St", city="Anytown", state="ABC", zip_code="12345", country="XYZ")

        # Create an Account instance with required arguments
        self.account = Account(username="test_user", password="password", name="Test User",
                               email="test@example.com", phone="123-456-7890",
                               shipping_address=self.shipping_address)

        # Create a Customer instance
        self.customer = Customer(account=self.account)

    def test_add_item_to_cart(self):
        # Implement your test for adding items to the cart
        product_category = ProductCategory(name="Electronics", description="Electronic products")
        product = Product(product_id=1, name="Laptop", description="High-performance laptop",
                          price=1500.0, category=product_category, available_item_count=10)
        self.customer.add_item_to_cart(product)
        self.assertIn(product, self.customer.cart)

    def test_place_order(self):
        # Implement your test for placing an order
        product_category = ProductCategory(name="Electronics", description="Electronic products")
        product = Product(product_id=1, name="Laptop", description="High-performance laptop",
                          price=1500.0, category=product_category, available_item_count=10)
        self.customer.add_item_to_cart(product)
        order = Order(order_id=1, customer_id=self.customer, order_items=[product])
        self.customer.place_order(order)

        self.assertIsInstance(order, Order)
        self.assertEqual(self.customer.order[0], order)

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        category = ProductCategory(name="Electronics", description="Electronic products")
        product = Product(product_id=1, name="Laptop", description="High-performance laptop",
                          price=1500.0, category=category, available_item_count=10)
        order = Order(order_id=1, customer_id="test_user", order_items=[product])
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.customer_id, "test_user")
        self.assertIn(product, order.order_items)

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        category = ProductCategory(name="Electronics", description="Electronic products")
        product = Product(product_id=1, name="Laptop", description="High-performance laptop",
                          price=1500.0, category=category, available_item_count=10)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1500.0)
        self.assertEqual(product.category, category)

class TestProductCategory(unittest.TestCase):
    def test_product_category_creation(self):
        category = ProductCategory(name="Electronics", description="Electronic products")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic products")

class TestShipment(unittest.TestCase):
    def test_shipment_creation(self):
        shipment = Shipment(shipment_number=1, shipment_method="Air")
        self.assertEqual(shipment.shipment_number, 1)
        self.assertEqual(shipment.shipment_method, "Air")

    def test_add_shipment_log(self):
        shipment = Shipment(shipment_number=1, shipment_method="Air")
        shipment_log = ShipmentLog(shipment_number=shipment.shipment_number, status="Shipped")
        shipment.add_shipment_log(shipment_log)
        self.assertEqual(shipment.shipment_logs[0], shipment_log)

class TestNotification(unittest.TestCase):
    def test_notification_creation(self):
        notification = Notification(notification_id=1, content="New notification")
        self.assertEqual(notification.notification_id, 1)
        self.assertEqual(notification.content, "New notification")

class TestCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog()

    def test_add_product_to_catalog(self):
        category = ProductCategory(name="Electronics", description="Electronic products")
        product = Product(product_id=1, name="Laptop", description="High-performance laptop",
                          price=1500.0, category=category, available_item_count=10)
        self.catalog.add_product(product)

        # Test if product is added to product_names dictionary
        self.assertEqual(self.catalog.product_names["Laptop"], product)

        # Test if product is added to product_categories dictionary
        self.assertIn(product, self.catalog.product_categories["Electronics"])

    def test_search_products_by_name(self):
        category = ProductCategory(name="Electronics", description="Electronic products")
        product = Product(product_id=1, name="Laptop", description="High-performance laptop",
                          price=1500.0, category=category, available_item_count=10)
        self.catalog.add_product(product)

        # Test searching for a product by name
        found_product = self.catalog.search_products_by_name("Laptop")
        self.assertEqual(found_product, product)

        # Test searching for a non-existent product
        non_existent_product = self.catalog.search_products_by_name("Desktop")
        self.assertIsNone(non_existent_product)

    def test_search_products_by_category(self):
        category = ProductCategory(name="Electronics", description="Electronic products")
        laptop = Product(product_id=1, name="Laptop", description="High-performance laptop",
                        price=1500.0, category=category, available_item_count=10)
        tablet = Product(product_id=2, name="Tablet", description="Portable tablet",
                        price=800.0, category=category, available_item_count=5)
        self.catalog.add_product(laptop)
        self.catalog.add_product(tablet)

        # Test searching for products by category
        electronics_products = self.catalog.search_products_by_category("Electronics")
        self.assertIn(laptop, electronics_products)
        self.assertIn(tablet, electronics_products)

        # Test searching for products in a non-existent category
        non_existent_category = self.catalog.search_products_by_category("Books")
        self.assertIsNone(non_existent_category)

if __name__ == "__main__":
    unittest.main()

