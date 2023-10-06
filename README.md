# Ecoalert

Example gql server in python that fetces data from external apis. Uses Strawberry + FastAPI.

## Setup

Requires poetry.

```sh
poetry install
poetry run uvicorn ecoalert.main:app # --reload if you want hot reloading
```

The graphiql interface is available from your browser at `localhost:8000/graphql`.

An example gql request can be:
```gql
query WeatherEvents {
  earthquakes{
    magnitude
    time
    place
  }
  warings(county:TROMS_OG_FINNMARK, event:SNOW){
    title
    pubDate
    description
  }
}
```
