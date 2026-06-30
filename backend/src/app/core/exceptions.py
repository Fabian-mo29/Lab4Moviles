class AppException(Exception):
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)

class NotFoundException(AppException):
    def __init__(self, entity: str, identifier: str | None = None):
        if identifier:
            detail = f"{entity} '{identifier}' not found."
        else:
            detail = f"{entity} not found."

        super().__init__(detail)

class AlreadyExistsException(AppException):
    def __init__(self, entity: str, field: str):
        super().__init__(f"{entity} with '{field}' already exists.")

class UnauthorizedException(AppException):
    def __init__(self, detail: str = "Invalid credentials."):
        super().__init__(detail)

class BadRequestException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail)

class ForbiddenException(AppException):
    def __init__(self, detail: str = "Access denied."):
        super().__init__(detail)
