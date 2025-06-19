import json

def sauvegarder_donnees(fichier, donnees):
    with open(fichier, 'w') as f:
        json.dump(donnees, f, indent=4)

def charger_donnees(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Si le fichier n'existe pas encorefrom storage import sauvegarder_donnees, charger_donnees

FICHIER_JSON = "donnees.json"

def menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Afficher les données")
    print("2. Ajouter une entrée")
    print("3. Sauvegarder et quitter")

def interface():
    donnees = charger_donnees(FICHIER_JSON)
   
    while True:
        menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            print("Données actuelles :", donnees)
        elif choix == "2":
            cle = input("Entrez la clé : ")
            valeur = input("Entrez la valeur : ")
            donnees[cle] = valeur
        elif choix == "3":
            sauvegarder_donnees(FICHIER_JSON, donnees)
            print("Données sauvegardées. Au revoir !")
            break
        else:
            print("Option invalide. Réessayez.")

if __name__ == "__main__":
    interface()