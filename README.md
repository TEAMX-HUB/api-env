# Compax FastAPI Backend

## Contents
- [Quick Start](#quick_start)
- [Testing](#testing)
- [Api Routes](#api_routes)
- [File Structure](#file_structure)
- [Built Using](#built_using)
- [Team](#team)

## Quick Start <a name = "quick_start"></a>

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

## Testing <a name = "testing"></a>

To run the tests in the project:

- You need to install the dev packages:

  ```bash
  poetry install --with dev
  ```

## Api Routes <a name = "api_routes"></a>

App Routes will be placed here!

## File Structure for Project <a name = "file_structure"></a>

Project Structure will be update soon.


##  Built Using <a name = "built_using"></a>
- [FastAPI](https://fastapi.tiangolo.com/) - Python Framework
- [Postgres](https://www.postgresql.org/) - Database
- [Poetry](https://python-poetry.org/) - Python Package Manager
- [Docker](https://www.docker.com/) - Containerization
- [SqlAlchemy](https://www.sqlalchemy.org/) - ORM
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Database Migration
- [Pytest](https://docs.pytest.org/en/6.2.x/) - Testing Framework


##  Team <a name = "team"></a>
- [@blackprince001](https://github.com/blackprince001)
- [@RansfordGenesis](https://github.com/RansfordGenesis)
- [@Benedicta-Asare](https://github.com/Benedicta-Asare)
- [@jasper-tech](https://github.com/jasper-tech)
- [@mkweeks](https://github.com/mkweeks)
- [@1sreal](https://github.com/1sreal)