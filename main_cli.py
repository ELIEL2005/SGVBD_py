import os
import sys
from Module1_Eliel import schema_manager
from Module2_Charlotte import crud_operations
from Module3_Victoire import query_engine
from Module4_Léon import sort_engine
from Module5_Eliel import storage

# Tables et schémas sont chargés depuis le fichier JSON au lancement
tables, schemas = storage.charger_etat()

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

def main():
    while True:
        afficher_menu()
        choix = input("Choix : ").strip()

        if choix == "1":
            nom_table = input("Nom de la nouvelle table : ").strip()
            schéma = schema_manager.creer_schema()
            schemas[nom_table] = schéma
            tables[nom_table] = []
            print(f"Table '{nom_table}' créée avec succès.")

        elif choix == "2":
            nom_table = input("Table dans laquelle insérer : ").strip()
            if nom_table in schemas:
                enreg = crud_operations.ajouter_enregistrement(schemas[nom_table])
                tables[nom_table].append(enreg)
                print("Enregistrement ajouté.")
            else:
                print("Table inexistante.")

        elif choix == "3":
            nom_table = input("Table à afficher : ").strip()
            if nom_table in tables:
                crud_operations.afficher_enregistrements(tables[nom_table])
            else:
                print("Table non trouvée.")

        elif choix == "4":
            nom_table = input("Table à modifier : ").strip()
            if nom_table in tables:
                crud_operations.mettre_a_jour_enregistrement(tables[nom_table], schemas[nom_table])
            else:
                print("Table inconnue.")

        elif choix == "5":
            nom_table = input("Table : ").strip()
            if nom_table in tables:
                crud_operations.supprimer_enregistrement(tables[nom_table])
            else:
                print("Table inconnue.")

        elif choix == "6":
            nom_table = input("Table : ").strip()
            if nom_table in tables:
                query_engine.rechercher(tables[nom_table])
            else:
                print("Table non trouvée.")

        elif choix == "7":
            nom_table = input("Table : ").strip()
            if nom_table in tables:
                sort_engine.trier(tables[nom_table])
            else:
                print("Table inconnue.")

        elif choix == "8":
            storage.sauvegarder_etat(tables, schemas)
            print("Données sauvegardées avec succès.")

        elif choix == "9":
            print("Sauvegarde finale...")
            storage.sauvegarder_etat(tables, schemas)
            print("Au revoir.")
            break

        else:
            print("Choix invalide. Réessaye.")

if __name__ == "__main__":
    main()
