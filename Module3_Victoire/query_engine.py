import time

class QueryEngine:
    def __init__(self, data):
        self.data = data
        self.index = self._create_index()

    def _create_index(self):
        """Crée un index basé sur l'ID des enregistrements pour une recherche rapide."""
        return {item["id"]: item for item in self.data}

    def recherche_sequentielle(self, critere):
        """Recherche séquentielle des enregistrements correspondant au critère."""
        return [item for item in self.data if critere(item)]

    def recherche_par_index(self, id_recherche):
        """Utilisation de l'index pour une recherche rapide par ID."""
        return self.index.get(id_recherche, None)

    def filtrer_par_age(self, age_min):
        """Filtre les enregistrements où l'âge est supérieur à une valeur donnée."""
        return [item for item in self.data if item["age"] > age_min]

    def comparer_performance(self, critere, id_test):
        """Compare les performances entre recherche séquentielle et recherche indexée."""
        debut_seq = time.time()
        resultat_seq = self.recherche_sequentielle(critere)
        temps_seq = time.time() - debut_seq

        debut_index = time.time()
        resultat_index = self.recherche_par_index(id_test)
        temps_index = time.time() - debut_index

        return {"séquentielle": temps_seq, "indexée": temps_index}


# =======================
# Fonction interactive pour main_cli
# =======================

def rechercher(table):
    """Interface interactive pour rechercher dans une table."""
    if not table:
        print("❌ La table est vide.")
        return

    print("\n🔍 Rechercher dans la table")
    print("Colonnes disponibles :", list(table[0].keys()))
    colonne = input("Nom de la colonne à filtrer : ").strip()
    valeur = input("Valeur à rechercher : ").strip()

    resultats = []
    for ligne in table:
        if colonne in ligne and str(ligne[colonne]) == valeur:
            resultats.append(ligne)

    if resultats:
        print(f"\n✅ {len(resultats)} résultat(s) trouvé(s) :")
        for r in resultats:
            print(r)
    else:
        print("❌ Aucun résultat trouvé.")
