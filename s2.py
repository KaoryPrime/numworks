import math
from outils import *

def f2e1():
    print("=== F2E1: IC vs IS ===")
    C0 = saisir("C0: ")
    t = saisir("Taux (ex 0.04): ")
    n = saisir("Duree n: ")
    Cn_ic = C0 * (1 + t) ** n
    I_ic = Cn_ic - C0
    I_is = C0 * t * n
    Cn_is = C0 + I_is
    print("a) Cn IC =", round(Cn_ic, 4))
    print("   I IC  =", round(I_ic, 4))
    print("   Cn IS =", round(Cn_is, 4))
    print("   I IS  =", round(I_is, 4))
    print("b) Diff I =", round(I_ic - I_is, 4))

def f2e2():
    print("=== F2E2: IC vs IS (2 pers) ===")
    C0 = saisir("C0: ")
    t = saisir("Taux (ex 0.10): ")
    n = saisir("Duree n: ")
    Cn_is = C0 * (1 + t * n)
    Cn_ic = C0 * (1 + t) ** n
    print("IS Cn =", round(Cn_is, 4))
    print("IC Cn =", round(Cn_ic, 4))
    print("Diff =", round(Cn_ic - Cn_is, 4))

def f2e3():
    print("=== F2E3: VA duree non entiere ===")
    C0 = saisir("C0: ")
    t = saisir("Taux (ex 0.05): ")
    n = saisir("Duree (ex 10.25): ")
    Cn = C0 * (1 + t) ** n
    print("Cn =", round(Cn, 4))
    print("Interets =", round(Cn - C0, 4))

def f2e4():
    print("=== F2E4: Trouver C0 (IC) ===")
    Cn = saisir("Cn: ")
    t = saisir("Taux (ex 0.055): ")
    n = saisir("Duree n: ")
    C0 = Cn / (1 + t) ** n
    print("C0 =", round(C0, 4))

def f2e5():
    print("=== F2E5: Trouver taux (IC) ===")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    n = saisir("Duree n: ")
    t = (Cn / C0) ** (1 / n) - 1
    print("Taux =", round(t * 100, 4), "%")

def f2e6():
    print("=== F2E6: Trouver duree (IC) ===")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    t = saisir("Taux (ex 0.05): ")
    n = math.log(Cn / C0) / math.log(1 + t)
    print("Duree n =", round(n, 4))
    print("Entier:", math.ceil(n))

def f2e7():
    print("=== F2E7: Trouver i (IC) ===")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    n = saisir("Duree n: ")
    t = (Cn / C0) ** (1 / n) - 1
    print("Taux i =", round(t * 100, 4), "%")

def f2e8():
    print("=== F2E8: Trouver n (semestres) ===")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    t = saisir("Taux semestriel (ex 0.0475): ")
    n = math.log(Cn / C0) / math.log(1 + t)
    print("n (semestres) =", round(n, 4))
    print("Entier:", math.ceil(n))

def f2e9():
    print("=== F2E9: Trouver C0 (IC) ===")
    Cn = saisir("Cn: ")
    t = saisir("Taux (ex 0.075): ")
    n = saisir("Duree n: ")
    C0 = Cn / (1 + t) ** n
    print("C0 =", round(C0, 4))

def f2e10():
    print("=== F2E10: 2 taux consecutifs ===")
    C0 = saisir("C0: ")
    t1 = saisir("Taux 1 (ex 0.04): ")
    n1 = saisir("Duree 1: ")
    t2 = saisir("Taux 2 (ex 0.06): ")
    n2 = saisir("Duree 2: ")
    C1 = C0 * (1 + t1) ** n1
    Cn = C1 * (1 + t2) ** n2
    tm = (Cn / C0) ** (1 / (n1 + n2)) - 1
    print("a) Apres per.1 =", round(C1, 4))
    print("b) Cn final =", round(Cn, 4))
    print("c) Taux moyen =", round(tm * 100, 4), "%")

def f2e11():
    print("=== F2E11: Retrouver t,C0,n ===")
    V1 = saisir("VA en annee n1: ")
    n1 = saisir("Annee n1: ")
    V2 = saisir("VA en annee n2: ")
    n2 = saisir("Annee n2: ")
    t = (V2 / V1) ** (1 / (n2 - n1)) - 1
    C0 = V1 / (1 + t) ** n1
    print("a) Taux =", round(t * 100, 4), "%")
    print("b) C0 =", round(C0, 4))
    It = saisir("Interets totaux (0=skip): ")
    if It > 0:
        nt = math.log((C0 + It) / C0) / math.log(1 + t)
        print("c) Duree totale =", round(nt, 4))

def f2e12():
    print("=== F2E12: Mouvements -> S ===")
    t = saisir("Taux par periode (ex 0.015): ")
    nf = saisir("Date finale: ")
    n = int(input("Nb flux connus: "))
    tot = 0
    for k in range(n):
        print("Flux", k + 1)
        f = saisir("  Montant (+depot -retrait): ")
        d = saisir("  Date: ")
        v = f * (1 + t) ** (nf - d)
        print("  Cap =", round(v, 4))
        tot += v
    print("Somme cap =", round(tot, 4))
    cible = saisir("Valeur cible finale: ")
    ds = saisir("Date du flux inconnu S: ")
    S = (cible - tot) / (1 + t) ** (nf - ds)
    print("S =", round(S, 4))

