from base_command import BaseCommand
from models.test_group import TestGroup


class AddTestGroup(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        name = self._params[0]

        new_group_id = len(self._app_data.groups) + 1

        new_test_group = TestGroup(new_group_id, name)

        self._app_data.add_test_group(new_test_group)

        return f'TestGroup with name {name} and ID {new_group_id} was created!'
