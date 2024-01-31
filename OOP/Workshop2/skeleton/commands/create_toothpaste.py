from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float
from models.toothpaste import Toothpaste


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):

        name = self._params[0]
        if self._app_data.product_exists(name):
            raise ValueError("Product already created")
        brand = self._params[1]
        price = float(self._params[2])
        gender = self._params[3]
        Gender.from_string(gender)
        ingredients = self._params[4]

        print(name)
        print(brand)
        print(price)
        print(gender)
        print(ingredients)

        self._app_data.create_toothpaste(name,brand,price,gender,ingredients)
        return f"Toothpaste with name {name} was created!"
