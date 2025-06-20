# schema_manager.py

# Dictionnaire global pour stocker les schémas
schemas = {}

def creer_schema():
    """
    Demande à l'utilisateur de définir un schéma de table depuis la CLI.
    :return: dict - {"colonne": type}
    """
    print("Définition d'un nouveau schéma de table")
    colonnes_types = {}
    while True:
        nom_colonne = input("Nom de la colonne (laisser vide pour terminer) : ").strip()
        if not nom_colonne:
            break
        type_colonne = input("Type de la colonne (int, str, float, bool) : ").strip()
        if type_colonne not in ["int", "str", "float", "bool"]:
            print("Type invalide. Réessayez.")
            continue
        colonnes_types[nom_colonne] = eval(type_colonne)
    return colonnes_types

def enregistrer_schema(nom_table, schema):
    """
    Enregistre un schéma dans le dictionnaire global.
    :param nom_table: str
    :param schema: dict
    """
    if nom_table in schemas:
        raise ValueError(f"La table '{nom_table}' existe déjà.")
    schemas[nom_table] = schema

def valider_donnees(nom_table, donnees):
    """
    Valide les données par rapport au schéma de la table.
    :param nom_table: str
    :param donnees: dict
    :return: bool
    """
    if nom_table not in schemas:
        raise ValueError(f"Le schéma de la table '{nom_table}' n'existe pas.")
   
    schema = schemas[nom_table]
    for colonne, type_attendu in schema.items():
        if colonne not in donnees:
            print(f"Erreur : la colonne '{colonne}' est manquante.")
            return False
        if not isinstance(donnees[colonne], type_attendu):
            print(f"Erreur : la colonne '{colonne}' attend un type {type_attendu.__name__}, "
                  f"mais a reçu {type(donnees[colonne]).__name__}.")
            return False
    return True

def afficher_schemas():
    """
    Affiche tous les schémas enregistrés.
    """
    print("=== Schémas enregistrés ===")
    for nom, sch in schemas.items():
        print(f"Table '{nom}': {sch}")
    print("===========================")

def generer_schema_auto(donnees):
    """
    Génère un schéma basé sur un exemple de dictionnaire.
    :param donnees: dict
    :return: dict
    """
    return {col: type(val) for col, val in donnees.items()}
