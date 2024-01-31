
class Category:
    def __init__(self, name):
        if len(name) < 2 or len(name) > 15:
            raise ValueError("Name is out of bounds!")
        self._name = name
        self._products = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value < 2 or value > 15:
            raise ValueError("Name is out of bounds!")
        self._name = value


    @property
    def products(self):
        return tuple(self._products)


    def add_product(self, product):
        if product in self._products:
            raise ValueError("Product already in products")

        self._products.append(product)

    def remove_product(self, product):
        if product not in self._products:
            raise ValueError("Product doesn't exist in products")

        self._products.remove(product)

    def to_string(self):
        result = f"#Category: {self._name}\n"
        if not self._products:
            result += "#No products in this category"
        else:
            for i in range(len(self._products)-1):
                result += self._products[i].to_string() + "\n ===\n"
            result += self._products[-1].to_string()
        return result


