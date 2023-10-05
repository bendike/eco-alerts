import strawberry

from backend.weatherapi.types import Item


@strawberry.type
class Alert:
    title: str
    description: str
    link: str
    author: str

    @classmethod
    def from_basemodel(cls, basemodel: Item):
        return cls(
            title=basemodel.title,
            description=basemodel.description,
            link=basemodel.link,
            author=basemodel.author,
        )
