from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.usage_type import UsageType
from models.shampoo import Shampoo


class CreateShampooCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        self._params = params
        self._app_data = app_data

    def execute(self):
        name = self._params[0]
        if self._app_data.product_exists(name):
            raise ValueError("This product already exists")
        brand = self._params[1]
        shampoo_price = float(self._params[2])

        shampoo_gender = self._params[3]
        Gender.from_string(shampoo_gender)
        shampoo_usage_type = self._params[5]
        if shampoo_usage_type != "Every_Day" and shampoo_usage_type != "Medical":
            raise ValueError("Shampoo should be 'Every_Day' or 'Medical'")
        shampoo_milliliters = int(self._params[4])

        self._app_data.create_shampoo(name, brand, shampoo_price, shampoo_gender, shampoo_usage_type, shampoo_milliliters)
        return f"Shampoo with name {name} was created!"
