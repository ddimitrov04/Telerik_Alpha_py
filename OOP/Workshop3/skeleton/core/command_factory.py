from commands.base.add_test_group import AddTestGroup
from commands.base.add_test import AddTest
from commands.base.add_test_run import AddTestRun
from commands.base.remove_group import RemoveGroup
from commands.base.test_report import TestReport
from commands.base.view_group import ViewGroup
from commands.base.view_system import ViewSystem
from application_data import ApplicationData


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = "a"

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == 'addtestgroup':
            return AddTestGroup(params, self._app_data, self._models_factory)
        elif cmd.lower() == 'addtest':
            return AddTest(params, self._app_data, self._models_factory)
        elif cmd.lower() == 'addtestrun':
            return AddTestRun(params, self._app_data)
        elif cmd.lower() == 'removegroup':
            return RemoveGroup(params, self._app_data)
        elif cmd.lower() == 'testreport':
            return TestReport(params, self._app_data)
        elif cmd.lower() == 'viewgroup':
            return ViewGroup(params, self._app_data)
        elif cmd.lower() == 'viewsystem':
            return ViewSystem(params, self._app_data)

        raise ValueError(f"Invalid command: {cmd}!")
