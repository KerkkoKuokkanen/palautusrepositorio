
# pylint: disable=too-few-public-methods
class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_goal_scorers(self, how_many):
        self.players.sort(key=lambda p: p.goals, reverse=True)
        return self.players[:how_many]

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [
                player for player in self.players if player.nationality == nationality
            ]
        filtered_players.sort(key=lambda p: p.points, reverse=True)
        return filtered_players
