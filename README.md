# Compax FastAPI Backend

This Readne is to only aid you set up a development workspace on your choice editing tools.

Access full extensive documentation here! [Documentation](https://teamx-hub.github.io/Compax-docs/)

## Quick Start

- Clone the repository

    ```bash
    git clone https://github.com/TEAMX-HUB/api-env
    ```

- Move into the directory

    ```bash
    cd api-env
    ```

- Set up a virtual environment with Venv on Vscode or any python environment manager you have installed, and it will automatically install the dependencies. This project uses pipenv to handle dependency installs and virtual environments.

- To simply install project dependencies, you have to run the following commands.

  ```bash
  poetry shell
  ```

  The above command inits a python virtual environment in your current directory. Then you proceed to do;

  ```bash
  poetry install
  ```

  to install all dependencies!

- Set up a dev environment by running the command to install dependencies to work on the project. Do note that the make command is already dependent on the one above. So if you use this command, there will be no need for you to run the prev one.
  
  ```bash
  poetry install --with dev
  ```

  while you're in `/api-env`

## Testing

To run the tests in the project:

- You need to install the dev packages:

  ```bash
  poetry install --with dev
  ```

## Project Structure

```console
.
├── app.py
├── compax_api
│   ├── config.py
│   ├── database.py
│   ├── errors.py
│   ├── __init__.py
│   ├── security.py
│   └── utils.py
├── Dockerfile
├── LICENSE
├── poetry.lock
├── prod.env
├── pyproject.toml
├── queries
│   ├── get_all_buildings.sql
│   ├── get_all_classroom_in_building_name.sql
│   ├── get_all_classrooms_in_building_id.sql
│   ├── get_all_classrooms.sql
│   ├── get_all_labs_in_building_id.sql
│   ├── get_all_labs_in_building_name.sql
│   ├── get_all_labs.sql
│   ├── get_all_offices_in_building_id.sql
│   ├── get_all_offices.sql
│   ├── get_all_ratings_building.sql
│   ├── get_all_ratings_classroom.sql
│   ├── get_all_ratings_lab.sql
│   ├── get_all_ratings_office.sql
│   ├── get_all_ratings.sql
│   ├── get_all_schedule.sql
│   ├── get_building_with_id.sql
│   ├── get_building_with_name.sql
│   ├── get_classroom_with_id.sql
│   ├── get_classroom_with_name.sql
│   ├── get_lab_with_id.sql
│   ├── get_lab_with_name.sql
│   ├── get_office_with_id.sql
│   ├── get_office_with_name.sql
│   ├── get_schedule_all_for_day.sql
│   ├── get_schedule_all_for_session.sql
│   ├── get_schedule_day_with_classes.sql
│   ├── get_schedule_day_with_user_data.sql
│   ├── get_schedule_for_classroom.sql
│   ├── get_schedule_for_lab.sql
│   ├── get_schedule_with_user_data.sql
│   ├── get_user_reference.sql
│   ├── get_user_username.sql
│   ├── get_user_uuid.sql
│   ├── insert_into_ratings.sql
│   ├── insert_into_users.sql
│   └── update_ratings_comments.sql
├── README.md
├── requirements.txt
├── routes
│   ├── admin.py
│   ├── auth.py
│   ├── building.py
│   ├── classroom.py
│   ├── __init__.py
│   ├── laboratory.py
│   ├── office.py
│   ├── ratings.py
│   ├── schedule.py
│   └── user.py
├── schema
│   ├── buildings.py
│   ├── classroom.py
│   ├── __init__.py
│   ├── laboratory.py
│   ├── office.py
│   ├── ratings.py
│   ├── schedule.py
│   └── user.py
├── tests
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_bucket.py
│   ├── test_database_connection.py
│   └── test_insertion.py
└── TODO.md

6 directories, 74 files
```

## Built Using

- [FastAPI](https://fastapi.tiangolo.com/) - Python Framework
- [Postgres](https://www.postgresql.org/) - Database
- [Poetry](https://python-poetry.org/) - Python Package Manager
- [Docker](https://www.docker.com/) - Containerization
- [Pytest](https://docs.pytest.org/en/6.2.x/) - Testing Framework
