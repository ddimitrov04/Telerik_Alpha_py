from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User


class ShowUsersCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        if self._requires_login() and not self._app_data.has_logged_in_user:
            raise ValueError('You are not logged in! Please login first!')
        user: 'User' = self._app_data.logged_in_user
        if not user.is_admin:
            raise ValueError('You are not an admin!')

        counter = 1
        text = "--USERS--"
        for i, user in enumerate(self._app_data.users):
            text += f"\n{counter}. {str(user)}"
            counter += 1

        return text

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0