import math
from outils import *

def f3e1():
    print("=== F3E1: Capital annuites ===")
    a = saisir("Annuite a: ")
    t = saisir("Taux (ex 0.06): ")
    n = int(input("Nb annuites: "))
    Sn = a * ((1 + t) ** n - 1) / t
    print("a) Sn =", round(Sn, 4))
    k = int(input("Capitaliser k periodes (0=non): "))
    if k > 0:
        print("b) Sn+k =", round(Sn * (1 + t) ** k, 4))

def f3e2():
    print("=== F3E2: Trouver annuite (Sn) ===")
    Sn = saisir("Capital cible Sn: ")
    t = saisir("Taux (ex 0.057): ")
    n = int(input("Nb versements: "))
    a = Sn * t / ((1 + t) ** n - 1)
    print("Annuite a =", round(a, 4))

def f3e3():
    print("=== F3E3: Trouver nb periodes ===")
    a = saisir("Mensualite: ")
    V0 = saisir("Capital emprunte V0: ")
    ta = saisir("Taux annuel (ex 0.06): ")
    print("1=prop(immo) 2=equiv(conso)")
    c = int(input("Choix: "))
    if c == 1:
        tm = ta / 12
    else:
        tm = (1 + ta) ** (1 / 12) - 1
    n = -math.log(1 - V0 * tm / a) / math.log(1 + tm)
    print("Taux mensuel =", round(tm * 100, 6), "%")
    print("n =", round(n, 4), "mois")
    print("Entier:", math.ceil(n))

def f3e4():
    print("=== F3E4: Trouver taux ===")
    V0 = saisir("Capital V0: ")
    a = saisir("Annuite: ")
    n = int(input("Nb annuites: "))
    lo, hi = 0.00001, 5.0
    def f(x):
        return a * (1 - (1 + x) ** (-n)) / x - V0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) * f(lo) < 0:
            hi = mid
        else:
            lo = mid
    print("Taux/periode =", round(mid * 100, 4), "%")
    print("Nb periodes/an? (1=an 2=sem 4=trim 12=mois 0=skip)")
    k = int(input("k: "))
    if k > 1:
        ta = (1 + mid) ** k - 1
        print("Taux annuel equiv =", round(ta * 100, 4), "%")

def f3e5():
    print("=== F3E5: Annuite avec decalage ===")
    C = saisir("Prix total: ")
    ac = saisir("Acompte date 0 (0=aucun): ")
    t = saisir("Taux (ex 0.05): ")
    d1 = int(input("Date 1ere annuite: "))
    d2 = int(input("Date derniere annuite: "))
    n = d2 - d1 + 1
    solde = C - ac
    facteur = (1 - (1 + t) ** (-n)) / t / (1 + t) ** (d1 - 1)
    a = solde / facteur
    print("Nb annuites =", n)
    print("Annuite a =", round(a, 4))

def f3e6():
    print("=== F3E6: Trouver taux (Sn) ===")
    a = saisir("Versement: ")
    n = int(input("Nb versements: "))
    Sn = saisir("Valeur acquise Sn: ")
    lo, hi = 0.00001, 5.0
    def f(x):
        return a * ((1 + x) ** n - 1) / x - Sn
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) * f(lo) < 0:
            hi = mid
        else:
            lo = mid
    print("Taux =", round(mid * 100, 4), "%")

def f3e7():
    print("=== F3E7: Flux variables VA ===")
    t = saisir("Taux (ex 0.05): ")
    n = int(input("Nb flux: "))
    tot = 0
    for k in range(1, n + 1):
        F = saisir("Flux annee " + str(k) + ": ")
        va = F / (1 + t) ** k
        print("  VA =", round(va, 4))
        tot += va
    print("V actuelle totale =", round(tot, 4))

def f3e8():
    print("=== F3E8: Comparer modalites ===")
    t = saisir("Taux actualisation (ex 0.06): ")
    nb = int(input("Nb modalites: "))
    res = []
    for m in range(nb):
        print("Modalite", m + 1)
        print("  1=comptant 2=flux dates")
        print("  3=annuites (dates d..d+n)")
        tp = int(input("  Type: "))
        if tp == 1:
            F = saisir("  Montant: ")
            rem = saisir("  Remise % (0=non): ")
            va = F * (1 - rem / 100)
        elif tp == 2:
            nf = int(input("  Nb flux: "))
            va = 0
            for k in range(nf):
                F = saisir("  Flux: ")
                d = saisir("  Date: ")
                va += F / (1 + t) ** d
        else:
            a = saisir("  Annuite: ")
            nn = int(input("  Nb annuites: "))
            d1 = saisir("  Date 1er versement: ")
            va = sum(a / (1 + t) ** (d1 + k) for k in range(nn))
        print("  VA =", round(va, 4))
        res.append((m + 1, round(va, 4)))
    print("-- RESULTATS --")
    for r in res:
        print("M" + str(r[0]) + " =", r[1])
    best = min(res, key=lambda x: x[1])
    print("=> Acheteur: M" + str(best[0]))

def f3e9():
    print("=== F3E9: Offres vendeur ===")
    t = saisir("Taux (ex 0.04): ")
    nb = int(input("Nb offres: "))
    res = []
    for m in range(nb):
        print("Offre", m + 1)
        print("  1=comptant 2=flux futur")
        print("  3=annuites debut(date 0)")
        print("  4=annuites fin(date 1..n)")
        tp = int(input("  Type: "))
        if tp == 1:
            va = saisir("  Montant: ")
        elif tp == 2:
            F = saisir("  Montant: ")
            d = saisir("  Date: ")
            va = F / (1 + t) ** d
        elif tp == 3:
            a = saisir("  Annuite: ")
            nn = int(input("  Nb annuites: "))
            va = sum(a / (1 + t) ** k for k in range(nn))
        else:
            a = saisir("  Annuite: ")
            nn = int(input("  Nb annuites: "))
            va = sum(a / (1 + t) ** k for k in range(1, nn + 1))
        print("  VA =", round(va, 4))
        res.append((m + 1, round(va, 4)))
    print("-- RESULTATS --")
    for r in res:
        print("O" + str(r[0]) + " =", r[1])
    best = max(res, key=lambda x: x[1])
    print("=> Vendeur: O" + str(best[0]))

def menu_s3():
    print("== SOLVEURS F3: ANNUITES ==")
    print("1. E1: Capital annuites")
    print("2. E2: Trouver annuite (Sn)")
    print("3. E3: Trouver nb periodes")
    print("4. E4: Trouver taux (V0)")
    print("5. E5: Annuite decalee")
    print("6. E6: Trouver taux (Sn)")
    print("7. E7: Flux variables VA")
    print("8. E8: Comparer modalites")
    print("9. E9: Offres vendeur")
    print("0. Retour")
    return int(input("Choix: "))

def solveur_f3():
    exos = [f3e1, f3e2, f3e3, f3e4, f3e5,
            f3e6, f3e7, f3e8, f3e9]
    while True:
        c = menu_s3()
        if c == 0:
            break
        if 1 <= c <= len(exos):
            exos[c - 1]()
