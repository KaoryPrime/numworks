def pg():
    input("[suite]")

def exo(t, lines):
    print("="*30)
    print(t)
    print("="*30)
    for l in lines:
        print(l)
    pg()

# ========================================
# FICHE 1 : INTERETS SIMPLES
# ========================================

def f1_exo1():
    exo("F1 Exo1: Agios decouverts", [
        "Suite a un decouvert bancaire",
        "de 1 300 EUR pendant 10 jours,",
        "la banque facture des agios",
        "au taux annuel de 18%.",
        "Quel est le montant des agios",
        "verses?",
    ])

def f1_exo2():
    exo("F1 Exo2: Placement 3 mois", [
        "Un individu place 45 000 EUR",
        "du 10 juin au 10 septembre",
        "au taux de 5%.",
        "De combien dispose-t-il",
        "a l'issue du placement?",
    ])

def f1_exo3():
    exo("F1 Exo3: Placement 5.5%", [
        "Un individu place 75 000 EUR",
        "du 15 mai au 18 septembre",
        "sur un compte rapportant 5,5%.",
        "De combien dispose-t-il",
        "a l'issue du placement?",
    ])

def f1_exo4():
    exo("F1 Exo4: Capital 18000", [
        "Placement 18 000 EUR a IS",
        "du 18 avril au 20 septembre.",
        "Taux annuel: 7%.",
        "",
        "a) Calculer I et valeur",
        "   acquise au 20 sept.",
    ])
    exo("F1 Exo4 suite", [
        "b) Si placement arrete",
        "   le 31 aout, calculer",
        "   le taux d'interet.",
        "",
        "c) Combien de jours pour",
        "   que I = 1 000 EUR",
        "   au taux de 7%?",
    ])

def f1_exo5():
    exo("F1 Exo5: Interets 7 mois", [
        "Quel est le montant des",
        "interets fournis par un",
        "placement de 34 800 EUR",
        "pendant 7 mois au taux",
        "d'interet annuel de 4,5%?",
    ])

def f1_exo6():
    exo("F1 Exo6: Trouver C0", [
        "Quelle somme doit-on placer",
        "aujourd'hui a IS 5,5% l'an",
        "pour disposer de 50 000 EUR",
        "dans 11 mois?",
    ])

def f1_exo7():
    exo("F1 Exo7: Trouver taux", [
        "Un individu place 2 700 EUR.",
        "100 jours plus tard, il",
        "recupere 2 735,37 EUR.",
        "Quel est le taux d'interet",
        "verse?",
    ])

def f1_exo8():
    exo("F1 Exo8: Trouver duree", [
        "Un individu place 29 200 EUR",
        "sur un compte rapportant",
        "5,80%. Il recupere",
        "30 658,38 EUR a l'issue.",
        "Quelle a ete la duree",
        "du placement?",
    ])

def f1_exo9():
    exo("F1 Exo9: Deux capitaux", [
        "Deux capitaux places a IS",
        "pendant 4 ans:",
        " 1er a 8%, le 2nd a 11%.",
        "Le 2nd a rapporte 320 EUR",
        "de plus que le 1er, mais",
        "est inferieur de 2000 EUR",
        "au premier.",
        "Trouver les 2 capitaux.",
    ])

def f1_exo10():
    exo("F1 Exo10: Livret A", [
        "Calculer les interets d'un",
        "placement sur un livret A",
        "de 2 500 EUR du 17 janvier",
        "au 14 fevrier 2015.",
        "Taux: 1,25%.",
    ])

def f1_exo11():
    exo("F1 Exo11: Cpte epargne", [
        "Mouvements sur un compte",
        "d'epargne a 2,5%:",
        " 5 jan: avoir 5 000 EUR",
        " 8 mars: retrait 4 000 EUR",
        " 18 mars: versement 800 EUR",
    ])
    exo("F1 Exo11 suite", [
        " 22 mai: retrait 1 500 EUR",
        " 6 juin: versement 1 000 EUR",
        " 7 juil: retrait 1 000 EUR",
        "",
        "Quelle somme reste-t-il",
        "sur le compte le 2 sept",
        "si les interets sont",
        "comptes par quinzaine?",
    ])

