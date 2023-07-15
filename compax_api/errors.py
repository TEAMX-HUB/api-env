from fastapi import HTTPException


class UserNotFound(HTTPException):
    pass


class AdminNotFound(HTTPException):
    pass


...  # more exceptions should be added here
