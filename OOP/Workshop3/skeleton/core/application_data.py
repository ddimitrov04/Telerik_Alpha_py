from models.test_group import TestGroup


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []

    @property
    def groups(self):
        return tuple(self._test_groups)

    def find_test_group_by_id(self, test_group_id: int):
        for test_group in self._test_groups:
            if test_group.id == test_group_id:
                return test_group
        return None

    def add_test_group(self, test_group: TestGroup):
        self._test_groups.append(test_group)

    def remove_test_group_by_id(self, test_group_id):
        found_group = None
        for group in self._test_groups:
            if group.id == id:
                found_group = group

        if found_group is None:
            return False
        else:
            self._test_groups.remove(found_group)
            return True

    def find_test_by_id(self, test_id: int):
        for test_group in self._test_groups:
            for test in test_group.tests:
                if test.id == test_id:
                    return test
        return None
