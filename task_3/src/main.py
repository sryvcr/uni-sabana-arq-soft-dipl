from rx import from_iterable
from rx.operators import flat_map, group_by, map, reduce, to_list


class SoccerMatch:
    def __init__(self, team: str, goals_scored: int, goals_againts: int):
        self._team = team
        self._goals_scored = goals_scored
        self._goals_againts = goals_againts

    def get_team(self) -> str:
        return self._team

    def get_goals_scored(self) -> int:
        return self._goals_scored

    def get_goals_againts(self) -> int:
        return self._goals_againts

    def calculate_match_points(self) -> int:
        # Partido ganado
        if self.get_goals_scored() > self.get_goals_againts():
            return 3
        # Partido empatado
        elif self.get_goals_scored() == self.get_goals_againts():
            return 1
        # Partido perdido
        else:
            return 0


# Lista de partidos
matches = [
    SoccerMatch("Real Madrid", 2, 0),
    SoccerMatch("Barcelona", 1, 3),
    SoccerMatch("Atletico Madrid", 0, 0),
    SoccerMatch("Atletico Madrid", 0, 2),
    SoccerMatch("Barcelona", 0, 0),
    SoccerMatch("Real Madrid", 3, 1),
]

# Agrupar las estadisticas por equipo
from_iterable(matches).pipe(
    # Agrupar partidos por equipo
    group_by(lambda match: match.get_team()),
    map(lambda group: group.pipe(
        # Sumar los puntos del equipo, goles a favor y en contra
        reduce(
            lambda acc, match: {
                "team": group.key,
                "total_points": acc["total_points"] + match.calculate_match_points(),
                "total_goals_scored": acc["total_goals_scored"] + match.get_goals_scored(),
                "total_goals_against": acc["total_goals_against"] + match.get_goals_againts(),
            },
            {
                "team": group.key,
                "total_points": 0,
                "total_goals_scored": 0,
                "total_goals_against": 0
            }
        ),
    )),
    # Aplanar el flujo de observables
    flat_map(lambda x: x),
    # Convierte el flujo a una lista para poder ordenarla
    to_list(),
    # Ordenar por puntos totales y diferencia de goles
    map(lambda teams: sorted(
        teams,
        key=lambda team: (
            team["total_points"],
            team["total_goals_scored"] - team["total_goals_against"],
        ),
        reverse=True,
    ))
).subscribe(
    lambda sorted_teams: [
        print(
            f"---------- {team['team']} ----------\n"
            f"Total Points: {team['total_points']}\n"
            f"Goals Scored: {team['total_goals_scored']}\n"
            f"Goals Against: {team['total_goals_against']}\n"
            f"Goal Difference: {team['total_goals_scored'] - team['total_goals_against']}"
        )
        for team in sorted_teams
    ]
)
