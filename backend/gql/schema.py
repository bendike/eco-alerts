import strawberry
from strawberry.fastapi import GraphQLRouter

from .resolvers import get_alerts
from .types import Alert


@strawberry.type
class Query:
    alerts: list[Alert] = strawberry.field(resolver=get_alerts)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)
