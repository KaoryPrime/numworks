def menu():
    print("=== MATHS FI ===")
    print("1. Interets Simples")
    print("2. Interets Composes")
    print("3. Annuites")
    print("4. Emprunts Indivis")
    print("5. Utilitaire dates")
    print("6. Enonces exercices")
    print("7. Definitions")
    print("8. Solveurs exercices")
    print("0. Quitter")
    return int(input("Choix: "))

def menu_solveurs():
    print("== SOLVEURS ==")
    print("1. Fiche 1: IS")
    print("2. Fiche 2: IC")
    print("3. Fiche 3: Annuites")
    print("4. Fiche 4: Emprunts")
    print("0. Retour")
    return int(input("Choix: "))

while True:
    c = menu()
    if c == 0: 
        break
    elif c == 1: 
        from f12 import fiche1
        fiche1()
    elif c == 2: 
        from f12 import fiche2
        fiche2()
    elif c == 3: 
        from f34 import fiche3
        fiche3()
    elif c == 4: 
        from f34 import fiche4
        fiche4()
    elif c == 5: 
        from outils import util_dates
        util_dates()
    elif c == 6: 
        from enonces import enonces
        enonces()
    elif c == 7: 
        from definitions import definitions
        definitions()
    elif c == 8:
        s = menu_solveurs()
        if s == 1:
            from s1 import solveur_f1
            solveur_f1()
        elif s == 2:
            from s2 import solveur_f2
            solveur_f2()
        elif s == 3:
            from s3 import solveur_f3
            solveur_f3()
        elif s == 4:
            from s4 import solveur_f4
            solveur_f4()
