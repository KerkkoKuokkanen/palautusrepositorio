
import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player_test(self):
        p = self.stats.search("Semenko")
        self.assertEqual(p.name, "Semenko")
        self.assertEqual(p.team, "EDM")
        self.assertEqual(p.goals, 4)
        self.assertEqual(p.assists, 12)

    def test_no_player(self):
        p = self.stats.search("Samu")
        self.assertIsNone(p)

    def test_team_search(self):
        p = self.stats.team("EDM")
        self.assertEqual(p[0].name, "Semenko")
        self.assertEqual(p[1].name, "Kurri")
        self.assertEqual(p[2].name, "Gretzky")

    def test_top(self):
        p = self.stats.top(3)
        self.assertEqual(p[0].name, "Gretzky")
        self.assertEqual(p[1].name, "Lemieux")
        self.assertEqual(p[2].name, "Yzerman")

    def test_top_points(self):
        p = self.stats.top(3, 1)
        self.assertEqual(p[0].name, "Gretzky")
        self.assertEqual(p[1].name, "Lemieux")
        self.assertEqual(p[2].name, "Yzerman")

    def test_top_goals(self):
        p = self.stats.top(3, 2)
        self.assertEqual(p[0].name, "Lemieux")
        self.assertEqual(p[1].name, "Yzerman")
        self.assertEqual(p[2].name, "Kurri")

    def test_top_assists(self):
        p = self.stats.top(3, 3)
        self.assertEqual(p[0].name, "Gretzky")
        self.assertEqual(p[1].name, "Yzerman")
        self.assertEqual(p[2].name, "Lemieux")
