import math
from outils import *

def f4e1():
    print("=== F4E1: Annuites non std ===")
    print("Saisir -1 pour annuite inconnue")
    C0 = saisir("Capital C0: ")
    t = saisir("Taux (ex 0.03): ")
    n = int(input("Nb periodes: "))
    dette = C0
    for p in range(1, n + 1):
        dette = dette * (1 + t)
        a = saisir("Annuite p" + str(p) + " (-1=?): ")
        if a == -1:
            print("Annuite finale =", round(dette, 4))
            break
        dette -= a
        print("  Solde =", round(dette, 4))

def f4e2():
    print("=== F4E2: n annuites dates ===")
    C0 = saisir("Capital C0: ")
    t = saisir("Taux (ex 0.035): ")
    n = int(input("Nb annuites: "))
    dates = []
    for k in range(n):
        d = saisir("Date annuite " + str(k + 1) + ": ")
        dates.append(d)
    facteur = sum(1 / (1 + t) ** d for d in dates)
    a = C0 / facteur
    print("Annuite a =", round(a, 4))

def f4e3():
    print("=== F4E3: Capital max mensuel ===")
    a = saisir("Mensualite: ")
    ta = saisir("Taux annuel (ex 0.03): ")
    na = int(input("Nb annees: "))
    print("1=prop(immo) 2=equiv(conso)")
    c = int(input("Choix: "))
    if c == 1:
        tm = ta / 12
    else:
        tm = (1 + ta) ** (1 / 12) - 1
    nm = na * 12
    C0 = a * (1 - (1 + tm) ** (-nm)) / tm
    print("Taux mensuel =", round(tm * 100, 6), "%")
    print("C0 max =", round(C0, 4))

def f4e4():
    print("=== F4E4: Rbt anticipe decale ===")
    C0 = saisir("Capital C0: ")
    t = saisir("Taux (ex 0.04): ")
    k = int(input("1ere annuite en annee: "))
    n = int(input("Nb annuites: "))
    dk = C0 * (1 + t) ** (k - 1)
    a = dk * t / (1 - (1 + t) ** (-n))
    print("a) Annuite =", round(a, 4))
    p = int(input("Annee rbt anticipe: "))
    j = p - k
    CRD = dk * (1 + t) ** j - a * ((1 + t) ** j - 1) / t
    rest = a * (n - j)
    eco = rest - CRD
    print("b) CRD annee", p, "=", round(CRD, 4))
    print("   Restant =", round(rest, 4))
    print("c) Economie =", round(eco, 4))

def f4e5():
    print("=== F4E5: TEG in fine ===")
    C0 = saisir("Capital C0: ")
    t = saisir("Taux nominal (ex 0.025): ")
    n = int(input("Nb periodes: "))
    assu = saisir("Assurance/periode: ")
    frais = saisir("Frais dossier (0=non): ")
    enc = C0 - frais
    ai = C0 * t
    fl = [ai + assu] * (n - 1) + [ai + assu + C0]
    lo, hi = 0.00001, 5.0
    def f(tg):
        return sum(fl[k] / (1 + tg) ** (k + 1) for k in range(n)) - enc
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) * f(lo) < 0:
            hi = mid
        else:
            lo = mid
    print("TEG =", round(mid * 100, 6), "%")

def f4e6():
    print("=== F4E6: Mensualites + tableau ===")
    C0 = saisir("Capital C0: ")
    ta = saisir("Taux annuel (ex 0.06): ")
    na = int(input("Nb annees: "))
    print("1=prop(immo) 2=equiv(conso)")
    c = int(input("Choix: "))
    if c == 1:
        tm = ta / 12
    else:
        tm = (1 + ta) ** (1 / 12) - 1
    nm = na * 12
    a = C0 * tm / (1 - (1 + tm) ** (-nm))
    cout = a * nm - C0
    print("Taux mensuel =", round(tm * 100, 6), "%")
    print("Mensualite =", round(a, 4))
    print("Cout total =", round(cout, 4))
    k = int(input("Nb lignes tableau (0=skip): "))
    if k > 0:
        print("Per|Interet|Amort|CRD")
        CRD = C0
        for p in range(1, nm + 1):
            Int = CRD * tm
            Am = a - Int
            CRD -= Am
            if p <= k or p == nm:
                if p == nm and p > k + 1:
                    print("...")
                print(p, "|", round(Int, 2), "|",
                      round(Am, 2), "|", round(CRD, 2))

def menu_s4():
    print("== SOLVEURS F4: EMPRUNTS ==")
    print("1. E1: Annuites non std")
    print("2. E2: n annuites dates")
    print("3. E3: Capital max mensuel")
    print("4. E4: Rbt anticipe decale")
    print("5. E5: TEG in fine")
    print("6. E6: Mensualites + tableau")
    print("0. Retour")
    return int(input("Choix: "))

def solveur_f4():
    exos = [f4e1, f4e2, f4e3, f4e4, f4e5, f4e6]
    while True:
        c = menu_s4()
        if c == 0:
            break
        if 1 <= c <= len(exos):
            exos[c - 1]()
