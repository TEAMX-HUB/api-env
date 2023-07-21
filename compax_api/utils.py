from pathlib import Path

from psycopg import Connection

queries_directory = Path.cwd() / "queries"


def _insert_parse_and_execute(filename: Path, payload: tuple, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    conn.execute(f"""{data}""", payload)
    # if results:
    #     return {"Success": "Account created successfully!"}
    # return {"Failure": "Account creation failed!"}


async def _get_parse_and_execute(filename: Path, payload: tuple, conn: Connection):
    with open(queries_directory / filename) as d:
        data = d.read()

    results = await conn.execute(data, payload)
    if results:
        return results
    return {"Failure": "Account creation failed!"}
