import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # yhteensä 16
            Player("Lemieux", "PIT", 45, 54), # yhteensä 99
            Player("Kurri",   "EDM", 37, 53), # yhteensä 90
            Player("Yzerman", "DET", 42, 56), # yhteensä 98
            Player("Gretzky", "EDM", 35, 89)  # yhteensä 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # injektoidaan stub-luokka (ei verkkoyhteyttä)
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_returns_none(self):
        player = self.stats.search("Pekka")
        self.assertIsNone(player)

    def test_team_returns_all_players(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team),3)

    def test_top_returns_correct_order_points(self):
        top_players = self.stats.top(1, SortBy.POINTS )
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_returns_correct_order_goals(self):
        top_players = self.stats.top(1, SortBy.GOALS )
        self.assertEqual(top_players[0].name, "Lemieux")

    def test_top_returns_correct_order_assists(self):
        top_players = self.stats.top(1, SortBy.ASSISTS )
        self.assertEqual(top_players[0].name, "Gretzky")

