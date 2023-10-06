import json

import httpx

from ecoalert.earthquakes.types import EarthQuakeFeatures


async def get_earth_quakes_features() -> list[EarthQuakeFeatures]:
    EXTERNAL_API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"  # noqa
    async with httpx.AsyncClient() as client:
        response = await client.get(EXTERNAL_API_URL)

    data = json.loads(response.text)
    features = data["features"]

    return [
        EarthQuakeFeatures.from_dict(
            feature["properties"],
        )
        for feature in features
    ]
