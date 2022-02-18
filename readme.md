# Local Library Web App / Api

## About

A simple asynchronous Web App and API for managing a local library of books. Books that you're reading, have read and
will read.

## Demo

[demo]: https://zn-local-library.herokuapp.com

A working demo can be found at [Heroku][demo].

## Setup

Execute the script `run.py` or run the following command in a terminal from the root project directory:

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
