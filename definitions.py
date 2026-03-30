def pg():
    input("[suite]")

def afficher(titre, lignes):
    print("=" * 30)
    print(titre)
    print("=" * 30)
    for l in lignes:
        print(l)
    pg()

def d_interet_simple():
    afficher("INTERET SIMPLE", [
        "Remuneration d'un capital",
        "calculee uniquement sur le",
        "capital initial (pas de",
        "capitalisation des interets).",
        "",
        "Formule:",
        " I = C x i x n / base",
        " Cn = C + I",
        "",
        "base: 360j (commerciale),",
        "      365j (civile),",
        "      12 (mois).",
    ])

def d_interet_compose():
    afficher("INTERET COMPOSE", [
        "Remuneration d'un capital",
        "ou les interets de chaque",
        "periode s'ajoutent au capital",
        "pour produire de nouveaux",
        "interets (capitalisation).",
        "",
        "Formule:",
        " Cn = C0 x (1+i)^n",
        " C0 = Cn / (1+i)^n",
    ])

def d_valeur_acquise():
    afficher("VALEUR ACQUISE", [
        "Montant total obtenu a la fin",
        "d'un placement (capital +",
        "interets cumules).",
        "",
        "IS: Cn = C0 + I",
        "IC: Cn = C0 x (1+i)^n",
    ])

def d_valeur_actuelle():
    afficher("VALEUR ACTUELLE", [
        "Valeur aujourd'hui d'une somme",
        "future. Technique inverse de",
        "la capitalisation: on",
        "actualise.",
        "",
        " V0 = Cn / (1+i)^n",
    ])

def d_taux_proportionnel():
    afficher("TAUX PROPORTIONNEL", [
        "Taux obtenu en divisant le",
        "taux annuel par le nombre",
        "de periodes dans l'annee.",
        "",
        " ts = ta / k",
        " k=12 (mois), k=4 (trim),",
        "   k=2 (semestre)",
        "",
        "Utilise pour:",
        " - Pret immobilier",
        " - Pret professionnel",
    ])

def d_taux_equivalent():
    afficher("TAUX EQUIVALENT", [
        "Taux qui, capitalise sur",
        "la sous-periode, donne le",
        "meme resultat que le taux",
        "annuel sur 1 an.",
        "",
        " ts = (1+ta)^(1/k) - 1",
        "",
        "Utilise pour:",
        " - Credit a la consommation",
        " - TAEG",
    ])

def d_escompte():
    afficher("ESCOMPTE COMMERCIAL", [
        "Operation par laquelle une",
        "banque avance le montant",
        "d'un effet de commerce",
        "avant son echeance, en",
        "deduisant des agios.",
        "",
        " E = VN x t x n / base",
        " Va = VN - E - commission",
        "",
        "VN = valeur nominale",
        "Va = valeur actuelle",
    ])

def d_lettre_change():
    afficher("LETTRE DE CHANGE", [
        "Effet de commerce par lequel",
        "le tireur (fournisseur)",
        "ordonne au tire (client) de",
        "payer une somme au porteur",
        "(creancier du fournisseur",
        "ou lui-meme).",
        "",
        "Aussi appelee: traite ou LCR.",
        "",
        "Art. L511-1 a L511-81",
        "du Code de commerce.",
    ])

def d_billet_ordre():
    afficher("BILLET A ORDRE", [
        "Effet de commerce par lequel",
        "le souscripteur (debiteur)",
        "s'engage a payer une somme",
        "a une date donnee au",
        "beneficiaire (creancier).",
        "",
        "Difference avec lettre de",
        "change: acte unilateral,",
        "pas besoin d'acceptation",
        "du tire.",
    ])

def d_effet_commerce():
    afficher("EFFET DE COMMERCE", [
        "Titre negociable qui constate",
        "une creance a court terme.",
        "",
        "Famille:",
        " - Lettre de change (traite)",
        " - Billet a ordre",
        " - Warrant",
        " - Cheque (parfois classe",
        "   a part)",
    ])

def d_annuite():
    afficher("ANNUITE", [
        "Somme versee ou recue a",
        "intervalles reguliers",
        "(annee, semestre, trimestre,",
        "mois).",
        "",
        "VA: Sn = a x ((1+i)^n-1)/i",
        "Vact: V0 = a x (1-(1+i)^-n)/i",
    ])

def d_annuite_constante():
    afficher("ANNUITE CONSTANTE", [
        "Chaque versement est du",
        "meme montant.",
        "",
        " a = C0 x i / (1-(1+i)^-n)",
        "",
        "L'annuite se decompose en:",
        " - Interet (decroissant)",
        " - Amortissement (croissant)",
    ])

