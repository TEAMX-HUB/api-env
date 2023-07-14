from fastapi import APIRouter

auth = APIRouter()


@auth.get("", tags=["auth"])
async def login():
    pass
