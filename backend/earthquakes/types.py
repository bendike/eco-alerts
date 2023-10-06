from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class EarthQuakeFeatures(BaseModel):
    mag: Decimal
    place: str
    time: datetime

    def __str__(self):
        return self.title

    @classmethod
    def from_dict(cls, properties):
        return cls(**properties)
