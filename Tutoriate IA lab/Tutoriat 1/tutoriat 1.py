# =====================================
# GRAF EXEMPLU
# =====================================

graf = {
    'A': ['B', 'C'],

    'B': ['A', 'D', 'E'],

    'C': ['A', 'F'],

    'D': ['B'],

    'E': ['B', 'G'],

    'F': ['C'],

    'G': ['E']
}

start = 'A'
goal = 'G'

# =====================================
# BFS
# Frontiera = Queue (FIFO)
# =====================================

def bfs(graf, start, goal):

    frontiera = [(start, [start])]
    vizitat = []

    while frontiera:

        nod, drum = frontiera.pop(0)

        if nod == goal:
            return drum

        if nod not in vizitat:

            vizitat.append(nod)

            for vecin in graf[nod]:
                frontiera.append(
                    (vecin, drum + [vecin])
                )

    return None


# =====================================
# DFS
# Frontiera = Stack (LIFO)
# =====================================

def dfs(graf, start, goal):

    frontiera = [(start, [start])]
    vizitat = []

    while frontiera:

        nod, drum = frontiera.pop()

        if nod == goal:
            return drum

        if nod not in vizitat:

            vizitat.append(nod)

            for vecin in reversed(graf[nod]):   #graf[nod][::-1]
                frontiera.append(
                    (vecin, drum + [vecin])
                )

    return None


# =====================================
# DLS
# DFS cu limita
# =====================================

def dls(graf, nod, goal, limita, drum, vizitat):

    if nod == goal:
        return drum

    if limita == 0:
        return None

    vizitat.append(nod)

    for vecin in graf[nod]:

        if vecin not in vizitat:

            rezultat = dls(
                graf,
                vecin,
                goal,
                limita - 1,
                drum + [vecin],
                vizitat
            )

            if rezultat is not None:
                return rezultat

    return None


# =====================================
# IDS
# DLS cu limite crescatoare
# =====================================

def ids(graf, start, goal, adancime_maxima):

    for limita in range(adancime_maxima + 1):

        rezultat = dls(
            graf,
            start,
            goal,
            limita,
            [start],
            []
        )

        if rezultat is not None:
            return rezultat

    return None


# =====================================
# GRAF CU COSTURI PENTRU UCS
# =====================================

graf_cost = {
    'A': [('B', 1), ('C', 5)],

    'B': [('A', 1),
          ('D', 2),
          ('E', 1)],

    'C': [('A', 5),
          ('F', 1)],

    'D': [('B', 2)],

    'E': [('B', 1),
          ('G', 1)],

    'F': [('C', 1)],

    'G': [('E', 1)]
}


# =====================================
# UCS
# Frontiera = lista ordonata dupa cost
# =====================================

def ucs(graf, start, goal):

    frontiera = [(0, start, [start])]
    vizitat = []

    while frontiera:

        # alegem nodul cu cost minim
        frontiera.sort()

        cost, nod, drum = frontiera.pop(0)

        if nod == goal:
            return cost, drum

        if nod not in vizitat:

            vizitat.append(nod)

            for vecin, c in graf[nod]:

                frontiera.append(
                    (
                        cost + c,
                        vecin,
                        drum + [vecin]
                    )
                )

    return None


# =====================================
# APELURI
# =====================================

print("===== BFS =====")
print(bfs(graf, start, goal))
print()

print("===== DFS =====")
print(dfs(graf, start, goal))
print()

print("===== DLS (limita = 2) =====")
print(dls(graf, start, goal, 2, [start],[]))
print()

print("===== DLS (limita = 3) =====")
print(dls(graf, start, goal, 3, [start],[]))
print()

print("===== IDS =====")
print(ids(graf, start, goal, 10))
print()

print("===== UCS =====")
print(ucs(graf_cost, start, goal))
print()