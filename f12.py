import math
from outils import *

def menu_is():
    print("-- INTERETS SIMPLES --")
    print("1. Interet I et valeur acquise Cn")
    print("2. Capital initial C0")
    print("3. Taux i")
    print("4. Duree n")
    print("5. Escompte commercial complet")
    print("6. Livret A (quinzaines)")
    print("7. Compte epargne mouvements")
    print("8. Deux capitaux (systeme)")
    print("0. Retour")
    return int(input("Choix: "))

def is_interet():
    print("-- Interet et Cn --")
    C = saisir("Capital C: ")
    i = saisir("Taux annuel i (ex 0.05): ")
    n, base = choisir_duree()
    I = C * i * n / base
    print("I =", round(I, 4))
    print("Cn =", round(C + I, 4))

def is_capital():
    print("-- Capital initial IS --")
    Cn = saisir("Valeur acquise Cn: ")
    i  = saisir("Taux i: ")
    n, base = choisir_duree()
    print("C0 =", round(Cn / (1 + i*n/base), 4))

def is_taux():
    print("-- Taux IS --")
    C0 = saisir("Capital C0: ")
    Cn = saisir("Valeur acquise Cn: ")
    n, base = choisir_duree()
    print("Taux i =", round((Cn-C0)/(C0*n/base)*100, 4), "%")

def is_duree():
    print("-- Duree IS --")
    C0 = saisir("Capital C0: ")
    I  = saisir("Interet desire I: ")
    i  = saisir("Taux i: ")
    print("Base: 1=360j  2=365j  3=12mois")
    base = {1:360,2:365,3:12}[int(input("Base: "))]
    n = I/(C0*i)*base
    print("Duree =", round(n,2))
    print("Entiers:", math.ceil(n))

def is_escompte():
    print("-- Escompte commercial --")
    VN = saisir("Valeur nominale VN: ")
    t  = saisir("Taux escompte (ex 0.06): ")
    n, base = choisir_duree()
    ch = saisir("Commission HT (0=aucune): ")
    tv = saisir("TVA (ex 0.20, 0=aucune): ")
    E        = VN * t * n / base
    comm_ttc = ch * (1 + tv)
    Va       = VN - E - comm_ttc
    agio     = E + comm_ttc
    tr       = agio / (VN * n / base)
    print("Escompte E =", round(E, 4))
    print("Commission TTC =", round(comm_ttc, 4))
    print("Valeur actuelle Va =", round(Va, 4))
    print("Agio =", round(agio, 4))
    print("Taux reel =", round(tr*100, 4), "%")

def livret_a():
    print("-- Livret A (quinzaines) --")
    print("Regle: versement -> qz SUIVANTE (1 ou 16)")
    print("       retrait   -> qz PRECEDENTE (1 ou 16)")
    C    = saisir("Capital C: ")
    taux = saisir("Taux annuel (ex 0.0125): ")
    print("1=entrer nb qz  2=calcul depuis dates (avec regle)")
    mode = int(input("Mode: "))
    if mode == 1:
        q = int(input("Nb quinzaines entieres: "))
    else:
        print("Type mouvement: 1=versement  2=retrait")
        t1 = int(input("Type debut: "))
        j1, m1 = date2("Date debut:")
        t2 = int(input("Type fin: "))
        j2, m2 = date2("Date fin:")
        ej1, em1 = qz_apres_versement(j1,m1) if t1==1 else qz_avant_retrait(j1,m1)
        ej2, em2 = qz_apres_versement(j2,m2) if t2==1 else qz_avant_retrait(j2,m2)
        q = qz_entre(ej1,em1, ej2,em2)
        print("Dates effectives:", ej1,"/",em1,"->",ej2,"/",em2)
        print("Quinzaines =", q)
    if q <= 0:
        print("Pas de qz entiere => I = 0")
        return
    I = C * taux * q / 24
    print("I =", round(I, 4))
    print("Cn =", round(C+I, 4))

