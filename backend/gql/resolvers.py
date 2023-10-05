
from backend.gql.types import Alert
from backend.weatherapi.selectors import get_items


def get_alerts() -> list[Alert]:
    items = get_items()
    return [Alert.from_basemodel(item) for item in items]
