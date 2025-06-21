import os
import sys
from Module1_Eliel import schema_manager
from Module2_Charlotte import crud_operations
from Module3_Victoire import query_engine
from Module4_Léon import sort_engine
from Module5_Eliel import storage

# Charger les tables et schémas depuis le fichier JSON au lancement
tables, sch = storage.charger_etat()
schema_manager.charger_schemas(sch)  # Injection des schémas dans le module 1

def afficher_menu():
    print("\n=== SGBD-Py - Menu Principal ===")
    print("1. Créer une table")
    print("2. Ajouter un enregistrement")
    print("3. Afficher les enregistrements")
    print("4. Mettre à jour un enregistrement")
    print("5. Supprimer un enregistrement")
    print("6. Rechercher (filtrage)")
    print("7. Trier les enregistrements")
    print("8. Sauvegarder les données")
    print("9. Quitter")
    print("===============================")

def table_existe(nom_table):
    if nom_table not in tables:
        print(f"❌ La table '{nom_table}' n'existe pas.")
        return False
    if nom_table not in schema_manager.get_schemas():
        print(f"❌ Le schéma de la table '{nom_table}' est introuvable.")
        return False
    return True

def main():
    while True:
        afficher_menu()
        choix = input("Choix : ").strip()

        if choix == "1":
            nom_table = input("Nom de la nouvelle table : ").strip()
            if nom_table in tables:
                print(f"❌ La table '{nom_table}' existe déjà.")
                continue
            schéma = schema_manager.creer_schema()
            schema_manager.enregistrer_schema(nom_table, schéma)
            tables[nom_table] = []
            print(f"✅ Table '{nom_table}' créée avec succès.")

        elif choix == "2":
            nom_table = input("Table dans laquelle insérer : ").strip()
            if not table_existe(nom_table):
                continue
            enreg = crud_operations.ajouter_enregistrement(schema_manager.get_schemas()[nom_table])
            if schema_manager.valider_donnees(nom_table, enreg):
                tables[nom_table].append(enreg)
                print("✅ Enregistrement ajouté.")
            else:
                print("❌ Données invalides. Ajout annulé.")

        elif choix == "3":
            nom_table = input("Table à afficher : ").strip()
            if not table_existe(nom_table):
                continue
            crud_operations.afficher_enregistrements(tables[nom_table])

        elif choix == "4":
            nom_table = input("Table à modifier : ").strip()
            if not table_existe(nom_table):
                continue
            crud_operations.mettre_a_jour_enregistrement(tables[nom_table], schema_manager.get_schemas()[nom_table])

        elif choix == "5":
            nom_table = input("Table : ").strip()
            if not table_existe(nom_table):
                continue
            crud_operations.supprimer_enregistrement(tables[nom_table])

        elif choix == "6":
            nom_table = input("Table : ").strip()
            if not table_existe(nom_table):
                continue
            query_engine.rechercher(tables[nom_table])

        elif choix == "7":
            nom_table = input("Table : ").strip()
            if not table_existe(nom_table):
                continue
            sort_engine.trier(tables[nom_table])

        elif choix == "8":
            storage.sauvegarder_etat(tables, schema_manager.get_schemas())
            print("✅ Données sauvegardées avec succès.")

        elif choix == "9":
            print("💾 Sauvegarde finale...")
            storage.sauvegarder_etat(tables, schema_manager.get_schemas())
            print("👋 Au revoir.")
            break

        else:
            print("❌ Choix invalide. Réessaye.")

if __name__ == "__main__":
    main()
