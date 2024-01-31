from base_command import BaseCommand  # Assuming you have a BaseCommand class


class ViewSystem(BaseCommand):
    def __init__(self, params, app_data):
        super().__init__(params, app_data)

    def execute(self):
        test_groups_count = len(self._app_data.groups)

        system_info = f'Test Reporter System ({test_groups_count} test groups)\n'

        for test_group in self._app_data.groups:
            group_info = (
                f'  #{test_group.id}. {test_group.name} ({len(test_group.tests)} tests)\n'
            )
            system_info += group_info

        return system_info
