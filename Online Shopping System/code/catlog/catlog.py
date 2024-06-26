from dataclasses import dataclass, field
from products.product import Product
from products.category import ProductCategory
from search.search import Search

@dataclass
class Catalog(Search):
    product_names: dict = field(default_factory=dict)
    product_categories: dict = field(default_factory=dict)

    def add_product(self, product: Product):
        self.product_names[product.name] = product
        if product.category.name not in self.product_categories:
            self.product_categories[product.category.name] = []
        self.product_categories[product.category.name].append(product)

    def search_products_by_name(self, name: str):
        return self.product_names.get(name)

    def search_products_by_category(self, category: str):
        return self.product_categories.get(category)
