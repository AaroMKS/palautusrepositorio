from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, Or, HasFewerThan

def main():
    url = " https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query
            .one_of(
            query.plays_in("PHI")
                .has_at_least(10, "assists")
                .has_fewer_than(10, "goals"),
            query.plays_in("EDM")
                .has_at_least(50, "points")
            )
            .build()
)

    for player in stats.matches(matcher):
        print(player)


class QueryBuilder:
    def __init__(self, matcher=None):
        if matcher is None:
            self._matcher = All()
        else:
            self._matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(
            And(self._matcher, PlaysIn(team))
        )

    def has_at_least(self, value, attr):
        return QueryBuilder(
            And(self._matcher, HasAtLeast(value, attr))
        )

    def has_fewer_than(self, value, attr):
        return QueryBuilder(
            And(self._matcher, HasFewerThan(value, attr))
        )
    def one_of(self, *queries):
        matchers = [query.build() for query in queries]
        return QueryBuilder(
            Or(*matchers)
        )
    def build(self):
        return self._matcher

if __name__ == "__main__":
    main()