def compte_epargne():
    print("-- Compte epargne mouvements --")
    taux = saisir("Taux annuel (ex 0.025): ")
    n    = int(input("Nb de mouvements: "))
    mvts = []
    for k in range(n):
        print("Mouvement", k+1)
        j, m = date2("  Date:")
        t    = int(input("  1=versement  2=retrait: "))
        mt   = saisir("  Montant: ")
        mvts.append((j, m, t, mt))
    print("Date de fin:")
    jf, mf = date2("")

    solde  = 0
    dj, dm = None, None

    for j, m, t, mt in mvts:
        ej, em = qz_apres_versement(j,m) if t==1 else qz_avant_retrait(j,m)
        if dj is not None:
            q = qz_entre(dj,dm, ej,em)
            I = solde * taux * q / 24
            print("  Q =", q, "| I =", round(I, 2))
            solde += I
        solde = solde+mt if t==1 else solde-mt
        print("Date", j,"/",m, "(eff",ej,"/",em,") | Solde =", round(solde, 2))
        dj, dm = ej, em

    ejf, emf = qz_avant_retrait(jf, mf)
    q = qz_entre(dj, dm, ejf, emf)
    I = solde * taux * q / 24
    print("  Q =", q, "| I =", round(I, 2))
    solde += I
    print("Solde final =", round(solde, 2))

def is_deux_capitaux():
    print("-- Deux capitaux IS --")
    print("C1 - C2 = diff_capital")
    print("I2 - I1 = diff_interet")
    diff_cap = saisir("Difference capitaux (C1-C2): ")
    i1 = saisir("Taux i1 (1er capital): ")
    i2 = saisir("Taux i2 (2nd capital): ")
    n, base = choisir_duree()
    diff_int = saisir("Difference interets (I2-I1): ")
    r1 = i1 * n / base
    r2 = i2 * n / base
    C2 = (diff_int + diff_cap * r1) / (r2 - r1)
    C1 = C2 + diff_cap
    print("C1 =", round(C1, 4))
    print("C2 =", round(C2, 4))
    print("I1 =", round(C1 * r1, 4))
    print("I2 =", round(C2 * r2, 4))

def fiche1():
    while True:
        c = menu_is()
        if c == 0: break
        elif c == 1: is_interet()
        elif c == 2: is_capital()
        elif c == 3: is_taux()
        elif c == 4: is_duree()
        elif c == 5: is_escompte()
        elif c == 6: livret_a()
        elif c == 7: compte_epargne()
        elif c == 8: is_deux_capitaux()

def menu_ic():
    print("-- INTERETS COMPOSES --")
    print("1. Valeur acquise Cn")
    print("2. Capital initial C0")
    print("3. Taux i")
    print("4. Duree n")
    print("5. Deux taux consecutifs + taux moyen")
    print("6. Retrouver taux+C0+duree")
    print("7. Mouvements -> trouver S")
    print("8. Flux multiples (VAN / capitalisation)")
    print("9. Taux actuariel")
    print("0. Retour")
    return int(input("Choix: "))

def ic_cn():
    print("-- Valeur acquise IC --")
    C0 = saisir("Capital C0: ")
    i  = saisir("Taux i (ex 0.05): ")
    n  = saisir("Duree n (decimal ok): ")
    Cn = C0 * (1+i)**n
    print("Cn =", round(Cn, 4))
    print("Interets =", round(Cn-C0, 4))

def ic_c0():
    print("-- Capital initial IC --")
    Cn = saisir("Cn: ")
    i  = saisir("Taux i: ")
    n  = saisir("Duree n: ")
    print("C0 =", round(Cn/(1+i)**n, 4))

def ic_taux():
    print("-- Taux IC --")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    n  = saisir("Duree n: ")
    print("Taux i =", round(((Cn/C0)**(1/n)-1)*100, 4), "%")

