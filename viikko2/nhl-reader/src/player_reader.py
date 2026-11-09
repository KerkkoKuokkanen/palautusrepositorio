import requests
from player import Player

# pylint: disable=too-few-public-methods
class PlayerReader:

    def __init__(self, season):
        self.url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    def get_players(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            data = response.json()

            if not isinstance(data, list):
                return []

            return [Player(player_dict) for player_dict in data]

        except (requests.RequestException, ValueError):
            return []
