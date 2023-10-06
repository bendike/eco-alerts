import json

import requests

from ecoalert.earthquakes.types import EarthQuakeFeatures


def get_earth_quakes_features() -> list[EarthQuakeFeatures]:
    EXTERNAL_API_URL = (
        "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"
    )
    response = requests.get(EXTERNAL_API_URL)

    data = json.loads(response.text)
    features = data["features"]

    return [
        EarthQuakeFeatures.from_dict(
            feature["properties"],
        )
        for feature in features
    ]
