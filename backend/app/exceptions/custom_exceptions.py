from fastapi import status


class UserNotFoundException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User not found"


class UserAlreadyExistsException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = "User already exists"


class InvalidCredentialsException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Invalid email or password"


class UnauthorizedException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = "You are not authorized to perform this action"


class AddressNotFoundException(Exception):
    def __init__(self):
        self.message = "Address not found"
        super().__init__(self.message)