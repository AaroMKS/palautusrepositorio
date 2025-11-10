class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.nationality = player_dict['nationality']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']

    def __str__(self):
        points = self.goals+self.assists
        return f"{self.name:<20}{self.team:<15}{self.goals} + {self.assists} = {points}"