def f1_exo12():
    exo("F1 Exo12: Escompte 1", [
        "Effet de 1 000 EUR echeance",
        "1er janvier N, escompte",
        "le 1er novembre N-1 au",
        "taux nominal de 7%.",
        "Commission: 5 EUR HT.",
        "Somme encaissee au 1er nov?",
        "(annee civile 365j)",
    ])

def f1_exo13():
    exo("F1 Exo13: Escompte 2", [
        "Effet de 730 EUR escompte",
        "le 16 mars, echeance 15 mai",
        "taux d'escompte: 6%.",
        "(annee civile 365j)",
    ])
    exo("F1 Exo13 suite", [
        "a) Nb jours d'escompte?",
        "b) Montant escompte?",
        "c) Valeur actuelle?",
        "Commission: 3,10 EUR HT",
        "d) Montant agio?",
        "e) Taux reel escompte?",
    ])

def f1_exo14():
    exo("F1 Exo14: Escompte 3", [
        "Effet de 90 000 EUR echeance",
        "15 mai, negocie 70 jours",
        "avant echeance.",
        "Taux escompte: 6,5%.",
        "Commission: 5 EUR HT.",
        "(annee commerciale 360j)",
    ])
    exo("F1 Exo14 suite", [
        "a) Escompte commercial?",
        "b) Somme recue?",
        "c) Cout de l'operation?",
        "d) Taux reel (TEG)?",
    ])

# ========================================
# FICHE 2 : INTERETS COMPOSES
# ========================================

def f2_exo1():
    exo("F2 Exo1: IC vs IS", [
        "Capital de 2 000 EUR place",
        "a 4% pendant 2 ans.",
        "a) Valeur acquise a IC?",
        "b) Difference entre interet",
        "   IC et IS?",
    ])

def f2_exo2():
    exo("F2 Exo2: David/Jeremie", [
        "David et Jeremie placent",
        "chacun 1 000 EUR pour 2 ans.",
        "David: IS a 10%/an",
        "Jeremie: IC a 10%/an",
        "Difference entre les",
        "valeurs acquises?",
    ])

def f2_exo3():
    exo("F2 Exo3: VA non entiere", [
        "Valeur acquise d'un capital",
        "de 5 000 EUR place a IC",
        "de 5% pendant 10 ans",
        "et 3 mois?",
    ])

def f2_exo4():
    exo("F2 Exo4: Trouver C0", [
        "Quel C0 offre au bout de",
        "7 ans une valeur acquise",
        "de 2 400 EUR au taux",
        "de 5,5%?",
    ])

def f2_exo5():
    exo("F2 Exo5: Trouver taux", [
        "Quel est le taux IC d'un",
        "capital de 2 500 EUR place",
        "pendant 6 ans qui permet",
        "d'obtenir 2 950,52 EUR?",
    ])

def f2_exo6():
    exo("F2 Exo6: Trouver duree", [
        "Duree de placement d'un",
        "capital de 2 000 EUR",
        "au taux de 5% qui produit",
        "une VA de 3 591,72 EUR?",
    ])

def f2_exo7():
    exo("F2 Exo7: Trouver i", [
        "C0 = 30 000 EUR",
        "n = 11 ans",
        "C11 = 89 971,77 EUR",
        "Trouver le taux i.",
    ])

def f2_exo8():
    exo("F2 Exo8: Trouver n sem.", [
        "C0 = 40 000 EUR",
        "Taux semestriel: 4,75%",
        "Cn = 76 597,84 EUR",
        "Trouver n (en semestres).",
    ])

def f2_exo9():
    exo("F2 Exo9: Trouver C0", [
        "Cn = 123 661,92 EUR",
        "Taux: 7,5%",
        "n = 10 ans",
        "Trouver C0.",
    ])

def f2_exo10():
    exo("F2 Exo10: 2 taux", [
        "Placement 8 000 EUR.",
        "4% les 3 premieres annees",
        "6% les annees suivantes.",
    ])
    exo("F2 Exo10 suite", [
        "a) Somme au bout de 3 ans?",
        "b) Somme au bout de 7 ans?",
        "c) Taux moyen annuel",
        "   du placement?",
    ])

def f2_exo11():
    exo("F2 Exo11: Retrouver", [
        "Placement a IC longue duree:",
        "VA en 7e annee: 177 014,22",
        "VA en 10e annee: 226 098,34",
        "Interets totaux: 239 974,29",
    ])
    exo("F2 Exo11 suite", [
        "a) Retrouver le taux en",
        "   demontrant la relation.",
        "b) Retrouver C0.",
        "c) Retrouver la duree",
        "   totale du placement.",
    ])

