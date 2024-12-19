# Calculo de Estadísticas de Partidos de Fútbol

Usando programación reactiva, en este ejemplo calculamos las estadísticas de los encuentros de distintos equipos de futbol, en este caso: Real Madrid, Barcelona y Atlético de Madrid.

Dado un lista (matches) de datos de un juego `SoccerMatch(team, goals_scored, goals_againts)`, el programa calcula los puntos y la diferencia de goles entre todos los partidos de un equipo.

### Requerimientos del sistema:

1. Los puntos por partido se dan de la siguiente manera:
    - Si los goles a favor (goals_scored) son mayores a los goles en contra (goals_againts) el equipo suma 3 puntos.
    - Si los goles a favor (goals_scored) son iguales a los goles en contra (goals_againts) el equipo suma 1 puntos.
    - Si los goles a favor (goals_scored) son menores a los goles en contra (goals_againts) el equipo no suma puntos.
2. El resultado final mostrado debe devolver los equipos en orden descendente por puntos y por diferencia de goles.

## Ejecutar el ejemplo:

Dentro de la raiz del proyecto _task_3/_, ejecutamos los siguientes comandos en el mismo orden:

1. Para construir la imagen de docker  
    `make build`
2. Para correr el contenedor con la imagen construida previamente y objetener los resultados  
    `make run`

Al finalizar, el programa devolverá los siguientes resultados:
```
---------- Real Madrid ----------
Total Points: 6
Goals Scored: 5
Goals Against: 1
Goal Difference: 4
---------- Barcelona ----------
Total Points: 1
Goals Scored: 1
Goals Against: 3
Goal Difference: -2
---------- Atletico Madrid ----------
Total Points: 1
Goals Scored: 0
Goals Against: 2
Goal Difference: -2
```
