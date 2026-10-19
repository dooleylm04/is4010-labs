"""Command-line weather application."""

import argparse
import os
import sys
from pathlib import Path

try:
    from week08.favorites import FavoritesManager
    from week08.weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = Path(__file__).with_name("favorites.json")
PLACEHOLDER_KEY = "YOUR_API_KEY_HERE"


def load_api_key():
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
    try:
        try:
            from week08 import config
        except ImportError:
            import config
    except ImportError:
        return None
    key = getattr(config, "WEATHER_API_KEY", None)
    if not key or key == PLACEHOLDER_KEY:
        return None
    return key


def build_parser():
    parser = argparse.ArgumentParser(description="Weather from WeatherAPI.com")
    sub = parser.add_subparsers(dest="command", required=True)

    current = sub.add_parser("current", help="Show current weather")
    current.add_argument("location")

    forecast = sub.add_parser("forecast", help="Show a 1-3 day forecast")
    forecast.add_argument("location")
    forecast.add_argument("--days", type=int, default=3, choices=[1, 2, 3])

    fav = sub.add_parser("favorites", help="Manage favorite locations")
    fav_sub = fav.add_subparsers(dest="favorites_command", required=True)
    fav_add = fav_sub.add_parser("add")
    fav_add.add_argument("name")
    fav_add.add_argument("location")
    fav_sub.add_parser("list")
    fav_remove = fav_sub.add_parser("remove")
    fav_remove.add_argument("name")

    return parser


def handle_favorites(args, favorites):
    if args.favorites_command == "add":
        if not favorites.add(args.name, args.location):
            print(f"Error: favorite '{args.name}' already exists.", file=sys.stderr)
            return 1
        print(f"Added {args.name}: {args.location}")
        return 0
    if args.favorites_command == "remove":
        if not favorites.remove(args.name):
            print(f"Error: favorite '{args.name}' not found.", file=sys.stderr)
            return 1
        print(f"Removed {args.name}")
        return 0
    # list
    items = favorites.list_all()
    if not items:
        print("No favorites saved.")
    for name, location in items.items():
        print(f"{name}: {location}")
    return 0


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        return handle_favorites(args, favorites)

    api_key = load_api_key()
    if not api_key:
        print("Error: no API key found. Set WEATHER_API_KEY or create week08/config.py.",
              file=sys.stderr)
        return 1

    client = WeatherAPI(api_key)
    location = favorites.get_location(args.location) or args.location

    if args.command == "current":
        data = client.get_current_weather(location)
        formatter = format_current_weather
    else:
        data = client.get_forecast(location, days=args.days)
        formatter = format_forecast

    if data is None:
        print(f"Error: could not get weather for '{location}'.", file=sys.stderr)
        return 1
    print(formatter(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())