from rx import from_iterable
from rx.operators import flat_map, map, reduce, group_by


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
        # Sumar los puntos del equipo
        reduce(lambda acc, match: acc + SoccerMatch.calculate_match_points(match), 0),
        # Asociar el equipo con sus puntos
        map(lambda total_points: (group.key, total_points))
    )),
    # Aplanar el flujo de observables
    flat_map(lambda x: x)
).subscribe(lambda result: print(f"Team: {result[0]}, Total Points: {result[1]}"))
