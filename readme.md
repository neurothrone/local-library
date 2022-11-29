# Local Library Web App / API

## About

![Index page of the website](assets/website.png?raw=true "Local Library index page")

An asynchronous Web App and API for managing a local library of books. Books that you're reading, have read and
will read.

## Demo

[demo]: https://zn-local-library.herokuapp.com

A working demo can be found at [Heroku][demo].

## Setup

1. Install packages from requirements.txt
2. Add an environment file called `.env` in the projects root directory with the following content:

```sh
DB_URL=...  # only if using production environment
ENVIRONMENT=...  # development, testing or production
```

3. Execute the script `run.py` or run the following command in a terminal from the root project directory:

```sh
uvicorn run:app
```

## Tools

[fastapi]: https://fastapi.tiangolo.com/

[tortoise-orm]: https://tortoise-orm.readthedocs.io/

[htmx]: https://htmx.org/

- Web framework: [FastAPI][fastapi]
- Database ORM: [Tortoise ORM][tortoise-orm]
- Frontend: [HTMX][htmx]
