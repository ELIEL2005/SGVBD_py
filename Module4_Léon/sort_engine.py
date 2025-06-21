def get_key_func(keys):
    """Génère une fonction d'extraction de clé de tri à partir d'une liste de colonnes"""
    def key_func(row):
        return tuple(row[key] for key in keys)
    return key_func

def insertion_sort(data, keys):
    """
    Tri par insertion stable en place
    - data : liste de dictionnaires (en place)
    - keys : liste des colonnes de tri (ordre de priorité)
    """
    key_func = get_key_func(keys)
    n = len(data)

    for i in range(1, n):
        current = data[i]
        current_key = key_func(current)
        j = i - 1

        while j >= 0 and key_func(data[j]) > current_key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

def merge_sort(data, keys):
    """
    Tri fusion récursif stable (retourne une nouvelle liste)
    - data : liste de dictionnaires
    - keys : liste des colonnes de tri
    Retourne nouvelle liste triée
    """
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid], keys)
    right = merge_sort(data[mid:], keys)
    return _merge(left, right, get_key_func(keys))

def _merge(left, right, key_func):
    """Fusionne deux listes triées"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ========================
# Fonction interactive pour main_cli.py
# ========================
def trier(table):
    """
    Interface interactive : trie une table selon une ou plusieurs colonnes,
    en utilisant un algorithme choisi par l'utilisateur.
    """
    if not table:
        print("❌ La table est vide.")
        return

    print("\n🔽 Tri des enregistrements")
    print("Colonnes disponibles :", list(table[0].keys()))

    colonnes = input("Colonne(s) à trier (séparées par des virgules) : ").strip()
    keys = [col.strip() for col in colonnes.split(",") if col.strip() in table[0]]

    if not keys:
        print("❌ Aucune colonne valide pour le tri.")
        return

    algo = input("Choisir l'algorithme : [1] Insertion Sort (en place), [2] Merge Sort (copie) : ").strip()

    if algo == "1":
        insertion_sort(table, keys)
        print("✅ Table triée (insertion sort) :")
    elif algo == "2":
        table[:] = merge_sort(table, keys)
        print("✅ Table triée (merge sort) :")
    else:
        print("❌ Choix d'algorithme invalide.")
        return

    for ligne in table:
        print(ligne)
