import strawberry
from strawberry.fastapi import GraphQLRouter

from .resolvers import get_alerts, get_earth_quakes
from .types import Alert, EarthQuake


@strawberry.type
class Query:
    alerts: list[Alert] = strawberry.field(resolver=get_alerts)
    earthquakes: list[EarthQuake] = strawberry.field(resolver=get_earth_quakes)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)
