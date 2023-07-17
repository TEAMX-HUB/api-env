from compax_api.database import get_db_conn


def test_database_connection_pool():
    assert get_db_conn()
