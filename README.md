
OBJECTIFS : ce rapport présente l’implémentation de tri en python répondant aux spécifications suivantes : implémentation de deux algorithmes de tri (insertion et fusion) ; capacité de tri mon-colonne et multi-niveaux ; utilisation de la récursivité pour le tri fusion.
Implémentation des algorithmes de Tri
Tri par insertion (insertion_sort)
Principe : construire le tri élément par élément, comme quand on trie des cartes à jouer.
Caractéristiques :
o	Algorithme stable (conserve l'ordre des éléments égaux)
o	Complexité : O(n²) dans le pire cas
o	Tri en place (ne nécessite pas d'espace mémoire supplémentaire)
Tri Fusion (merge_sort et et _merge)
Principe : diviser pour régner en séparant récursivement la liste avant de fusionner les parties triées.
Caractéristiques :
o	Algorithme stable et récursif
o	Complexité : O (n log n) dans tous les cas
o	Nécessite un espace mémoire supplémentaire O(n)
Tri Multi-Niveaux
La fonction “get_key_func” génère des tuples de valeurs permettant les comparaisons multi-colonnes :
def get_key_func(keys):
    def key_func(row):
        return tuple(row[key] for key in keys)
    return key_func
Exemple d'utilisation :
o	Tri par nom puis par âge : `keys = ["nom", "age"]
o	Python compare d'abord les noms, puis les âges en cas d'égalité
Auto-apprentissage et Récursivité
Le tri fusion illustre parfaitement :
o	La Division récursive de la liste en sous-listes ;
o	Le Tri des sous-listes ;
o	La Fusion des sous-listes triées en une seule via _merge.
Fonction récursive :
def merge_sort(data, keys) :
    if len(data) <= 1 :
        return data
    left = merge_sort(data[:mid], keys)
    right = merge_sort(data[mid :], keys)
    return _merge(left, right, ...)
 Tests: 
Data = [
{'nom': 'Donic', 'age': 25, 'ville': 'Kisangani'}
{'nom': 'Isaac', 'age': 30, 'ville': 'Goma'}
{'nom': 'Jules', 'age': 20, 'ville': 'Lubumbashi'}
{'nom': 'Samuel', 'age': 25, 'ville': 'Bunia'}
]
Tri par nom puis age
insertion_sort(data.copy(), ["nom", "age"])
merge_sort(data, ["nom", "age"])
Résultats Attendus :
o	Priorité au tri par "nom"
o	En cas de noms identiques, le tri par "age" croissant est appliqué.
o	Conservation de l'ordre initial pour les clés identiques (stabilité)

Difficultés rencontrées
o	Gestion des clés multiples
o	Risque de recursionError sur des très grandes listes (dépassement de pile)
o	Surconsommation mémoire due à la création de multiples sous-listes ;
o	Vérification de la stabilité sur des données complexes ;
o	Réutilisation de mémoire pour les fusions.
Apport du module
o	Interface uniforme : en appliquant le même syntaxe (sort (data, keys)) pour les deux algorithmes.
o	Adaptabilité : fonctionne avec tout type de données comparable (numérique, strings) via key_func.
o	Extensibilité : architecture modulaire permettant d’ajouter d’autres algorithmes.
o	Stabilité : supporte le multi-niveau grâce aux tuples tout en conservant l’ordre des égalités.
Conclusion
Pour clore, Ce module implémente avec succès deux algorithmes de tri complémentaires, le tri multi-niveaux via des tuples de comparaison, la récursivité pour le tri fusion, une structure claire et extensible ceux qui constituent l’apprentissage des algorithmes fondamentaux, des applications réelles nécessitant des tris complexes ainsi qu’une extension future vers des optimisations avancées.

