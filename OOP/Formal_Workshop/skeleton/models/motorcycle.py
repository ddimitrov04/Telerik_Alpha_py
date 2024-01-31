from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    # MAKE_LEN_MIN = 2
    # MAKE_LEN_MAX = 15
    # MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'
    #
    # MODEL_LEN_MIN = 1
    # MODEL_LEN_MAX = 15
    # MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'
    #
    # PRICE_MIN = 0
    # PRICE_MAX = 1000000
    # PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'
    #
    # CATEGORY_LEN_MIN = 3
    # CATEGORY_LEN_MAX = 10
    # CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'
    #
    # WHEELS_COUNT = 2
    # Names of methods/attributes should be exactly match those in the README file
    def __init__(self, make , model, price, category: str):
        super().__init__(make, model, price)
        self.category = category
        self.wheels = 2

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        if len(value) < 3 or len(value) > 10:
            raise ValueError('Category must be between 3 and 10 characters long!')

        self._category = value


    def __str__(self):
        text = f"{super().__str__()}\nCategory: {self.category}\n"
        if not self.comments:
            cmntmsg = f"--NO COMMENTS--"
        else:
            cmntmsg = f"--COMMENTS--"
            for c in self.comments:
                cmntmsg += f"\n{c}"
            cmntmsg += f"\n--COMMENTS--"
        text += cmntmsg
        return text
