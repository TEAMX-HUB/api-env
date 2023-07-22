from __future__ import annotations

import pytest
from psycopg import Connection
from supabase import Client, create_client

from compax_api.config import get_settings
from compax_api.database import get_db_conn

config = get_settings()


@pytest.fixture(scope="session")
def supabase() -> Client:
    url, key = config.supabase_client_url, config.supabase_client_key

    assert url is not None, "Must provide SUPABASE_TEST_URL environment variable"
    assert key is not None, "Must provide SUPABASE_TEST_KEY environment variable"
    return create_client(url, key)


@pytest.fixture(scope="session")
def database_connection() -> Connection:
    return get_db_conn()


@pytest.fixture(scope="session")
def data() -> dict:
    data = {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "username": "ehehehehehasd@st.knust.edu.gh",
        "student_reference": 12345678,
        "department": "Computer Science",
        "year_group": 3,
        "password": "creatine",
        "created_at": "2023-07-21T09:43:46.730Z",
        "is_classrep": True,
        "is_admin": False,
        "is_deleted": False,
        "is_exams_officer": False,
    }
    return data
