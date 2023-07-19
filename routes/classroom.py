from fastapi import APIRouter

classroom = APIRouter()


@classroom.get("/classroom", tags=["classrooms"])
async def get_all_classrooms():
    pass


@classroom.get("/classroom/{classroom_id}", tags=["classrooms"])
async def get_classroom(classroom_id: int):
    pass
