"""
    It is a Greedy Algorithm
    The Time Complexity of this Greedy Algorithm (Set Cover Problem): O(n * m), 
    where n is the number of stations and m is the number of states.
    A Greedy Algorithm is a problem-solving approach that makes the locally optimal choice at each step,
    aiming to find a global optimum.
    This specific algorithm finds the minimum set of stations required to cover all desired states.
"""

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az']),
}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)


