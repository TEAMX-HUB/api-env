from uuid import uuid4 as UUID

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
    def __init__(self, user_id: UUID):
        detail = f"User with ID {user_id} not found."
        super().__init__(status_code=404, detail=detail)


class InvalidCredentialsException(CompaxException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid credentials.")


class UnauthorizedException(CompaxException):
    def __init__(self):
        super().__init__(status_code=403, detail="Unauthorized access.")


class BookingNotFoundException(CompaxException):
    def __init__(self, booking_id: str):
        detail = f"Booking with ID {booking_id} not found."
        super().__init__(status_code=404, detail=detail)
