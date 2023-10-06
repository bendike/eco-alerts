import strawberry
from strawberry.fastapi import GraphQLRouter

from .resolvers import get_earthquakes, get_weather_warnings
from .types import EarthQuake, Warning


@strawberry.type
class Query:
    warings: list[Warning] = strawberry.field(resolver=get_weather_warnings)
    earthquakes: list[EarthQuake] = strawberry.field(resolver=get_earthquakes)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)
