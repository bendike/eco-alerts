import strawberry

from backend.weatherapi.types import Item


@strawberry.type
class Alert:
    title: str
    description: str
    pub_date: str
    author: str

    @classmethod
    def from_basemodel(cls, basemodel: Item):
        return cls(
            title=basemodel.title,
            description=basemodel.description,
            pub_date=basemodel.pub_date,
            author=basemodel.author,
        )
