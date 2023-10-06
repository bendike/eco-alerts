from io import StringIO

import requests
from lxml import etree

from .types import WeatherWarning


def get_warnings(
    county: str | None = None,
    event: str | None = None,
) -> list[WeatherWarning]:
    EXTERNAL_API_URL = _build_url(county, event)

    # Use requests to deal with https
    response = requests.get(EXTERNAL_API_URL)
    xml_str = response.text

    # The parse method needs a file, not a string.
    # So use StringIO.
    tree = etree.parse(StringIO(xml_str))

    items = list(tree.getroot().iter("item"))

    return [WeatherWarning.from_element(element=item) for item in items]


def _build_search_params(county: str | None, event: str | None) -> str:
    params = []
    if county:
        params.append(f"county={county}")
    if event:
        params.append(f"event={event}")
    return "?" + "&".join(params) if params else ""


def _build_url(county: str | None, event: str | None) -> str:
    return "https://api.met.no/weatherapi/metalerts/1.1/" + _build_search_params(
        county,
        event,
    )
