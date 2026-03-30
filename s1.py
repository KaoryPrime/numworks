import math
from outils import *

def f1e1():
    print("=== F1E1: Agios decouvert ===")
    print("I = C * t * n / base")
    C = saisir("Capital C: ")
    t = saisir("Taux annuel (ex 0.18): ")
    n = saisir("Nb jours: ")
    b = int(input("Base 360/365: "))
    I = C * t * n / b
    print("Agios I =", round(I, 2))

def f1e2():
    print("=== F1E2: Placement IS (jours) ===")
    C0 = saisir("C0: ")
    t = saisir("Taux (ex 0.05): ")
    n = saisir("Nb jours: ")
    b = int(input("Base 360/365: "))
    I = C0 * t * n / b
    print("I =", round(I, 4))
    print("Cn =", round(C0 + I, 4))

def f1e3():
    print("=== F1E3: Placement IS (jours) ===")
    C0 = saisir("C0: ")
    t = saisir("Taux (ex 0.055): ")
    n = saisir("Nb jours: ")
    b = int(input("Base 360/365: "))
    I = C0 * t * n / b
    print("I =", round(I, 4))
    print("Cn =", round(C0 + I, 4))

def f1e4():
    print("=== F1E4: IS multi-parts ===")
    C0 = saisir("C0: ")
    b = int(input("Base 360/365: "))
    print("-- a) I et Cn --")
    t = saisir("Taux (ex 0.07): ")
    n = saisir("Nb jours: ")
    I = C0 * t * n / b
    print("I =", round(I, 4))
    print("Cn =", round(C0 + I, 4))
    print("-- b) Trouver taux --")
    n2 = saisir("Nb jours (b): ")
    I2 = saisir("Interet I (b): ")
    print("Taux =", round(I2 * b / (C0 * n2) * 100, 4), "%")
    print("-- c) Trouver duree --")
    I3 = saisir("Interet voulu I (c): ")
    t3 = saisir("Taux (c) (ex 0.07): ")
    print("Duree =", round(I3 * b / (C0 * t3), 2), "jours")

def f1e5():
    print("=== F1E5: Interets en mois ===")
    C0 = saisir("C0: ")
    t = saisir("Taux annuel (ex 0.045): ")
    n = saisir("Nb mois: ")
    I = C0 * t * n / 12
    print("I =", round(I, 4))

def f1e6():
    print("=== F1E6: Trouver C0 (IS) ===")
    Cn = saisir("Valeur souhaitee Cn: ")
    t = saisir("Taux (ex 0.055): ")
    n = saisir("Duree: ")
    print("Base: 1=360j 2=365j 3=12mois")
    base = {1:360,2:365,3:12}[int(input("Base: "))]
    C0 = Cn / (1 + t * n / base)
    print("C0 =", round(C0, 4))

def f1e7():
    print("=== F1E7: Trouver taux (IS) ===")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    n = saisir("Duree: ")
    print("Base: 1=360j 2=365j 3=12mois")
    base = {1:360,2:365,3:12}[int(input("Base: "))]
    t = (Cn - C0) / (C0 * n / base)
    print("Taux =", round(t * 100, 4), "%")

def f1e8():
    print("=== F1E8: Trouver duree (IS) ===")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    t = saisir("Taux (ex 0.058): ")
    print("Base: 1=360j 2=365j 3=12mois")
    base = {1:360,2:365,3:12}[int(input("Base: "))]
    I = Cn - C0
    n = I * base / (C0 * t)
    print("I =", round(I, 4))
    print("Duree =", round(n, 2))
    print("Entier:", math.ceil(n))

def f1e9():
    print("=== F1E9: 2 capitaux IS ===")
    print("C2*t2*n - C1*t1*n = diff_I")
    print("C1 - C2 = diff_C")
    t1 = saisir("Taux 1 (ex 0.08): ")
    t2 = saisir("Taux 2 (ex 0.11): ")
    n = saisir("Duree (annees): ")
    dI = saisir("Diff interets (I2-I1): ")
    dC = saisir("C1 - C2: ")
    C2 = (dI + dC * t1 * n) / (t2 * n - t1 * n)
    C1 = C2 + dC
    print("C1 =", round(C1, 4))
    print("C2 =", round(C2, 4))
    print("I1 =", round(C1 * t1 * n, 4))
    print("I2 =", round(C2 * t2 * n, 4))

def f1e10():
    print("=== F1E10: Livret A (quinzaines) ===")
    C = saisir("Capital C: ")
    t = saisir("Taux annuel (ex 0.0125): ")
    print("1=entrer nb qz  2=calculer")
    mode = int(input("Mode: "))
    if mode == 1:
        q = int(input("Nb quinzaines: "))
    else:
        print("Type: 1=versement 2=retrait")
        t1 = int(input("Type debut: "))
        j1, m1 = date2("Date debut:")
        t2 = int(input("Type fin: "))
        j2, m2 = date2("Date fin:")
        ej1, em1 = qz_apres_versement(j1, m1) if t1 == 1 else qz_avant_retrait(j1, m1)
        ej2, em2 = qz_apres_versement(j2, m2) if t2 == 1 else qz_avant_retrait(j2, m2)
        q = qz_entre(ej1, em1, ej2, em2)
        print("Eff:", ej1, "/", em1, "->", ej2, "/", em2)
        print("Quinzaines =", q)
    if q <= 0:
        print("Pas de qz => I = 0")
        return
    I = C * t * q / 24
    print("I =", round(I, 4))
    print("Cn =", round(C + I, 4))

