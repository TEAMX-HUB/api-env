from pathlib import Path

from psycopg import Connection

queries_directory = Path.cwd() / "queries"


def _insert_parse_and_execute(filename: Path, payload: dict, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    conn.execute(f"""{data}""", payload)
    # if results:
    #     return {"Success": "Account created successfully!"}
    # return {"Failure": "Account creation failed!"}


def _get_all_and_execute_params(filename: Path, payload: dict, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = conn.execute(
        data,
        payload,
    ).fetchall()
    if results:
        return results
    return {"Failure": "No Results Found!"}


def _get_one_and_execute_params(filename: Path, payload: dict, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = conn.execute(data, payload).fetchone()

    if results:
        return results
    return {"Failure": "No Results Found!"}


def _get_all_and_execute(filename: Path, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = conn.execute(data).fetchall()
    if results:
        return results
    return {"Failure": "No Results Found!"}


def _get_one_and_execute(filename: Path, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = conn.execute(
        data,
    ).fetchone()
    if results:
        return results
    return {"Failure": "No Results Found!"}