def f2_exo12():
    exo("F2 Exo12: Mouvements", [
        "Pour 100 000 EUR fin nov 2015",
        "- Fin nov 2010: depot 30 000",
        "- Fin fev 2012: depot 30 000",
        "- Fin mai 2013: retrait 20000",
        "- Fin aout 2014: depot S",
        "Taux trimestriel: 1,5%.",
        "Calculer S.",
    ])

def f2_exo13():
    exo("F2 Exo13: Taux actuariel", [
        "M. Bongo place 20 000 EUR",
        "sur des actions. 2 ans plus",
        "tard, revend pour 26 422 EUR.",
        "Calculer le taux de",
        "rendement actuariel.",
    ])

def f2_exo14():
    exo("F2 Exo14: Lina chemisier", [
        "Lina: chemisier au comptant",
        "avec remise 12%",
        "OU payer avec 4 cheques",
        "d'1/4 du prix affiche",
        "encaisses fin de chaque",
        "trimestre (4 trimestres).",
        "A-t-elle raison de payer",
        "a credit?",
    ])

def f2_exo15():
    exo("F2 Exo15: Achat 16000", [
        "Achat d'un bien, 2 choix:",
        "1) 16 000 EUR comptant",
        "2) 10 000 EUR dans 3 ans",
        "   + 10 000 EUR dans 4 ans",
        "Taux actualisation: 7%.",
        "Modalite plus favorable",
        "pour l'acheteur?",
    ])

def f2_exo16():
    exo("F2 Exo16: Investisseur", [
        "2 placements a 5%/an, VA",
        "retirees le 31/12/N+4:",
        "1) 180 000 EUR le 01/04/N",
        "2) 5 versements annuels de",
        "   46 300 EUR, 1er=01/04/N",
    ])
    exo("F2 Exo16 suite", [
        "Calculer la VA pour chacun",
        "au 31/12/N+4 et indiquer",
        "lequel choisir.",
    ])

def f2_exo17():
    exo("F2 Exo17: Investissement", [
        "Investissement 1er mars 2014",
        "Depense: 300 000 EUR",
        "Recette1: 200 000 EUR",
        "  le 1er mars 2018",
        "Recette2: 200 000 EUR",
        "  le 1er mars 2019",
    ])
    exo("F2 Exo17 suite", [
        "a) Taux 7%: depense",
        "   opportune?",
        "b) Taux 6%: opportune?",
        "c) Taux pour lequel on",
        "   n'a pas plus de raisons",
        "   d'investir que non?",
    ])

# ========================================
# FICHE 3 : ANNUITES
# ========================================

def f3_exo1():
    exo("F3 Exo1: Capital annuites", [
        "Versements annuels constants",
        "de 1 500 EUR. Taux: 6%.",
        "1er versement: 1/2/08",
        "Dernier: 1/2/15",
    ])
    exo("F3 Exo1 suite", [
        "Calculer capital constitue:",
        "a) a la date du 1/2/15",
        "b) a la date du 1/2/18",
        "   (capital non retire",
        "   le 1/2/15).",
    ])

def f3_exo2():
    exo("F3 Exo2: Versement cst", [
        "Capital >= 100 000 EUR",
        "pour le 1/1/17.",
        "Versements annuels constants",
        "1er versement: 1/1/08",
        "Dernier: 1/1/17",
        "Taux: 5,70%.",
        "Calculer le versement.",
    ])

def f3_exo3():
    exo("F3 Exo3: Date rbt", [
        "Mensualites de 1 077,22 EUR",
        "pour rembourser 30 000 EUR",
        "emprunte le 1/7/12.",
        "Taux annuel: 6%.",
        "1ere mensualite 1 mois",
        "apres encaissement.",
        "Date rbt total?",
    ])

def f3_exo4():
    exo("F3 Exo4: Taux annuel", [
        "Emprunt 42 000 EUR rembourse",
        "par 10 semestrialites de",
        "5 426 EUR, 1ere versee 6",
        "mois apres encaissement.",
        "Quel est le taux annuel",
        "de cet emprunt?",
    ])

