def saisir(msg):
    return float(input(msg))

def choisir_duree():
    print("Base: 1=360j  2=365j  3=12mois")
    base = {1:360,2:365,3:12}[int(input("Base: "))]
    n = float(input("Duree n: "))
    return n, base

def date2(msg):
    if msg:
        print(msg)
    j = int(input("  Jour: "))
    m = int(input("  Mois (1-12): "))
    return j, m

def qz_apres_versement(j, m):
    if j <= 15:
        return 16, m
    else:
        m2 = m + 1
        if m2 > 12:
            m2 = 1
        return 1, m2

def qz_avant_retrait(j, m):
    if j <= 15:
        return 1, m
    else:
        return 16, m

def qz_entre(j1, m1, j2, m2):
    def num(j, m):
        return (m - 1) * 2 + (0 if j == 1 else 1)
    return num(j2, m2) - num(j1, m1)

def nb_jours(j1, m1, j2, m2):
    jours_mois = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    d1 = sum(jours_mois[1:m1]) + j1
    d2 = sum(jours_mois[1:m2]) + j2
    return d2 - d1

def util_dates():
    while True:
        print("-- UTILITAIRE DATES --")
        print("1. Nb jours entre 2 dates")
        print("2. Quinzaine apres versement")
        print("3. Quinzaine avant retrait")
        print("4. Nb quinzaines entre 2 dates")
        print("0. Retour")
        c = int(input("Choix: "))
        if c == 0:
            break
        elif c == 1:
            print("Date 1:")
            j1, m1 = date2("")
            print("Date 2:")
            j2, m2 = date2("")
            print("Nb jours =", nb_jours(j1,m1,j2,m2))
        elif c == 2:
            j, m = date2("Date versement:")
            ej, em = qz_apres_versement(j, m)
            print("Effective:", ej, "/", em)
        elif c == 3:
            j, m = date2("Date retrait:")
            ej, em = qz_avant_retrait(j, m)
            print("Effective:", ej, "/", em)
        elif c == 4:
            print("Date 1 (j=1 ou 16):")
            j1, m1 = date2("")
            print("Date 2 (j=1 ou 16):")
            j2, m2 = date2("")
            print("Quinzaines =", qz_entre(j1,m1,j2,m2))
