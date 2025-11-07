import requests
from player import Player
from rich.console import Console
from rich.table import Table
console = Console()
def main():
    season = input("Season: ")
    nationality = input("Nationality: ").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players=stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Released", justify="left", style="cyan", no_wrap=True)
    table.add_column("teams", justify="center", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        total = player.goals + player.assists
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(total))
    console.print(table)

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()
        players = [Player(player_dict) for player_dict in response]
        return players

class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        team_members = [i for i in self._players if i.nationality == nationality]
        sort = sorted(team_members, key=lambda points: points.goals + points.assists, reverse = True)
        return sort

if __name__ == "__main__":
    main()
