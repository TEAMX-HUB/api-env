from compax_api.database import get_db_conn
from compax_api.utils import _insert_parse_and_execute

data = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "username": "JohnDoe@st.knust.edu.gh",
    "student_reference": 12345678,
    "department": "Computer Science",
    "year_group": 3,
    "password": "newpassword",
    "created_at": "2023-07-21T09:43:46.730Z",
    "is_classrep": True,
    "is_admin": False,
    "is_deleted": False,
    "is_exams_officer": False,
}

_insert_parse_and_execute("insert_into_users.sql", payload=data, conn=get_db_conn())
