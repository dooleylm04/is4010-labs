"""Persistent, case-insensitive storage of favorite locations."""

import json


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = self._load()

    def _load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            return {}
        if not isinstance(data, dict):
            return {}
        return {str(k).lower(): v for k, v in data.items()}

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.favorites, f, indent=2)

    def add(self, name, location):
        key = name.lower()
        if key in self.favorites:
            return False
        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        key = name.lower()
        if key not in self.favorites:
            return False
        del self.favorites[key]
        self._save()
        return True

    def list_all(self):
        return dict(self.favorites)

    def get_location(self, name):
        return self.favorites.get(name.lower())