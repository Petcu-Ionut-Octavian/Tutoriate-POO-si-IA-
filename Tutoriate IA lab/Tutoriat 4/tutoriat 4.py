import pandas as pd


# ========================================================
# EXEMPLUL 1 - DISTRIBUȚIE DE PROBABILITATE
# ========================================================

def ex1_distributie():

    df = pd.DataFrame({
        "Stare": [
            "Soare",
            "Ploaie",
            "Ninsoare",
            "Furtuna"
        ],
        "Probabilitate": [
            0.50,
            0.30,
            0.15,
            0.05
        ]
    })

    print(df)

# ex1_distributie()


# ========================================================
# EXEMPLUL 2 - VERIFICAREA UNEI DISTRIBUȚII
# ========================================================

def ex2_verificare_distributie():

    df = pd.DataFrame({
        "Eveniment": [
            "A",
            "B",
            "C",
            "D"
        ],
        "Probabilitate": [
            0.20,
            0.30,
            0.10,
            0.40
        ]
    })

    print(df)

    print("\nSuma probabilităților:")
    print(df["Probabilitate"].sum())

# ex2_verificare_distributie()


# ========================================================
# EXEMPLUL 3 - REPARTIȚIE MARGINALĂ
# ========================================================

def ex3_marginalizare():

    df = pd.DataFrame({
        "Ploaie": [
            "Da",
            "Da",
            "Nu",
            "Nu"
        ],
        "Trafic": [
            "Mare",
            "Mic",
            "Mare",
            "Mic"
        ],
        "Probabilitate": [
            0.40,
            0.10,
            0.20,
            0.30
        ]
    })

    print("Distribuția comună\n")
    print(df)

    marginala = (
        df.groupby("Ploaie")
        ["Probabilitate"]
        .sum()
        .reset_index()
    )

    print("\nDistribuția marginală\n")
    print(marginala)

# ex3_marginalizare()


# ========================================================
# EXEMPLUL 4 - PROBABILITATE CONDIȚIONATĂ
# ========================================================

def ex4_probabilitate_conditionata():

    p_a = 0.60
    p_b = 0.30
    p_a_intersect_b = 0.24

    df = pd.DataFrame({
        "Mărime": [
            "P(A)",
            "P(B)",
            "P(A ∩ B)"
        ],
        "Valoare": [
            p_a,
            p_b,
            p_a_intersect_b
        ]
    })

    print(df)

    p_a_given_b = (
        p_a_intersect_b
        / p_b
    )

    print("\nP(A|B) =", p_a_given_b)

# ex4_probabilitate_conditionata()


# ========================================================
# EXEMPLUL 5 - FORMULA DE ÎNMULȚIRE
# ========================================================

def ex5_formula_inmultire():

    df = pd.DataFrame({
        "Probabilitate": [
            "P(Ploaie)",
            "P(Trafic Mare | Ploaie)"
        ],
        "Valoare": [
            0.30,
            0.80
        ]
    })

    print(df)

    rezultat = 0.30 * 0.80

    print(
        "\nP(Trafic Mare ∩ Ploaie) =",
        rezultat
    )

# ex5_formula_inmultire()


# ========================================================
# EXEMPLUL 6 - NORMALIZARE
# ========================================================

def ex6_normalizare():

    df = pd.DataFrame({
        "Ipoteza": [
            "A",
            "B",
            "C"
        ],
        "Valoare ne-normalizată": [
            0.30,
            0.20,
            0.10
        ]
    })

    suma = df[
        "Valoare ne-normalizată"
    ].sum()

    df["Valoare normalizată"] = (
        df["Valoare ne-normalizată"]
        / suma
    )

    print(df)

    print(
        "\nSumă după normalizare:",
        df["Valoare normalizată"].sum()
    )

# ex6_normalizare()


# ========================================================
# EXEMPLUL 7 - REGULA LUI BAYES
# ========================================================

def ex7_bayes():

    df = pd.DataFrame({
        "Probabilitate": [
            "P(Boala)",
            "P(Test+ | Boala)",
            "P(Test+)"
        ],
        "Valoare": [
            0.01,
            0.90,
            0.0585
        ]
    })

    print(df)

    rezultat = (
        0.90 * 0.01
    ) / 0.0585

    print(
        "\nP(Boala | Test+) =",
        round(rezultat, 4)
    )

# ex7_bayes()


# ========================================================
# EXEMPLUL 8 - INDEPENDENȚĂ
# ========================================================

def ex8_independenta():

    p_a = 0.5
    p_b = 0.4

    df = pd.DataFrame({
        "Expresie": [
            "P(A)",
            "P(B)",
            "P(A∩B)",
            "P(A)·P(B)"
        ],
        "Valoare": [
            p_a,
            p_b,
            0.20,
            p_a * p_b
        ]
    })

    print(df)

# ex8_independenta()


# ========================================================
# EXEMPLUL 9 - INDEPENDENȚĂ CONDIȚIONATĂ
# ========================================================

def ex9_independenta_conditionata():

    df = pd.DataFrame({
        "Variabila A": [
            "Ploaie"
        ],
        "Variabila B": [
            "Întârziere"
        ],
        "Condiție": [
            "Trafic"
        ]
    })

    print(df)

# ex9_independenta_conditionata()


# ========================================================
# EXEMPLUL 10 - REGULA DE ÎNLĂNȚUIRE
# ========================================================

def ex10_chain_rule():

    p_c = 0.5
    p_b_c = 0.6
    p_a_b_c = 0.8

    df = pd.DataFrame({
        "Probabilitate": [
            "P(C)",
            "P(B|C)",
            "P(A|B,C)"
        ],
        "Valoare": [
            p_c,
            p_b_c,
            p_a_b_c
        ]
    })

    print(df)

    rezultat = (
        p_c
        * p_b_c
        * p_a_b_c
    )

    print(
        "\nP(A,B,C) =",
        rezultat
    )

# ex10_chain_rule()


# ========================================================
# EXEMPLUL 11 - REȚEA BAYESIANĂ
# ========================================================

def ex11_retea_bayesiana():

    df = pd.DataFrame({
        "Nod": [
            "Boala",
            "Febra",
            "Tuse",
            "Test Pozitiv",
            "Diagnostic",
            "Tratament"
        ],
        "Parinte": [
            "-",
            "Boala",
            "Boala",
            "Boala",
            "Boala, Febra, Tuse, Test Pozitiv",
            "Diagnostic"
        ]
    })

    print(df)

# ex11_retea_bayesiana()


# ========================================================
# EXEMPLUL 12 - CPT - Conditional Probability Table
# ========================================================

def ex12_cpt():

    df = pd.DataFrame({
        "Ploaie": [
            "Da",
            "Nu"
        ],
        "P(Trafic=Mare)": [
            0.80,
            0.20
        ],
        "P(Trafic=Mic)": [
            0.20,
            0.80
        ]
    })

    print(df)

# ex12_cpt()