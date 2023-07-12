from fastapi import APIRouter

classroompoint = APIRouter()


@classroompoint.get("/classroom", tags=["classrooms"])
async def get_all_classrooms():
    pass


@classroompoint.get("/classroom/{classroom_id}", tags=["classrooms"])
async def get_classroom(classroom_id: int):
    pass
