from base_command import BaseCommand


class ViewGroup(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):

        test_group_id = self._params[0]

        test_group = self._app_data.find_test_group_by_id(test_group_id)

        if not test_group:
            raise ValueError(f"TestGroup with ID {test_group_id} not found.")

        group_id = test_group.id
        group_name = test_group.name
        tests_count = len(test_group.tests)

        group_info = f'#{group_id}. {group_name} ({tests_count} tests)\n'

        for test in test_group.tests:
            test_info = (
                f'  #{test.id}. [{test.description}]: {len(test.test_runs)} runs\n'
            )
            group_info += test_info

        return group_info
