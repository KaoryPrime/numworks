import math
from outils import *

def menu_ann():
    print("-- ANNUITES --")
    print("1. Valeur acquise annuites")
    print("2. Valeur actuelle annuites")
    print("3. Annuite depuis VA ou Vact")
    print("4. Taux (dichotomie)")
    print("5. Duree n")
    print("6. Flux variables -> valeur actuelle")
    print("7. Comparer modalites de paiement")
    print("8. Timeline : annuites + flux")
    print("0. Retour")
    return int(input("Choix: "))

def ann_va():
    print("-- Valeur acquise annuites --")
    a  = saisir("Annuite a: ")
    i  = saisir("Taux i: ")
    n  = int(input("Nb annuites n: "))
    Sn = a*((1+i)**n-1)/i
    print("Sn =", round(Sn,4))
    k  = int(input("Capitaliser encore k periodes (0=non): "))
    if k>0:
        print("Sn+k =", round(Sn*(1+i)**k,4))

def ann_vact():
    print("-- Valeur actuelle annuites --")
    a  = saisir("Annuite a: ")
    i  = saisir("Taux i: ")
    n  = int(input("Nb annuites n: "))
    V0 = a*(1-(1+i)**(-n))/i
    print("V0 =", round(V0,4))

def ann_calcul_a():
    print("-- Calcul annuite --")
    print("1=depuis Sn (valeur acquise)")
    print("2=depuis V0 (valeur actuelle)")
    c  = int(input("Choix: "))
    i  = saisir("Taux i: ")
    n  = int(input("Nb annuites n: "))
    if c == 1:
        Sn = saisir("Sn: ")
        a  = Sn*i/((1+i)**n-1)
    else:
        V0 = saisir("V0: ")
        a  = V0*i/(1-(1+i)**(-n))
    print("Annuite a =", round(a,4))

def ann_taux():
    print("-- Taux annuites (dichotomie) --")
    print("1=depuis V0  2=depuis Sn")
    c  = int(input("Choix: "))
    a  = saisir("Annuite a: ")
    n  = int(input("Nb annuites n: "))
    if c == 1:
        V = saisir("V0: ")
        def f(x): return a*(1-(1+x)**(-n))/x-V
    else:
        V = saisir("Sn: ")
        def f(x): return a*((1+x)**n-1)/x-V
    lo, hi = 0.00001, 5.0
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid)*f(lo)<0: hi=mid
        else: lo=mid
    print("Taux i =", round(mid*100,4), "%")

def ann_duree():
    print("-- Duree annuites --")
    a  = saisir("Annuite a: ")
    i  = saisir("Taux i: ")
    V0 = saisir("V0: ")
    n  = -math.log(1-V0*i/a)/math.log(1+i)
    print("Duree n =", round(n,4))
    print("Entiers:", math.ceil(n))

def ann_flux_variables():
    print("-- Flux variables -> V actuelle --")
    i   = saisir("Taux i: ")
    n   = int(input("Nb flux: "))
    tot = 0
    for k in range(1,n+1):
        F  = saisir("Flux annee "+str(k)+": ")
        va = F/(1+i)**k
        print("  VA =", round(va,4))
        tot += va
    print("V actuelle totale =", round(tot,4))

def ann_comparer():
    print("-- Comparer modalites --")
    i    = saisir("Taux actualisation i: ")
    print("1=acheteur (min VA)  2=vendeur (max VA)")
    role = int(input("Role: "))
    nb   = int(input("Nb de modalites: "))
    res  = []
    for m in range(nb):
        print("Modalite", m+1)
        print("  1=flux unique  2=annuites fin  3=annuites debut (1er en date 0)")
        t = int(input("  Type: "))
        if t == 1:
            F    = saisir("  Montant: ")
            date = saisir("  Date (0=comptant): ")
            rem  = saisir("  Remise % (0=aucune): ")
            va   = F*(1-rem/100)/(1+i)**date
        elif t == 2:
            a  = saisir("  Annuite: ")
            nn = int(input("  Nb annuites: "))
            d  = saisir("  Date 1er versement: ")
            va = sum(a/(1+i)**(d+k) for k in range(nn))
        else:
            a  = saisir("  Annuite: ")
            nn = int(input("  Nb annuites: "))
            va = sum(a/(1+i)**k for k in range(nn))
        print("  VA =", round(va,4))
        res.append((m+1, round(va,4)))
    print("-- COMPARAISON --")
    for r in res:
        print("Modalite", r[0], ":", r[1])
    if role == 1:
        best = min(res, key=lambda x:x[1])
        print("=> Meilleure ACHETEUR: modalite", best[0])
    else:
        best = max(res, key=lambda x:x[1])
        print("=> Meilleure VENDEUR: modalite", best[0])

