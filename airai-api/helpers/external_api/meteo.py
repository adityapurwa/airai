from typing import Dict, Any, Optional

import aiohttp


class Meteo:
    variables = [
        "european_aqi",
        "european_aqi_pm2_5",
        "european_aqi_pm10",
        "european_aqi_no2",
        "european_aqi_o3",
        "european_aqi_so2",
    ]

    async def fetch_air_quality(self, city: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Asynchronously fetches air quality data for the given city from the Open Meteo API.

        Args:
            city: A dictionary containing the city's name, latitude, and longitude.

        Returns:
            A dictionary containing the air quality data, or None if the API request failed.
        """
        async with aiohttp.ClientSession() as session:
            url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={city['latitude']}&longitude={city['longitude']}&hourly={','.join(self.variables)}"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    data["city"] = city["name"]
                    return data
                else:
                    print(f"Error: {response.status} {await response.text()}")
                    return None
