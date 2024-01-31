from base_command import BaseCommand  # Assuming you have a BaseCommand class


class TestReport(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        test_id = self._params[0]

        test = self._app_data.find_test_by_id(test_id)

        if not test:
            raise ValueError(f"Test with ID {test_id} not found.")

        test_description = test.description
        test_runs_count = len(test.test_runs)
        passing_runs_count = sum(1 for run in test.test_runs if run.test_result == "pass")
        failing_runs_count = test_runs_count - passing_runs_count
        total_runtime = sum(run.runtime for run in test.test_runs)
        avg_runtime = total_runtime / test_runs_count if test_runs_count > 0 else 0

        report_info = (
            f'#{test_id}. [{test_description}]: {test_runs_count} runs\n'
            f'- Passing: {passing_runs_count}\n'
            f'- Failing: {failing_runs_count}\n'
            f'- Total runtime: {total_runtime}ms\n'
            f'- Average runtime: {avg_runtime:.1f}ms'
        )

        return report_info
