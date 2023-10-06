from backend.earthquakes.selectors import get_earth_quakes_features
from backend.gql.types import Alert, County, EarthQuake, EventType
from backend.weatherapi.selectors import get_items


def get_alerts(
    county: County | None = None,
    event: EventType | None = None,
) -> list[Alert]:
    items = get_items(
        county=county.value if county else None,
        event=event.value if event else None,
    )
    return [Alert.from_basemodel(item) for item in items]


def get_earth_quakes(
    county: County | None = None,
    event: EventType | None = None,
) -> list[Alert]:
    features = get_earth_quakes_features()
    return [EarthQuake.from_basemodel(feature) for feature in features]
