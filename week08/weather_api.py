"""Small client for WeatherAPI.com plus output formatters."""

import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _get(self, endpoint, params):
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}", params=params, timeout=10
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_current_weather(self, location):
        return self._get("current.json", {"key": self.api_key, "q": location})

    def get_forecast(self, location, days=3):
        if not 1 <= days <= 3:
            raise ValueError("days must be between 1 and 3")
        return self._get(
            "forecast.json", {"key": self.api_key, "q": location, "days": days}
        )


def format_current_weather(data):
    loc = data["location"]
    cur = data["current"]
    return f"{loc['name']}, {loc['country']}: {cur['temp_f']}°F, {cur['condition']['text']}"


def format_forecast(data):
    lines = []
    for day in data["forecast"]["forecastday"]:
        d = day["day"]
        lines.append(
            f"{day['date']}: high {d['maxtemp_f']}°F, low {d['mintemp_f']}°F, "
            f"{d['condition']['text']}"
        )
    return "\n".join(lines)