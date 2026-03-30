def menu():
    print("=== MATHS FI ===")
    print("1. Interets Simples")
    print("2. Interets Composes")
    print("3. Annuites")
    print("4. Emprunts Indivis")
    print("5. Utilitaire dates")
    print("6. Enonces exercices")
    print("0. Quitter")
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
