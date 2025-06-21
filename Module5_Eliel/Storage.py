import json
import os

DATA_FILE = "data.json"

def sauvegarder_etat(tables, schemas):
    """
    Sauvegarde les tables et les schémas dans un fichier JSON.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"tables": tables, "schemas": schemas}, f, indent=4)
        print("✅ Sauvegarde réussie.")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")

def charger_etat():
    """
    Charge les tables et schémas depuis un fichier JSON s’il existe.
    :return: (tables, schemas)
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                print("📦 Données chargées depuis le fichier JSON.")
                return data.get("tables", {}), data.get("schemas", {})
        except Exception as e:
            print(f"❌ Erreur lors du chargement : {e}")
            return {}, {}
    else:
        print("ℹ️ Aucun fichier de données trouvé. Initialisation vide.")
        return {}, {}