def f2e13():
    print("=== F2E13: Taux actuariel ===")
    C0 = saisir("Mise initiale: ")
    Cn = saisir("Valeur finale: ")
    n = saisir("Duree n: ")
    t = (Cn / C0) ** (1 / n) - 1
    print("Taux =", round(t * 100, 4), "%")

def f2e14():
    print("=== F2E14: Comptant vs credit ===")
    P = saisir("Prix affiche: ")
    rem = saisir("Remise comptant % (ex 12): ")
    Vc = P * (1 - rem / 100)
    print("Prix comptant =", round(Vc, 4))
    n = int(input("Nb paiements credit: "))
    a = saisir("Montant paiement: ")
    lo, hi = 0.00001, 5.0
    def f(x):
        return a * (1 - (1 + x) ** (-n)) / x - Vc
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) * f(lo) < 0:
            hi = mid
        else:
            lo = mid
    print("Taux/periode =", round(mid * 100, 4), "%")
    print("Nb periodes/an? (4=trim 12=mois)")
    k = int(input("k: "))
    print("Taux annuel =", round(((1 + mid) ** k - 1) * 100, 4), "%")

def f2e15():
    print("=== F2E15: Comparer 2 paiements ===")
    t = saisir("Taux actualisation (ex 0.07): ")
    print("-- Option 1 --")
    v1 = saisir("Montant comptant: ")
    print("-- Option 2 --")
    n2 = int(input("Nb flux option 2: "))
    tot = 0
    for k in range(n2):
        f = saisir("  Flux " + str(k + 1) + ": ")
        d = saisir("  Date: ")
        tot += f / (1 + t) ** d
    print("VA option 1 =", round(v1, 4))
    print("VA option 2 =", round(tot, 4))
    if tot < v1:
        print("=> Option 2 (acheteur)")
    else:
        print("=> Option 1 (acheteur)")

def f2e16():
    print("=== F2E16: Comparer placements ===")
    t = saisir("Taux (ex 0.05): ")
    df = saisir("Date finale: ")
    print("-- Placement 1 --")
    C1 = saisir("Montant unique: ")
    d1 = saisir("Date versement: ")
    VA1 = C1 * (1 + t) ** (df - d1)
    print("VA1 =", round(VA1, 4))
    print("-- Placement 2 --")
    n2 = int(input("Nb versements: "))
    a2 = saisir("Montant versement: ")
    d2 = saisir("Date 1er versement: ")
    VA2 = sum(a2 * (1 + t) ** (df - d2 - k) for k in range(n2))
    print("VA2 =", round(VA2, 4))
    print("=> Choisir", "P1" if VA1 > VA2 else "P2")

def f2e17():
    print("=== F2E17: VAN investissement ===")
    n = int(input("Nb flux (depense+recettes): "))
    flux = []
    for k in range(n):
        f = saisir("Flux " + str(k + 1) + " (+/-): ")
        d = saisir("  Date: ")
        flux.append((f, d))
    t1 = saisir("Taux 1 (ex 0.07): ")
    van1 = sum(f / (1 + t1) ** d for f, d in flux)
    print("VAN taux 1 =", round(van1, 4))
    print("=>", "FAVORABLE" if van1 > 0 else "DEFAVORABLE")
    t2 = saisir("Taux 2 (ex 0.06): ")
    van2 = sum(f / (1 + t2) ** d for f, d in flux)
    print("VAN taux 2 =", round(van2, 4))
    print("=>", "FAVORABLE" if van2 > 0 else "DEFAVORABLE")
    print("-- TRI (dichotomie) --")
    lo, hi = 0.00001, 5.0
    def g(x):
        return sum(f / (1 + x) ** d for f, d in flux)
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(mid) * g(lo) < 0:
            hi = mid
        else:
            lo = mid
    print("TRI =", round(mid * 100, 4), "%")

def menu_s2():
    print("== SOLVEURS F2: IC ==")
    print("1. E1: IC vs IS")
    print("2. E2: IC vs IS (2 pers)")
    print("3. E3: VA non entiere")
    print("4. E4: Trouver C0")
    print("5. E5: Trouver taux")
    print("6. E6: Trouver duree")
    print("7. E7: Trouver i")
    print("8. E8: Trouver n (sem)")
    print("9. E9: Trouver C0")
    print("10. 2 taux + taux moyen")
    print("11. Retrouver t,C0,n")
    print("12. Mouvements -> S")
    print("13. Taux actuariel")
    print("14. Comptant vs credit")
    print("15. Comparer paiements")
    print("16. Comparer placements")
    print("17. VAN + TRI")
    print("0. Retour")
    return int(input("Choix: "))

def solveur_f2():
    exos = [f2e1, f2e2, f2e3, f2e4, f2e5,
            f2e6, f2e7, f2e8, f2e9, f2e10,
            f2e11, f2e12, f2e13, f2e14, f2e15,
            f2e16, f2e17]
    while True:
        c = menu_s2()
        if c == 0:
            break
        if 1 <= c <= len(exos):
            exos[c - 1]()
