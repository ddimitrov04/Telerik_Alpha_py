from models.vehicle import Vehicle


class Truck(Vehicle):
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
    # WEIGHT_CAP_MIN = 1
    # WEIGHT_CAP_MAX = 100
    # WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'
    #
    # WHEELS_COUNT = 8

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
    def __init__(self, make, model, price, weight_capacity):
        super().__init__(make, model, price)
        self.wheels = 8
        self.weight_capacity = weight_capacity


    @property
    def weight_capacity(self):
        return self._weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, value):
        if value < 1 or value > 100:
            raise ValueError('Weight capacity must be between 1 and 100!')

        self._weight_capacity = value


    def __str__(self):
        text = f"{super().__str__()}\nWeight Capacity: {self.weight_capacity}t\n"
        if not self.comments:
            cmntmsg = f"--NO COMMENTS--"
        else:
            cmntmsg = f"--COMMENTS--"
            for c in self.comments:
                cmntmsg += f"\n{c}"
            cmntmsg += f"\n--COMMENTS--"
        text += cmntmsg
        return text