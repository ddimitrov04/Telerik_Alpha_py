from models.test import Test
from models.test_group import TestGroup


class ModelsFactory:
    def __init__(self):
        self._test_group_id = 1
        self._test_id = 1

    def create_group(self, name: str):
        group_id = self._test_group_id
        self._test_group_id += 1

        return TestGroup(group_id, name)

    def create_test(self, description: str):
        test_id = self._test_id
        self._test_id += 1

        return Test(test_id, description)
