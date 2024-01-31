from base_command import BaseCommand
from models.test_run import TestRun


class AddTestRun(BaseCommand):

    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        test_id, result, runtime = self._params

        test = self._app_data.find_test_by_id(test_id)

        if not test:
            raise ValueError(f"Test with ID {test_id} not found.")

        new_test_run = TestRun(result, runtime)

        test.add_test_run(new_test_run)

        return f'TestRun with result "{result}" and runtime {runtime}ms was added to Test with ID {test_id}.'
