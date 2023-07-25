from fastapi import HTTPException


class CompaxException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code, detail=detail)


class BuildingNotFoundException(CompaxException):
    def __init__(self, building_id: str):
        detail = f"Building with ID {building_id} not found."
        super().__init__(status_code=404, detail=detail)


class ClassroomNotFoundException(CompaxException):
    def __init__(self, classroom_id: str):
        detail = f"Classroom with ID {classroom_id} not found."
        super().__init__(status_code=404, detail=detail)


class LaboratoryNotFoundException(CompaxException):
    def __init__(self, laboratory_id: str):
        detail = f"Laboratory with ID {laboratory_id} not found."
        super().__init__(status_code=404, detail=detail)


class OfficeNotFoundException(CompaxException):
    def __init__(self, office_id: str):
        detail = f"Office with ID {office_id} not found."
        super().__init__(status_code=404, detail=detail)


class UserNotFoundException(CompaxException):
    def __init__(self, message: str):
        detail = f"{message}"
        super().__init__(status_code=404, detail=detail)


class UserReferenceFoundException(CompaxException):
    def __init__(self, ref: int):
        detail = f"User with Reference {int} not found."
        super().__init__(status_code=404, detail=detail)


class UserNameNotFoundException(CompaxException):
    def __init__(self, username: str):
        detail = f"User with name {username} not found."
        super().__init__(status_code=404, detail=detail)


class AuthInvalidCredentialsException(CompaxException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid credentials. "
            + "User might exist. User with reference might exist. "
            + "User year group might be Incorrect",
        )


class InvalidRatingException(CompaxException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid credentials. Details Provided might incorrect!",
        )


class UnauthorizedException(CompaxException):
    def __init__(self):
        super().__init__(status_code=403, detail="Unauthorized access.")


class BookingNotFoundException(CompaxException):
    def __init__(self, booking_id: str):
        detail = f"Booking with ID {booking_id} not found."
        super().__init__(status_code=404, detail=detail)
