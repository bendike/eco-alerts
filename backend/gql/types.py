from datetime import datetime
from decimal import Decimal
from enum import Enum

import strawberry

from backend.earthquakes.types import EarthQuakeFeatures
from backend.weatherapi.types import Item

##############
# weatherapi #
##############


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


@strawberry.enum
class County(Enum):
    VIKEN = "30"
    OSLO = "03"
    INNLANDET = "34"
    VESTFOLD_OG_TELEMARK = "38"
    AGDER = "42"
    ROGALAND = "11"
    VESTLAND = "46"
    MORE_OG_ROMSDAL = "15"
    TRONDELAG = "50"
    NORDLAND = "18"
    TROMS_OG_FINNMARK = "54"


@strawberry.enum
class EventType(Enum):
    BLOWING_SNOW = "blowingSnow"
    FOREST_FIRE = "forestFire"
    GALE = "gale"
    ICE = "ice"
    ICING = "icing"
    LIGHTNING = "lightning"
    POLAR_LOW = "polarLow"
    RAIN = "rain"
    RAIN_FLOOD = "rainFlood"
    SNOW = "snow"
    STORM_SURGE = "stormSurge"
    WIND = "wind"


##############
# earthquakes #
##############


@strawberry.type
class EarthQuake:
    magnitude: Decimal
    place: str
    time: datetime

    @classmethod
    def from_basemodel(cls, basemodel: EarthQuakeFeatures):
        return cls(
            magnitude=basemodel.mag,
            place=basemodel.place,
            time=basemodel.time,
        )
