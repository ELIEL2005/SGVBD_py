# Module1_Eliel/schema_manager.py

# Dictionnaire global pour stocker les schémas
schemas = {}

def creer_schema():
    """
    Crée un nouveau schéma en demandant les colonnes et leurs types.
    :return: dict représentant le schéma
    """
    print("Définition d'un nouveau schéma de table")
    schema = {}
    while True:
        colonne = input("Nom de la colonne (laisser vide pour terminer) : ").strip()
        if colonne == "":
            break
        type_str = input("Type (str, int, float, bool) : ").strip().lower()
        if type_str == "int":
            schema[colonne] = int
        elif type_str == "float":
            schema[colonne] = float
        elif type_str == "bool":
            schema[colonne] = bool
        else:
            schema[colonne] = str
    return schema

def enregistrer_schema(nom_table, schema):
    """
    Enregistre un schéma dans le dictionnaire global.
    """
    schemas[nom_table] = schema

def get_schemas():
    """
    Retourne le dictionnaire des schémas (utile pour sauvegarder).
    """
    return schemas

def charger_schemas(donnees_schemas):
    """
    Recharge les schémas à partir d'un dictionnaire (utile après lecture JSON).
    """
    global schemas
    schemas = {}
    for nom, colonne_types in donnees_schemas.items():
        schema_converti = {}
        for col, type_str in colonne_types.items():
            if type_str == "int":
                schema_converti[col] = int
            elif type_str == "float":
                schema_converti[col] = float
            elif type_str == "bool":
                schema_converti[col] = bool
            else:
                schema_converti[col] = str
        schemas[nom] = schema_converti

def valider_donnees(nom_table, donnees):
    """
    Valide les données d’un enregistrement selon le schéma de la table.
    """
    if nom_table not in schemas:
        raise ValueError(f"Le schéma de la table '{nom_table}' n'existe pas.")

    schema = schemas[nom_table]
    for colonne, type_attendu in schema.items():
        if colonne not in donnees:
            print(f"❌ Colonne manquante : {colonne}")
            return False
        if not isinstance(donnees[colonne], type_attendu):
            print(f"❌ Mauvais type pour '{colonne}': attendu {type_attendu.__name__}, reçu {type(donnees[colonne]).__name__}")
            return False
    return True

def afficher_schemas():
    """
    Affiche tous les schémas enregistrés.
    """
    for nom, sch in schemas.items():
        print(f"Table '{nom}': {sch}")
