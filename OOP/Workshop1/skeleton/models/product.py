from models.gender import Gender


class Product:
    def __init__(self, name, brand, price, gender):
        if len(name) < 3 or len(name) > 10:
            raise ValueError("Invalid product name length")
        self._name = name

        if len(brand) < 2 or len(brand) > 10:
            raise ValueError("Invalid brand name length")
        self._brand = brand
        if price < 0:
            raise ValueError("Price can't be negative")
        self._price = price
        Gender.from_string(gender)
        self._gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3 or len(value) > 10:
            raise ValueError("Invalid product name length")
        if value == self._name:
            raise ValueError("A product with that name already exists!")
        self._name = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if len(value) < 2 or len(value) > 10:
            raise ValueError("Invalid brand name length")
        self._brand = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")

        self._price = value

    @property
    def gender(self):
        return self._gender

    def to_string(self):
        prodPrice = self._price
        return f" #{self._name} {self._brand}\n #Price: ${prodPrice:.2f}\n #Gender: {self._gender}"


# prod = Product("Cola", "coca-cola", 3, "Unisex")
#
# print(prod.to_string())
