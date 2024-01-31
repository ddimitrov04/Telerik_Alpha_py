class Neshto:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new):
        if len(new) < 5:
            raise ValueError("ne mojach")
        self.name = new



x = Neshto("Gosho")
print(x.name)