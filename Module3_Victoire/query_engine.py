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

# Exemple de base de données
donnees = [
    {"id": 1, "nom": "Alice", "age": 28},
    {"id": 2, "nom": "Bob", "age": 35},
    {"id": 3, "nom": "Charlie", "age": 40},
    {"id": 4, "nom": "David", "age": 23},
]

# Création du moteur de recherche
moteur = QueryEngine(donnees)

# Test de la recherche séquentielle (ex: trouver les personnes de plus de 30 ans)
resultat_filtre = moteur.filtrer_par_age(30)
print("Filtrage par âge (>30) :", resultat_filtre)

# Test de recherche par index
resultat_index = moteur.recherche_par_index(2)
print("Recherche par ID (2) :", resultat_index)

# Test de comparaison de performance
resultat_perf = moteur.comparer_performance(lambda x: x["age"] > 30, 3)
print("Comparaison des performances :", resultat_perf)
