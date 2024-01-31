from models.product import Product


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        self.usage_type = usage_type
        if usage_type == "Every_Day" or usage_type == "Medical":
            raise ValueError("Shampoo should be 'Every_Day' or 'Medical'")
        self.milliliters = milliliters
        super().__init__(name, brand, price, gender)

    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        if value != "Every_Day" and value != "Medical":
            raise ValueError("Shampoo should be 'Every_Day' or 'Medical'")
        self._usage_type = value

    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, new):
        if new < 0:
            raise ValueError("Milliliters cannot be negative")
        self._milliliters = new

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Milliliters: {self._milliliters}',
            f' #Usage: {self._usage_type}'
        ])


