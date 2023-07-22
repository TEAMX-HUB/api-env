from compax_api.utils import _insert_parse_and_execute


def test_database_insertion(database_connection, data):
    assert _insert_parse_and_execute(
        "insert_into_users.sql", payload=data, conn=database_connection
    )