def f3_exo5():
    exo("F3 Exo5: Timeline annuite", [
        "Achat d'un bien: 350 000 EUR",
        "Acompte date 0: 100 000 EUR",
        "Solde finance par 8",
        "annuites constantes (= a)",
        "de date 2 a date 9.",
        "Taux: 5%.",
        "Calculer le montant de",
        "chacune de ces annuites.",
    ])

def f3_exo6():
    exo("F3 Exo6: Timeline taux", [
        "Constitution compte retraite:",
        "18 versements de 10 000 EUR",
        "(dates 1 a 18).",
        "Objectif: 300 000 EUR",
        "en date 18.",
        "Quel est le taux de",
        "capitalisation (ou de",
        "rentabilite)?",
    ])

def f3_exo7():
    exo("F3 Exo7: Flux variables", [
        "Benefices sur 5 ans:",
        " An1: 150 000  An2: 180 000",
        " An3: 200 000  An4: 190 000",
        " An5: 210 000",
        "Benefices realises en fin",
        "d'annee. Taux: 5%.",
        "Valeur actuelle au debut",
        "de l'annee 1?",
    ])

def f3_exo8():
    exo("F3 Exo8: 3 modalites", [
        "Achat de 100 000 EUR,",
        "3 modalites de paiement:",
        "1) Comptant: remise 2%",
        "2) 2 traites 57 500 EUR:",
        "   dans 2 ans et 3 ans 6m",
    ])
    exo("F3 Exo8 suite", [
        "3) 10 versements de 14 100",
        "   1er dans 2 ans, 2e dans",
        "   3 ans,..., 10e dans 11ans",
        "Taux actualisation: 6%.",
        "Quelle solution pour",
        "l'acheteur?",
    ])

def f3_exo9():
    exo("F3 Exo9: Offres vendeur", [
        "Offres pour une propriete:",
        "1) 47 500 EUR comptant",
        "2) 62 500 EUR dans 5 ans",
        "3) 15 annuites de 4 500 EUR",
        "   1er versement immediat",
        "Taux: 4%.",
        "Offre la plus avantageuse",
        "pour le vendeur?",
    ])

# ========================================
# FICHE 4 : EMPRUNTS INDIVIS
# ========================================

def f4_exo1():
    exo("F4 Exo1: Annuites non std", [
        "Emprunt annee 0: 10 000 EUR",
        "Taux: 3%.",
        "An1: annuite 5 000 EUR",
        "An2: annuite 1 000 EUR",
        "An3: rien",
        "An4: le reste",
        "Montant verse annee 4?",
    ])

def f4_exo2():
    exo("F4 Exo2: 2 annuites", [
        "Emprunt annee 0: 100 000 EUR",
        "Taux: 3,5%.",
        "Rembourse en 2 annuites",
        "identiques: annee 2 et",
        "annee 4.",
        "Montant de ces annuites?",
    ])

def f4_exo3():
    exo("F4 Exo3: Capital max", [
        "Quel capital peut-on",
        "emprunter a 3% si on",
        "rembourse 1 000 EUR/mois",
        "pendant 10 ans?",
        "1ere mensualite 1 mois",
        "apres encaissement.",
    ])

def f4_exo4():
    exo("F4 Exo4: Rbt anticipe", [
        "Emprunt 20 000 EUR annee 0",
        "Taux: 4%, 7 annuites cst",
        "pendant 8 ans, 1ere annuite",
        "versee en annee 2.",
    ])
    exo("F4 Exo4 suite", [
        "Decide annee 5 de terminer",
        "le remboursement.",
        "a) Montant de l'annuite?",
        "b) Somme a verser annee 5?",
        "c) Combien a-t-il",
        "   economise?",
    ])

def f4_exo5():
    exo("F4 Exo5: TEG", [
        "TEG d'un emprunt sur 5 ans",
        "in fine de 10 000 EUR",
        "au taux de 2,5%.",
        "Assurance: 50 EUR/an.",
    ])

def f4_exo6():
    exo("F4 Exo6: Mensualites", [
        "Emprunt 1 000 000 EUR",
        "Taux annuel: 6%, sur 3 ans",
        "par mensualites constantes.",
        "1ere: 1 mois apres.",
    ])
    exo("F4 Exo6 suite", [
        "a) Cout de l'emprunt?",
        "b) 2 premieres lignes du",
        "   tableau d'amortissement",
        "   + derniere ligne.",
        "Taux prop si pret immo",
        "Taux equiv si pret conso",
    ])

