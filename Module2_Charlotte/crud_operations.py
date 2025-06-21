def ajouter_enregistrement(schema):
    """
    Demande à l'utilisateur de saisir les valeurs pour chaque colonne du schéma.
    :param schema: dict {"nom_colonne": type}
    :return: dict représentant un enregistrement
    """
    print("Ajout d'un nouvel enregistrement :")
    enregistrement = {}
    for colonne, type_attendu in schema.items():
        while True:
            valeur = input(f"{colonne} ({type_attendu.__name__}) : ").strip()
            try:
                if type_attendu == int:
                    valeur = int(valeur)
                elif type_attendu == float:
                    valeur = float(valeur)
                elif type_attendu == bool:
                    valeur = valeur.lower() in ["true", "1", "oui"]
                else:
                    valeur = str(valeur)
                enregistrement[colonne] = valeur
                break
            except ValueError:
                print(f"❌ Valeur invalide pour {colonne}. Veuillez entrer un {type_attendu.__name__}.")
    return enregistrement

def afficher_enregistrements(table):
    """
    Affiche tous les enregistrements d'une table.
    :param table: liste de dictionnaires
    """
    if not table:
        print("📭 La table est vide.")
    else:
        print("📄 Enregistrements :")
        for i, ligne in enumerate(table, 1):
            print(f"{i}. {ligne}")

def mettre_a_jour_enregistrement(table, schema):
    """
    Permet de modifier un enregistrement.
    :param table: liste de dictionnaires
    :param schema: dict du schéma
    """
    afficher_enregistrements(table)
    try:
        index = int(input("Numéro de l'enregistrement à modifier : ")) - 1
        if 0 <= index < len(table):
            print("Saisie des nouvelles valeurs (laisser vide pour ne pas changer) :")
            for colonne, type_attendu in schema.items():
                valeur = input(f"{colonne} [{table[index][colonne]}] : ").strip()
                if valeur:
                    try:
                        if type_attendu == int:
                            valeur = int(valeur)
                        elif type_attendu == float:
                            valeur = float(valeur)
                        elif type_attendu == bool:
                            valeur = valeur.lower() in ["true", "1", "oui"]
                        else:
                            valeur = str(valeur)
                        table[index][colonne] = valeur
                    except ValueError:
                        print(f"❌ Valeur invalide pour {colonne}. Modification ignorée.")
            print("✅ Enregistrement mis à jour.")
        else:
            print("❌ Numéro invalide.")
    except ValueError:
        print("❌ Entrée non valide.")

def supprimer_enregistrement(table):
    """
    Supprime un enregistrement de la table.
    :param table: liste de dictionnaires
    """
    afficher_enregistrements(table)
    try:
        index = int(input("Numéro de l'enregistrement à supprimer : ")) - 1
        if 0 <= index < len(table):
            del table[index]
            print("🗑️ Enregistrement supprimé.")
        else:
            print("❌ Numéro invalide.")
    except ValueError:
        print("❌ Entrée non valide.")
