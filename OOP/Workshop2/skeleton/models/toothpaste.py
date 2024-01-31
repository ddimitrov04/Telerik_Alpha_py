from models.product import Product


class Toothpaste(Product):

    def __init__(self, name, brand, price, gender, ingredients):
        self._ingredients = ingredients
        super().__init__(name, brand, price, gender)

    @property
    def ingredients(self):
        return tuple(self._ingredients)

    @ingredients.setter
    def ingredients(self, new):
        self._ingredients = new

    def to_string(self):
        result = f" #{self.name} {self.brand}\n #Price: ${self.price:.2f}\n #Gender: {self.gender}\n #Ingredients: "
        counter = 0
        for i in self._ingredients:
            if counter == 0:
                result += "["
            counter +=1

            result += f"{i}, "
            if counter == len(self._ingredients)-1:
                    break
        result += f"{self._ingredients[-1]}]"
        return result

