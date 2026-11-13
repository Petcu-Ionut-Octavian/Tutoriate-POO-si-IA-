# =====================================================
# TUTORIAT IA - EURISTICI, GREEDY SI A*
# Toate exemplele sunt in acelasi fisier.
# Decomentezi apelurile din main dupa nevoie.
# =====================================================

# -----------------------------------------------------
# GRAFUL CU HARTA ROMANIEI
# -----------------------------------------------------

graf = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu', 146)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Rimnicu': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Fagaras': [('Sibiu', 99), ('Bucuresti', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucuresti', 101)],
    'Bucuresti': [('Fagaras', 211), ('Pitesti', 101)]
}

# -----------------------------------------------------
# EURISTICA - DISTANTA AERIANA PANA LA BUCURESTI
# -----------------------------------------------------

h = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Sibiu': 253,
    'Rimnicu': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucuresti': 0
}

# =====================================================
# EXEMPLUL 1 - AFISAREA EURISTICII
# =====================================================

def exemplu_euristica():

    print("Distanta aeriana Arad -> Bucuresti =", h['Arad'])
    print("Distanta aeriana Sibiu -> Bucuresti =", h['Sibiu'])
    print("Distanta aeriana Pitesti -> Bucuresti =", h['Pitesti'])
    print()


# =====================================================
# EXEMPLUL 2 - COMPARAREA A DOUA NODURI
# GREEDY ALEGE h MINIM
# =====================================================

def exemplu_greedy_intuitie():

    candidat1 = "Sibiu"
    candidat2 = "Timisoara"

    h1 = h[candidat1]
    h2 = h[candidat2]

    print(candidat1, "->", h1)
    print(candidat2, "->", h2)

    if h1 < h2:
        print("Greedy alege", candidat1)
    else:
        print("Greedy alege", candidat2)

    print()

# =====================================================
# GREEDY BEST FIRST SEARCH
# f(n) = h(n)
# =====================================================

def greedy(graf, start, scop, euristica):

    frontiera = [(euristica[start], start, [start])]

    vizitat = []

    while frontiera:

        frontiera.sort()

        _, nod, drum = frontiera.pop(0)

        if nod == scop:
            return drum

        if nod not in vizitat:

            vizitat.append(nod)

            for vecin, cost in graf[nod]:

                if vecin not in vizitat:

                    frontiera.append(
                        (euristica[vecin],
                         vecin,
                         drum + [vecin])
                    )

    return None


def exemplu_greedy():

    drum = greedy(
        graf,
        "Arad",
        "Bucuresti",
        h
    )

    print("GREEDY")
    print("Drum:", drum)
    print()


# =====================================================
# EXEMPLUL 3 - g(n)
# COSTUL REAL PARCURS
# =====================================================

def exemplu_g():

    cost = 0

    cost += 140
    print("Arad -> Sibiu =", cost)

    cost += 80
    print("Arad -> Sibiu -> Rimnicu =", cost)

    cost += 97
    print("Arad -> Sibiu -> Rimnicu -> Pitesti =", cost)

    print()


# =====================================================
# EXEMPLUL 4 - h(n)
# ESTIMAREA PANA LA SCOP
# =====================================================

def exemplu_h():

    print("h(Arad) =", h["Arad"])
    print("h(Sibiu) =", h["Sibiu"])
    print("h(Pitesti) =", h["Pitesti"])
    print("h(Bucuresti) =", h["Bucuresti"])

    print()


# =====================================================
# EXEMPLUL 5 - f(n) = g(n)+h(n)
# =====================================================

def exemplu_f():

    g = 220
    h_nod = 193

    f = g + h_nod

    print("g =", g)
    print("h =", h_nod)
    print("f =", f)

    print()


# =====================================================
# ALGORITMUL A*
# =====================================================

def a_star(graf, start, scop, euristica):

    frontiera = [(euristica[start], 0, start, [start])]

    vizitat = []

    while frontiera:

        frontiera.sort()

        f, g, nod, drum = frontiera.pop(0)

        if nod == scop:
            return g, drum

        if nod not in vizitat:

            vizitat.append(nod)

            for vecin, cost in graf[nod]:

                if vecin not in vizitat:

                    g_nou = g + cost
                    f_nou = g_nou + euristica[vecin]

                    frontiera.append(
                        (
                            f_nou,
                            g_nou,
                            vecin,
                            drum + [vecin]
                        )
                    )

    return None


def exemplu_astar():

    cost, drum = a_star(
        graf,
        "Arad",
        "Bucuresti",
        h
    )

    print("A*")
    print("Cost =", cost)
    print("Drum =", drum)

    print()


# =====================================================
# EXEMPLUL 6
# EURISTICA ADMISIBILA
# =====================================================

def exemplu_admisibila():

    cost_real = 200
    euristica = 150

    if euristica <= cost_real:
        print("Euristica este admisibila")

    print()


# =====================================================
# EXEMPLUL 7
# EURISTICA INADMISIBILA
# =====================================================

def exemplu_inadmisibila():

    cost_real = 200
    euristica = 250

    if euristica > cost_real:
        print("Euristica este inadmisibila")

    print()


# =====================================================
# EXEMPLUL 8
# DOMINANTA EURISTICILOR
# =====================================================

def exemplu_dominanta():

    ha = 8
    hc = 5

    print("ha =", ha)
    print("hc =", hc)

    if ha >= hc:
        print("ha domina hc")

    print()


# =====================================================
# MAIN
# =====================================================



exemplu_euristica()

exemplu_greedy_intuitie()

exemplu_greedy()

exemplu_g()

exemplu_h()

exemplu_f()

exemplu_astar()

exemplu_admisibila()

exemplu_inadmisibila()

exemplu_dominanta()