# ========================================
# MENUS
# ========================================

def menu_f1():
    print("-- F1: INTERETS SIMPLES --")
    print("1. Agios decouvert")
    print("2. Placement 3 mois")
    print("3. Placement 5.5%")
    print("4. Capital 18000 (3 parts)")
    print("5. Interets 7 mois")
    print("6. Trouver C0")
    print("7. Trouver taux")
    print("8. Trouver duree")
    print("9. Deux capitaux")
    print("10. Livret A")
    print("11. Compte epargne")
    print("12. Escompte effet 1000")
    print("13. Escompte effet 730")
    print("14. Escompte effet 90000")
    print("0. Retour")
    return int(input("Choix: "))

def menu_f2():
    print("-- F2: INTERETS COMPOSES --")
    print("1. IC vs IS (2000)")
    print("2. David/Jeremie")
    print("3. VA non entiere (5000)")
    print("4. Trouver C0 (2400)")
    print("5. Trouver taux (2500)")
    print("6. Trouver duree (2000)")
    print("7. Trouver i (30000)")
    print("8. Trouver n sem. (40000)")
    print("9. Trouver C0 (123661)")
    print("10. 2 taux (8000)")
    print("11. Retrouver taux/C0/n")
    print("12. Mouvements (100000)")
    print("13. Taux actuariel Bongo")
    print("14. Lina chemisier")
    print("15. Achat 16000")
    print("16. Investisseur 2 choix")
    print("17. Investissement 300000")
    print("0. Retour")
    return int(input("Choix: "))

def menu_f3():
    print("-- F3: ANNUITES --")
    print("1. Capital annuites (1500)")
    print("2. Versement constant")
    print("3. Date remboursement")
    print("4. Taux annuel (42000)")
    print("5. Timeline annuite")
    print("6. Timeline taux")
    print("7. Flux variables 5 ans")
    print("8. 3 modalites (100000)")
    print("9. Offres vendeur")
    print("0. Retour")
    return int(input("Choix: "))

def menu_f4():
    print("-- F4: EMPRUNTS INDIVIS --")
    print("1. Annuites non standards")
    print("2. 2 annuites identiques")
    print("3. Capital max mensuel")
    print("4. Rbt anticipe (20000)")
    print("5. TEG in fine (10000)")
    print("6. Mensualites (1000000)")
    print("0. Retour")
    return int(input("Choix: "))

def run_fiche(menu_fn, exos):
    while True:
        c = menu_fn()
        if c == 0:
            break
        if 1 <= c <= len(exos):
            exos[c - 1]()

def fiche1_enonces():
    run_fiche(menu_f1, [
        f1_exo1, f1_exo2, f1_exo3, f1_exo4,
        f1_exo5, f1_exo6, f1_exo7, f1_exo8,
        f1_exo9, f1_exo10, f1_exo11, f1_exo12,
        f1_exo13, f1_exo14,
    ])

def fiche2_enonces():
    run_fiche(menu_f2, [
        f2_exo1, f2_exo2, f2_exo3, f2_exo4,
        f2_exo5, f2_exo6, f2_exo7, f2_exo8,
        f2_exo9, f2_exo10, f2_exo11, f2_exo12,
        f2_exo13, f2_exo14, f2_exo15, f2_exo16,
        f2_exo17,
    ])

def fiche3_enonces():
    run_fiche(menu_f3, [
        f3_exo1, f3_exo2, f3_exo3, f3_exo4,
        f3_exo5, f3_exo6, f3_exo7, f3_exo8,
        f3_exo9,
    ])

def fiche4_enonces():
    run_fiche(menu_f4, [
        f4_exo1, f4_exo2, f4_exo3, f4_exo4,
        f4_exo5, f4_exo6,
    ])

def enonces():
    while True:
        print("=== ENONCES EXERCICES ===")
        print("1. Fiche 1: Interets Simples")
        print("2. Fiche 2: Interets Composes")
        print("3. Fiche 3: Annuites")
        print("4. Fiche 4: Emprunts Indivis")
        print("0. Retour")
        c = int(input("Choix: "))
        if c == 0:
            break
        elif c == 1:
            fiche1_enonces()
        elif c == 2:
            fiche2_enonces()
        elif c == 3:
            fiche3_enonces()
        elif c == 4:
            fiche4_enonces()
