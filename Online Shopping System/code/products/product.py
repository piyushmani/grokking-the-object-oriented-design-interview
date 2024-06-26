from dataclasses import dataclass
from products.category import ProductCategory

@dataclass
class Product:
    product_id: int
    name: str
    description: str
    price: float
    category: ProductCategory
    available_item_count: int = 0
