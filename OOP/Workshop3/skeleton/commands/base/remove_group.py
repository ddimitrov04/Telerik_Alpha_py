from base_command import BaseCommand


class RemoveGroup(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):

        test_group_id = self._params[0]

        test_group = self._app_data.find_test_group_by_id(test_group_id)

        if not test_group:
            raise ValueError(f"TestGroup with ID {test_group_id} not found.")

        for test in test_group.tests:
            test.clear_test_runs()

        self._app_data.remove_test_group_by_id(test_group_id)

        return f'TestGroup with ID {test_group_id} and all its tests and test runs were removed.'
