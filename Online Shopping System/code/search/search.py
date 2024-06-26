from abc import ABC
from typing import List

class Search(ABC):
    def search_products_by_name(self, name: str) -> List:
        pass

    def search_products_by_category(self, category: str) -> List:
        pass
