from io import StringIO

import requests
from lxml import etree

from backend.weatherapi.types import Item


def get_items() -> list[Item]:
    EXTERNAL_API_URL = "https://api.met.no/weatherapi/metalerts/1.1/"

    # Use requests to deal with https
    response = requests.get(EXTERNAL_API_URL)
    xml_str = response.text

    # The parse method needs a file, not a string.
    # So use StringIO.
    tree = etree.parse(StringIO(xml_str))

    items = list(tree.getroot().iter("item"))

    return [Item.from_element(element=item) for item in items]
