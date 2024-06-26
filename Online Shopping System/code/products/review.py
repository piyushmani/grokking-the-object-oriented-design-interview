from dataclasses import dataclass
from users.customer import Member
from products.product import Product

@dataclass
class ProductReview:
    rating: int
    review: str
    product: Product
    reviewer: Member
