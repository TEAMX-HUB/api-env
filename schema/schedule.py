from pydantic import BaseModel
from datetime import date, time


class AcademicEventWeek(BaseModel):
    id: int
    weekday: str
    department: str
    schedule_id: int
    track_id: int


class AcademicTrack(BaseModel):
    id: int
    semester: int
    sem_starts: date
    sem_ends: date
    academic_year: str


class SessionSchedule(BaseModel):
    id: int
    course_code: str
    course_name: str
    year_group: int
    schedule_time: int
    class_location: int
    lab_location: int


class SessionTime(BaseModel):
    id: int
    start_time: time
    end_time: time
