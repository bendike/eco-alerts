from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str
    link: str
    author: str

    def __str__(self):
        return self.title

    @classmethod
    def from_element(cls, element):
        props = {child.tag: child.text for child in element.iterchildren()}
        return cls(**props)