def ann_timeline():
    print("-- Timeline --")
    print("1=trouver annuite  2=trouver taux")
    mode = int(input("Mode: "))
    if mode == 1:
        C0 = saisir("Capital date 0 (negatif si emprunt): ")
        i  = saisir("Taux i: ")
        n  = int(input("Nb annuites (dates 1 a n): "))
        F  = saisir("Flux en date n (0=aucun): ")
        a  = (-C0*(1+i)**n - F)*i/((1+i)**n-1)
        print("Annuite a =", round(a,4))
    else:
        a  = saisir("Annuite par periode: ")
        n  = int(input("Nb versements: "))
        Sn = saisir("Valeur acquise Sn: ")
        def f(x):
            if x==0: return a*n-Sn
            return a*((1+x)**n-1)/x-Sn
        lo, hi = 0.00001, 5.0
        for _ in range(200):
            mid=(lo+hi)/2
            if f(mid)*f(lo)<0: hi=mid
            else: lo=mid
        print("Taux =", round(mid*100,4), "%")

def fiche3():
    while True:
        c = menu_ann()
        if c == 0: break
        elif c == 1: ann_va()
        elif c == 2: ann_vact()
        elif c == 3: ann_calcul_a()
        elif c == 4: ann_taux()
        elif c == 5: ann_duree()
        elif c == 6: ann_flux_variables()
        elif c == 7: ann_comparer()
        elif c == 8: ann_timeline()

def menu_emp():
    print("-- EMPRUNTS INDIVIS --")
    print("1. Annuite constante + cout")
    print("2. Capital empruntable")
    print("3. Tableau amortissement")
    print("4. Capital restant du (CRD)")
    print("5. Remboursement anticipe")
    print("6. Annuites non standards")
    print("7. Emprunt avec decalage")
    print("8. TEG (frais + assurance)")
    print("9. Taux equiv / proportionnels")
    print("10. Annuites egales dates spec.")
    print("0. Retour")
    return int(input("Choix: "))

def emp_annuite():
    print("-- Annuite constante --")
    C0 = saisir("Capital C0: ")
    i  = saisir("Taux par periode i: ")
    n  = int(input("Nb periodes n: "))
    a  = C0*i/(1-(1+i)**(-n))
    print("Annuite a =", round(a,4))
    print("Cout total =", round(a*n-C0,4))

def emp_capital():
    print("-- Capital empruntable --")
    a  = saisir("Annuite a: ")
    i  = saisir("Taux i: ")
    n  = int(input("Nb periodes n: "))
    print("C0 =", round(a*(1-(1+i)**(-n))/i,4))

def emp_tableau():
    print("-- Tableau amortissement --")
    C0  = saisir("Capital C0: ")
    i   = saisir("Taux i: ")
    n   = int(input("Nb periodes n: "))
    a   = C0*i/(1-(1+i)**(-n))
    print("Annuite =", round(a,4))
    k   = int(input("Nb lignes depuis debut: "))
    print("Per | Interet | Amort | CRD")
    CRD = C0
    for p in range(1,n+1):
        Int = CRD*i
        Am  = a-Int
        CRD -= Am
        if p<=k or p==n:
            if p==n and p>k+1: print("...")
            print(p,"|",round(Int,2),"|",round(Am,2),"|",round(CRD,2))

def emp_crd():
    print("-- Capital restant du --")
    C0 = saisir("Capital C0: ")
    i  = saisir("Taux i: ")
    n  = int(input("Nb periodes n: "))
    k  = int(input("Apres k periodes: "))
    a  = C0*i/(1-(1+i)**(-n))
    CRD = C0*(1+i)**k - a*((1+i)**k-1)/i
    print("Annuite =", round(a,4))
    print("CRD apres", k, "=", round(CRD,4))

def emp_anticipe():
    print("-- Remboursement anticipe --")
    C0 = saisir("Capital C0: ")
    i  = saisir("Taux i: ")
    n  = int(input("Nb periodes n: "))
    k  = int(input("Periode remboursement: "))
    a  = C0*i/(1-(1+i)**(-n))
    CRD     = C0*(1+i)**k - a*((1+i)**k-1)/i
    restant = a*(n-k)
    print("Annuite =", round(a,4))
    print("CRD periode", k, "=", round(CRD,4))
    print("Restant sans anticipe =", round(restant,4))
    print("Economie =", round(restant-CRD,4))

