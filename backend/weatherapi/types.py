from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: str
    pubDate: str
    author: str

    def __str__(self):
        return self.title

    # lets have the exposed field be snake cased
    @property
    def pub_date(self):
        return self.pubDate

    @classmethod
    def from_element(cls, element):
        props = {child.tag: child.text for child in element.iterchildren()}
        return cls(**props)
