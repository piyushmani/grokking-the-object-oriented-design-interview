from dataclasses import dataclass
from products.product import Product

@dataclass
class OrderItem:
    product: Product
    quantity: int
    price: float
