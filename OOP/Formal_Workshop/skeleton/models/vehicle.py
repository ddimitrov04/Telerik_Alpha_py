from models.comment import Comment

class Vehicle:
    def __init__(self, make: str, model: str, price: float):
        self.make = make
        self.model = model
        self.price = price
        self.type = type(self).__name__
        self._comments = []
        self.content = True
        if len(self._comments) < 1:
            self.content = False
        self.wheels = 2
        if self.type == "Car":
            self.wheels = 4
        elif self.type == "Truck":
            self.wheels = 8

    @property
    def comments(self):
        return tuple(self._comments)

    def get_comment(self, index):
        for i in range(len(self._comments)):
            if i == index:
                return self._comments[index]
        raise ValueError("There is no comment on this index.")

    def remove_comment(self, index):
        if index in self._comments:
            self._comments.remove(index)

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value: str):
        if len(value) < 2 or len(value) > 15:
            raise ValueError("Make must be between 2 and 15 characters long!")
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Model must be between 1 and 15 characters long!")
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0 or value > 1000000:
            raise ValueError("Price must be between 0.0 and 1000000.00!")

        self._price = value

    def __str__(self):
        return f"{self.type}:\nMake: {self.make}\nModel: {self.model}\nWheels: {self.wheels}\nPrice: ${self.price:.2f}"

