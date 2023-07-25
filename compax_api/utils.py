from pathlib import Path

from psycopg import Connection

queries_directory = Path.cwd() / "queries"


def _insert_one_and_execute_params(filename: Path, payload: dict, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = conn.execute(f"""{data}""", payload)
    if results:
        return {"Success": "Insert Successful!"}
    return {"Failure": "Insert Successful!"}


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


def _update_and_execute(filename: Path, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = conn.execute(
        data,
    )
    if results:
        return results
    return {"Failure": "No Results Found!"}
