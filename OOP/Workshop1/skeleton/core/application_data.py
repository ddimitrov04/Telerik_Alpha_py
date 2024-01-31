from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:
    def __init__(self):
        self._products = []
        self._categories = []
        self._shoppingCart = ShoppingCart()

    @property
    def products(self):
        return tuple(self._products)

    @property
    def categories(self):
        return tuple(self._categories)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shoppingCart

    def find_product_by_name(self, name) -> Product:
        for product in self._products:
            if product.name == name:
                return product

        raise ValueError("Product doesn't exist")

    def find_category_by_name(self, name) -> Category:
        for category in self.categories:
            if category.name == name:
                return category

        raise ValueError("Category doesn't exist")

    def create_category(self, name) -> None:
        if self.category_exists(name):
            raise ValueError("Category with that name already exist")
        self._categories.append(Category(name))

    def create_product(self, name, brand, price, gender) -> None:
        if self.product_exists(name):
            raise ValueError("Product with that name already exist")
        self._products.append(Product(name, brand, price, gender))

    def category_exists(self, name) -> bool:
        for category in self._categories:
            if category.name == name:
                return True
        return False

    def product_exists(self, name) -> bool:
        for product in self._products:
            if product.name == name:
                return True
        return False