def emp_non_standards():
    print("-- Annuites non standards --")
    print("Saisir -1 pour l annuite finale inconnue.")
    C0    = saisir("Capital C0: ")
    i     = saisir("Taux annuel i: ")
    n     = int(input("Nb periodes: "))
    dette = C0
    for p in range(1,n+1):
        dette = dette*(1+i)
        a = saisir("Annuite periode "+str(p)+" (-1=inconnue): ")
        if a == -1:
            print("Annuite finale (solde) =", round(dette,4))
            break
        dette -= a
        print("  Solde restant =", round(dette,4))

def emp_decalage():
    print("-- Emprunt avec decalage --")
    C0 = saisir("Capital C0 (annee 0): ")
    i  = saisir("Taux annuel i: ")
    k  = int(input("1ere annuite a l annee k: "))
    n  = int(input("Nb annuites n: "))
    dk = C0*(1+i)**(k-1)
    a  = dk*i/(1-(1+i)**(-n))
    print("Dette capitalisee en annee", k-1, "=", round(dk,4))
    print("Annuite a =", round(a,4))
    rep = input("Calcul remboursement anticipe? (o/n): ")
    if rep == 'o':
        p   = int(input("Annee du remboursement: "))
        j   = p-k
        CRD = dk*(1+i)**j - a*((1+i)**j-1)/i
        print("Annuites payees =", j)
        print("CRD annee", p, "=", round(CRD,4))
        print("Restant sans anticipe =", round(a*(n-j),4))
        print("Economie =", round(a*(n-j)-CRD,4))

def emp_teg():
    print("-- TEG emprunt --")
    print("1=annuites constantes  2=in fine")
    mode = int(input("Mode: "))
    C0   = saisir("Capital C0: ")
    i    = saisir("Taux nominal par periode: ")
    n    = int(input("Nb periodes: "))
    assu = saisir("Assurance par periode (0=aucune): ")
    frais= saisir("Frais dossier (0=aucun): ")
    enc  = C0-frais
    if mode == 1:
        a = C0*i/(1-(1+i)**(-n))
        def f(tg): return sum((a+assu)/(1+tg)**k for k in range(1,n+1))-enc
    else:
        ai  = C0*i
        fl  = [ai+assu]*(n-1)+[ai+assu+C0]
        def f(tg): return sum(fl[k]/(1+tg)**(k+1) for k in range(n))-enc
    lo, hi = 0.00001, 5.0
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)*f(lo)<0: hi=mid
        else: lo=mid
    print("TEG par periode =", round(mid*100,6), "%")
    print("Si mensuel:")
    print("  Annuel prop  =", round(mid*12*100,4), "%")
    print("  Annuel equiv =", round(((1+mid)**12-1)*100,4), "%")

def emp_taux_ep():
    print("-- Taux equiv / proportionnel --")
    print("1=Annuel->sous-periode  2=Sous-periode->annuel")
    c = int(input("Choix: "))
    print("Sous-periode: 1=mois  2=trimestre  3=semestre")
    p = int(input("Sous-periode: "))
    k = {1:12,2:4,3:2}[p]
    if c == 1:
        ta = saisir("Taux annuel ta: ")
        print("Proportionnel =", round(ta/k*100,6), "%")
        print("Equivalent    =", round(((1+ta)**(1/k)-1)*100,6), "%")
        print("=> Immo/pro : PROPORTIONNEL")
        print("=> Conso TAEG : EQUIVALENT")
    else:
        ts = saisir("Taux sous-periode ts: ")
        print("Annuel prop  =", round(ts*k*100,6), "%")
        print("Annuel equiv =", round(((1+ts)**k-1)*100,6), "%")

def emp_annuites_dates():
    print("-- Annuites egales dates specif. --")
    C0 = saisir("Capital C0: ")
    i  = saisir("Taux par periode i: ")
    n  = int(input("Nb versements egaux: "))
    dates = []
    for k in range(n):
        d = saisir("Date versement " + str(k+1) + ": ")
        dates.append(d)
    T = max(dates)
    s = sum((1+i)**(T-d) for d in dates)
    a = C0*(1+i)**T / s
    print("Annuite a =", round(a, 4))
    print("Total verse =", round(a*n, 4))
    print("Cout =", round(a*n - C0, 4))

def fiche4():
    while True:
        c = menu_emp()
        if c == 0: break
        elif c == 1: emp_annuite()
        elif c == 2: emp_capital()
        elif c == 3: emp_tableau()
        elif c == 4: emp_crd()
        elif c == 5: emp_anticipe()
        elif c == 6: emp_non_standards()
        elif c == 7: emp_decalage()
        elif c == 8: emp_teg()
        elif c == 9: emp_taux_ep()
        elif c == 10: emp_annuites_dates()