def d_van():
    afficher("VAN - VALEUR ACTUELLE NETTE", [
        "Somme des flux actualises",
        "d'un investissement.",
        "",
        " VAN = somme(Fk/(1+i)^k)",
        "",
        "VAN > 0 : investissement",
        "  rentable (FAVORABLE)",
        "VAN < 0 : investissement",
        "  non rentable (DEFAVORABLE)",
    ])

def d_crd():
    afficher("CRD - CAPITAL RESTANT DU", [
        "Montant restant a rembourser",
        "apres k periodes.",
        "",
        "CRD = C0(1+i)^k",
        "    - a x ((1+i)^k-1)/i",
        "",
        "Sert au remboursement",
        "anticipe et au calcul",
        "du tableau d'amortissement.",
    ])

def d_teg():
    afficher("TEG / TAEG", [
        "Taux Effectif Global: taux",
        "reel d'un emprunt incluant",
        "tous les frais (assurance,",
        "frais de dossier...).",
        "",
        "Credit conso (TAEG):",
        "  -> methode EQUIVALENTE",
        "Pret immo / pro:",
        "  -> methode PROPORTIONNELLE",
    ])

def d_emprunt_indivis():
    afficher("EMPRUNT INDIVIS", [
        "Emprunt contracte aupres",
        "d'un seul preteur (banque).",
        "Rembourse par annuites",
        "constantes ou variables.",
        "",
        "A distinguer de l'emprunt",
        "obligataire (plusieurs",
        "preteurs via obligations).",
    ])

def d_tableau_amort():
    afficher("TABLEAU D'AMORTISSEMENT", [
        "Tableau detaillant pour",
        "chaque periode:",
        " - Capital Restant Du (CRD)",
        " - Interet de la periode",
        " - Amortissement du capital",
        " - Annuite (I + Amort)",
        "",
        "Interet = CRD x i",
        "Amort = Annuite - Interet",
    ])

def d_capitalisation():
    afficher("CAPITALISATION", [
        "Calcul d'une valeur future",
        "a partir d'un capital",
        "present.",
        "",
        "On multiplie par (1+i)^n",
        "pour aller vers le futur.",
        "",
        "Inverse: ACTUALISATION",
        " -> on divise par (1+i)^n",
    ])

def d_actualisation():
    afficher("ACTUALISATION", [
        "Calcul d'une valeur presente",
        "a partir d'un flux futur.",
        "",
        "On divise par (1+i)^n",
        "pour ramener au present.",
        "",
        "V0 = Cn / (1+i)^n",
        "",
        "Inverse: CAPITALISATION",
    ])

def d_quinzaine():
    afficher("QUINZAINE (LIVRET A)", [
        "Unite de temps pour le calcul",
        "des interets du livret A.",
        "24 quinzaines par an.",
        "",
        "Regles:",
        " Versement: interets a partir",
        "  de la quinzaine SUIVANTE.",
        " Retrait: interets jusqu'a la",
        "  quinzaine PRECEDENTE.",
        "",
        " I = C x taux x nb_qz / 24",
    ])

def d_in_fine():
    afficher("REMBOURSEMENT IN FINE", [
        "Mode de remboursement ou",
        "l'emprunteur ne paie que",
        "les interets chaque periode",
        "et rembourse le capital",
        "en totalite a la derniere",
        "echeance.",
        "",
        "Annuites 1 a n-1: C0 x i",
        "Derniere annuite: C0 x i + C0",
    ])

def definitions():
    defs = [
        ("Interet simple", d_interet_simple),
        ("Interet compose", d_interet_compose),
        ("Valeur acquise", d_valeur_acquise),
        ("Valeur actuelle", d_valeur_actuelle),
        ("Taux proportionnel", d_taux_proportionnel),
        ("Taux equivalent", d_taux_equivalent),
        ("Escompte commercial", d_escompte),
        ("Lettre de change", d_lettre_change),
        ("Billet a ordre", d_billet_ordre),
        ("Effet de commerce", d_effet_commerce),
        ("Annuite", d_annuite),
        ("Annuite constante", d_annuite_constante),
        ("VAN", d_van),
        ("CRD (Capital restant du)", d_crd),
        ("TEG / TAEG", d_teg),
        ("Emprunt indivis", d_emprunt_indivis),
        ("Tableau amortissement", d_tableau_amort),
        ("Capitalisation", d_capitalisation),
        ("Actualisation", d_actualisation),
        ("Quinzaine (Livret A)", d_quinzaine),
        ("Remboursement in fine", d_in_fine),
    ]
    while True:
        print("=== DEFINITIONS ===")
        for idx, (nom, _) in enumerate(defs, 1):
            print(str(idx) + ". " + nom)
        print("0. Retour")
        c = int(input("Choix: "))
        if c == 0:
            break
        if 1 <= c <= len(defs):
            defs[c - 1][1]()
