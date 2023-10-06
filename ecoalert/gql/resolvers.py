from ecoalert.earthquakes.selectors import get_earth_quakes_features
from ecoalert.weatherwarnings.selectors import get_warnings

from .types import County, EarthQuake, EventType, Warning


def get_weather_warnings(
    county: County | None = None,
    event: EventType | None = None,
) -> list[Warning]:
    items = get_warnings(
        county=county.value if county else None,
        event=event.value if event else None,
    )
    return [Warning.from_basemodel(item) for item in items]


def get_earthquakes(
    county: County | None = None,
    event: EventType | None = None,
) -> list[EarthQuake]:
    features = get_earth_quakes_features()
    return [EarthQuake.from_basemodel(feature) for feature in features]