def ic_duree():
    print("-- Duree IC --")
    C0 = saisir("C0: ")
    Cn = saisir("Cn: ")
    i  = saisir("Taux i: ")
    n  = math.log(Cn/C0)/math.log(1+i)
    print("Duree n =", round(n, 4))
    print("Entiers:", math.ceil(n))

def ic_deux_taux():
    print("-- Deux taux consecutifs --")
    C0 = saisir("C0: ")
    i1 = saisir("Taux 1 i1: ")
    n1 = saisir("Duree 1 n1: ")
    i2 = saisir("Taux 2 i2: ")
    n2 = saisir("Duree 2 n2: ")
    Ci = C0*(1+i1)**n1
    Cn = Ci*(1+i2)**n2
    tm = (Cn/C0)**(1/(n1+n2))-1
    print("C apres periode 1 =", round(Ci, 4))
    print("Cn =", round(Cn, 4))
    print("Taux moyen =", round(tm*100, 4), "%")

def ic_retrouver():
    print("-- Retrouver taux, C0, duree --")
    V1 = saisir("Valeur acquise en n1: ")
    n1 = saisir("Date n1: ")
    V2 = saisir("Valeur acquise en n2 (n2>n1): ")
    n2 = saisir("Date n2: ")
    i  = (V2/V1)**(1/(n2-n1))-1
    C0 = V1/(1+i)**n1
    print("Taux i =", round(i*100, 4), "%")
    print("C0 =", round(C0, 4))
    rep = input("Interets totaux connus? (o/n): ")
    if rep == 'o':
        It = saisir("Interets totaux: ")
        nt = math.log((C0+It)/C0)/math.log(1+i)
        print("Duree totale =", round(nt, 4))

def ic_mouvements():
    print("-- Mouvements -> S inconnu --")
    i  = saisir("Taux par periode: ")
    nf = saisir("Date finale: ")
    n  = int(input("Nb flux connus: "))
    tot = 0
    for k in range(n):
        print("Flux", k+1)
        f = saisir("  Montant (+depot -retrait): ")
        t = saisir("  Date: ")
        v = f*(1+i)**(nf-t)
        print("  Capitalise =", round(v,4))
        tot += v
    print("Somme capitalises =", round(tot,4))
    cible = saisir("Valeur cible finale: ")
    ts    = saisir("Date du flux inconnu S: ")
    S     = (cible-tot)/(1+i)**(nf-ts)
    print("S =", round(S, 4))

def ic_van():
    print("-- Flux multiples (VAN) --")
    i    = saisir("Taux i: ")
    print("1=Valeur actuelle (date 0)  2=Valeur future (date N)")
    mode = int(input("Mode: "))
    N    = saisir("Date N: ") if mode==2 else 0
    n    = int(input("Nb flux: "))
    tot  = 0
    for k in range(n):
        print("Flux", k+1)
        f = saisir("  Montant (+recette -depense): ")
        t = saisir("  Date: ")
        v = f/(1+i)**t if mode==1 else f*(1+i)**(N-t)
        print("  Valeur ramenee =", round(v,4))
        tot += v
    print("Total =", round(tot,4))
    print("=> FAVORABLE" if tot>0 else "=> DEFAVORABLE")

def ic_actuariel():
    print("-- Taux actuariel --")
    C0 = saisir("Mise initiale C0: ")
    Cn = saisir("Valeur finale Cn: ")
    n  = saisir("Duree n: ")
    print("Taux =", round(((Cn/C0)**(1/n)-1)*100, 4), "%")

def fiche2():
    while True:
        c = menu_ic()
        if c == 0: break
        elif c == 1: ic_cn()
        elif c == 2: ic_c0()
        elif c == 3: ic_taux()
        elif c == 4: ic_duree()
        elif c == 5: ic_deux_taux()
        elif c == 6: ic_retrouver()
        elif c == 7: ic_mouvements()
        elif c == 8: ic_van()
        elif c == 9: ic_actuariel()
