# schema_manager.py

# Dictionnaire global pour stocker les schémas
schemas = {}

def creer_schema(nom_table, colonnes_types):
    """
    Crée un nouveau schéma de table.
    :param nom_table: str - nom de la table
    :param colonnes_types: dict - {"colonne": "type"}
    """
    if nom_table in schemas:
        raise ValueError(f"La table '{nom_table}' existe déjà.")
    schemas[nom_table] = colonnes_types

def valider_donnees(nom_table, donnees):
    """
    Valide les données par rapport au schéma de la table.
    :param nom_table: str - nom de la table
    :param donnees: dict - {"colonne": valeur}
    :return: bool - True si valide, sinon False
    """
    if nom_table not in schemas:
        raise ValueError(f"Le schéma de la table '{nom_table}' n'existe pas.")
   
    schema = schemas[nom_table]
    for colonne, type_attendu in schema.items():
        if colonne not in donnees:
            return False
        if not isinstance(donnees[colonne], eval(type_attendu)):
            return False
    return True

# Définition globale des schémas
schemas = {
    "utilisateur": {"id": int, "nom": str, "age": int}
}

def valider_donnees(nom_table, donnees):
    """
    Valide les données par rapport au schéma de la table.
    :param nom_table: str - nom de la table
    :param donnees: dict - {"colonne": valeur}
    :return: bool - True si valide, sinon False
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
    Affiche tous les schémas stockés.
    """
    for nom, sch in schemas.items():
        print(f"Table '{nom}': {sch}")

def generer_schema_auto(donnees):
    """
    Génère un schéma basé sur les types de valeurs fournies.
    :param donnees: dict - {"colonne": valeur}
    :return: dict - {"colonne": type}
    """
    schema_genere = {}
    for colonne, valeur in donnees.items():
        schema_genere[colonne] = type(valeur)
    return schema_genere

# Exemple d'utilisation
afficher_schemas()

print(valider_donnees("utilisateur", {"id": 1, "nom": "ELIEL", "age": 20}))  # True
print(valider_donnees("utilisateur", {"id": "1", "nom": "ELIEL", "age": 20}))  # False (id n'est pas int)

# Générer un schéma automatique à partir d'exemple de données
nouveau_schema = generer_schema_auto({"id": 1, "nom": "Alice", "age": 25})
print("Schéma généré automatiquement :", nouveau_schema)

