class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']

    def __str__(self):
        points = self.goals+self.assists
        return f"{self.name:<20}{self.team:<15}{self.goals} + {self.assists} = {points}"