def f1e11():
    print("=== F1E11: Cpte epargne mvts ===")
    t = saisir("Taux annuel (ex 0.025): ")
    n = int(input("Nb mouvements: "))
    mvts = []
    for k in range(n):
        print("Mvt", k + 1)
        j, m = date2("  Date:")
        tp = int(input("  1=versement 2=retrait: "))
        mt = saisir("  Montant: ")
        mvts.append((j, m, tp, mt))
    print("Date de fin:")
    jf, mf = date2("")
    solde = 0
    dj, dm = None, None
    for j, m, tp, mt in mvts:
        ej, em = qz_apres_versement(j, m) if tp == 1 else qz_avant_retrait(j, m)
        if dj is not None:
            q = qz_entre(dj, dm, ej, em)
            I = solde * t * q / 24
            print("  Q=", q, "I=", round(I, 2))
            solde += I
        solde = solde + mt if tp == 1 else solde - mt
        print("Date", j, "/", m, "(eff", ej, "/", em, ") Solde=", round(solde, 2))
        dj, dm = ej, em
    ejf, emf = qz_avant_retrait(jf, mf)
    q = qz_entre(dj, dm, ejf, emf)
    I = solde * t * q / 24
    print("  Q=", q, "I=", round(I, 2))
    solde += I
    print("Solde final =", round(solde, 2))

def f1e12():
    print("=== F1E12: Escompte ===")
    VN = saisir("Valeur nominale VN: ")
    t = saisir("Taux escompte (ex 0.07): ")
    n = saisir("Nb jours: ")
    b = int(input("Base 360/365: "))
    ch = saisir("Commission HT (0=aucune): ")
    tv = saisir("TVA (ex 0.20, 0=aucune): ")
    E = VN * t * n / b
    cttc = ch * (1 + tv)
    Va = VN - E - cttc
    agio = E + cttc
    tr = agio / (VN * n / b)
    print("Escompte E =", round(E, 4))
    print("Comm TTC =", round(cttc, 4))
    print("Va nette =", round(Va, 4))
    print("Agio =", round(agio, 4))
    print("Taux reel =", round(tr * 100, 4), "%")

def f1e13():
    print("=== F1E13: Escompte complet ===")
    VN = saisir("Valeur nominale VN: ")
    t = saisir("Taux escompte (ex 0.06): ")
    n = saisir("Nb jours: ")
    b = int(input("Base 360/365: "))
    ch = saisir("Commission HT (0=aucune): ")
    tv = saisir("TVA (ex 0.20, 0=aucune): ")
    E = VN * t * n / b
    cttc = ch * (1 + tv)
    Va = VN - E
    agio = E + cttc
    net = VN - agio
    tr = agio / (VN * n / b)
    print("a) Nb jours =", n)
    print("b) Escompte E =", round(E, 4))
    print("c) Va (avant comm) =", round(Va, 4))
    print("   Net (apres comm) =", round(net, 4))
    print("d) Agio =", round(agio, 4))
    print("e) Taux reel =", round(tr * 100, 4), "%")

def f1e14():
    print("=== F1E14: Escompte + TEG ===")
    VN = saisir("Valeur nominale VN: ")
    t = saisir("Taux escompte (ex 0.065): ")
    n = saisir("Nb jours avant echeance: ")
    b = int(input("Base 360/365: "))
    ch = saisir("Commission HT (0=aucune): ")
    tv = saisir("TVA (ex 0.20, 0=aucune): ")
    E = VN * t * n / b
    cttc = ch * (1 + tv)
    agio = E + cttc
    net = VN - agio
    tr = agio * b / (net * n)
    print("a) Escompte E =", round(E, 4))
    print("b) Somme recue =", round(net, 4))
    print("c) Cout operation =", round(agio, 4))
    print("d) TEG =", round(tr * 100, 4), "%")

def menu_s1():
    print("== SOLVEURS F1: IS ==")
    print("1. E1: Agios decouvert")
    print("2. E2: Placement (jours)")
    print("3. E3: Placement (jours)")
    print("4. E4: IS multi-parts")
    print("5. E5: Interets (mois)")
    print("6. E6: Trouver C0")
    print("7. E7: Trouver taux")
    print("8. E8: Trouver duree")
    print("9. E9: 2 capitaux")
    print("10. E10: Livret A")
    print("11. E11: Cpte epargne mvts")
    print("12. E12: Escompte")
    print("13. E13: Escompte complet")
    print("14. E14: Escompte + TEG")
    print("0. Retour")
    return int(input("Choix: "))

def solveur_f1():
    exos = [f1e1, f1e2, f1e3, f1e4, f1e5,
            f1e6, f1e7, f1e8, f1e9, f1e10,
            f1e11, f1e12, f1e13, f1e14]
    while True:
        c = menu_s1()
        if c == 0:
            break
        if 1 <= c <= len(exos):
            exos[c - 1]()
