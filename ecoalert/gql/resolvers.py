from ecoalert.earthquakes.selectors import get_earth_quakes_features
from ecoalert.weatherwarnings.selectors import get_warnings

from .types import County, EarthQuake, EventType, Warning


async def get_weather_warnings(
    county: County | None = None,
    event: EventType | None = None,
) -> list[Warning]:
    items = await get_warnings(
        county=county.value if county else None,
        event=event.value if event else None,
    )
    return [Warning.from_basemodel(item) for item in items]


async def get_earthquakes() -> list[EarthQuake]:
    features = await get_earth_quakes_features()
    return [EarthQuake.from_basemodel(feature) for feature in features]
