from models.comment import Comment
from models.constants.user_role import UserRole
from models.vehicle import Vehicle


class User:
    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    # YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self, username: str, firstname: str, lastname: str, password: str, user_role: str):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.user_role = UserRole.from_string(user_role)
        self._is_admin = False
        if self.user_role == "Admin":
            self._is_admin = True

        self._vehicles = []

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def vehicles(self):
        return tuple(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle):
        role = self.user_role
        if self.is_admin:
            raise ValueError(self.ADMIN_CANNOT_ADD_VEHICLES_ERR)
        if role == "Normal":
            if len(self.vehicles) == 5:
                raise ValueError(self.NORMAL_USER_LIMIT_REACHED_ERR)

        self._vehicles.append(vehicle)

    def add_comment(self, content, vehicle: Vehicle):
        cmnt = Comment(content, self.username)
        vehicle.add_comment(cmnt)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name: str):
        if len(name) < 2 or len(name) > 20:
            raise ValueError(f'Username must be between 2 and 20 characters long!')

        for char in name:
            if not char.isalnum():
                raise ValueError('Username contains invalid symbols!')

        self._username = name

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, fname: str):
        if len(fname) < 2 or len(fname) > 20:
            raise ValueError(f'Firstname must be between 2 and 20 characters long!')

        self._firstname = fname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lname: str):
        if len(lname) < 2 or len(lname) > 20:
            raise ValueError(f'Lastname must be between 2 and 20 characters long!')

        self._lastname = lname

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, text: str):
        if len(text) < 5 or len(text) > 30:
            raise ValueError(f'Password must be between 5 and 30 characters long!')
        spec_symbols = ["@", "*", "-", "_"]
        for char in text:
            if not char.isalnum():
                if char not in spec_symbols:
                    raise ValueError('Password contains invalid symbols!')

        self._password = text

    def __str__(self):
        return f"Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}"

    def print_vehicles(self):
        if len(self._vehicles) == 0:
            return f"--USER {self.username}--\n--NO VEHICLES--"

        text = f"--USER {self.username}--"
        for i in range(len(self._vehicles)):
            text += f"\n{i + 1}. {self._vehicles[i]}"

        return text

    def get_vehicle(self, index):
        for i in range(len(self.vehicles)):
            if index == i:
                return self.vehicles[index]

        raise ValueError(self.THE_VEHICLE_DOES_NOT_EXIT)

    def remove_comment(self, comment, vehicle: Vehicle):
        if comment.author != self.username:
            raise ValueError("You are not the author of the comment you are trying to remove!")

        vehicle.remove_comment(comment)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)
