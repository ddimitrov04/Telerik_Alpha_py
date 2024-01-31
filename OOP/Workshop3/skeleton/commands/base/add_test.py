from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class AddTest(BaseCommand):
    def __init__(self, params : list[str], app_data: ApplicationData, models_factory : ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        test_group_id = int(self.params[0])
        description = self.params[1]

        test_group = self._app_data.find_test_group_by_id(test_group_id)

        if test_group is None:
            return f"TestGroup with ID {test_group_id} not found."

        new_test = self._models_factory.create_test(description)

        test_group.add_test(new_test)

        return f'Test #{test_group.id} was added to TestGroup with ID {test_group_id}.'
