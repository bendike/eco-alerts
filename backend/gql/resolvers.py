
from backend.gql.types import Alert
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
