def minimax(nod, max_player):
    if isinstance(nod, int):
        return nod

    if max_player:
        return max(minimax(copil, False) for copil in nod)
    else:
        return min(minimax(copil, True) for copil in nod)


arbore = [
    [
        [3, 5],
        [6, 9]
    ],
    [
        [1, 2],
        [0, -1]
    ]
]

print("Valoarea MiniMax =", minimax(arbore, True))



#%%



def alpha_beta(nod, alpha, beta, max_player):
    if isinstance(nod, int):
        return nod

    if max_player:
        valoare = float("-inf")

        for copil in nod:
            valoare = max(
                valoare,
                alpha_beta(copil, alpha, beta, False)
            )

            alpha = max(alpha, valoare)

            if beta <= alpha:
                break

        return valoare

    else:
        valoare = float("inf")

        for copil in nod:
            valoare = min(
                valoare,
                alpha_beta(copil, alpha, beta, True)
            )

            beta = min(beta, valoare)

            if beta <= alpha:
                break

        return valoare


arbore = [
    [
        [3, 5],
        [6, 9]
    ],
    [
        [1, 2],
        [0, -1]
    ]
]

print(
    "Valoarea Alpha-Beta =",
    alpha_beta(
        arbore,
        float("-inf"),
        float("inf"),
        True
    )
)






#%%


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

noduri = {
    "MAX": (0, 3),

    "MIN1": (-3, 2),
    "MIN2": (3, 2),

    "MAX1": (-4.5, 1),
    "MAX2": (-1.5, 1),
    "MAX3": (1.5, 1),
    "MAX4": (4.5, 1),

    "3": (-5.2, 0),
    "5": (-3.8, 0),

    "6": (-2.2, 0),
    "9": (-0.8, 0),

    "1": (0.8, 0),
    "2": (2.2, 0),

    "0": (3.8, 0),
    "-1": (5.2, 0),
}

muchii = [
    ("MAX", "MIN1"),
    ("MAX", "MIN2"),

    ("MIN1", "MAX1"),
    ("MIN1", "MAX2"),

    ("MIN2", "MAX3"),
    ("MIN2", "MAX4"),

    ("MAX1", "3"),
    ("MAX1", "5"),

    ("MAX2", "6"),
    ("MAX2", "9"),

    ("MAX3", "1"),
    ("MAX3", "2"),

    ("MAX4", "0"),
    ("MAX4", "-1"),
]

for a, b in muchii:
    x1, y1 = noduri[a]
    x2, y2 = noduri[b]
    ax.plot([x1, x2], [y1, y2], "k", linewidth=2, alpha=0.1)

for nume, (x, y) in noduri.items():
    ax.scatter(x, y, s=1200, color="lightblue", edgecolors="black")
    ax.text(x, y, nume, ha="center", va="center", fontsize=10)

ax.set_title("Arbore MiniMax", fontsize=14)
ax.axis("off")

plt.tight_layout()
plt.show()
