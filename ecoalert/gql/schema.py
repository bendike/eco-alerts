import strawberry
from strawberry.fastapi import GraphQLRouter

from .resolvers import get_earthquakes, get_weather_warnings
from .types import EarthQuake, Warning


@strawberry.type
class Query:
    warings: list[Warning] = strawberry.field(
        resolver=get_weather_warnings,
        description="Retrieve active weather warnings based on county and event type. Returns all acive warnings if no args are given.",
    )
    earthquakes: list[EarthQuake] = strawberry.field(
        resolver=get_earthquakes,
        description="Retrieve earthquake information for earthquakes within the last hour.",
    )


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)
