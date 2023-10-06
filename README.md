# Ecoalert

Example gql server in python that fetces data from external apis. Uses Strawberry + FastAPI.

## Setup

Requires poetry.

```sh
poetry install
poetry run uvicorn ecoalert.main:app # --reload if you want hot reloading
```

The graphiql interface is available from your browser at `localhost:8000/graphql`.
