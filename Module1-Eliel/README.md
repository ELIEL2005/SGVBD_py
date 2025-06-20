

Module 1 – Définition et Gestion des Schémas de Table

 Description générale

Le Module 1 constitue la base structurelle du système. Il permet de définir des schémas de table, c’est-à-dire la structure des données que l’utilisateur souhaite stocker : noms des colonnes et types de données associés (str, int, float, etc.).

Ce module garantit que toutes les données insérées ou manipulées dans les autres modules respectent un format prédéfini.




 Fonctionnalités principales

1. Création de schémas personnalisés :
L’utilisateur définit une nouvelle table en donnant :

un nom de table (ex : "étudiants")

les colonnes et leurs types (ex : nom: str, âge: int, moyenne: float)



2. Stockage centralisé des schémas :
Les schémas sont sauvegardés dans un dictionnaire global, accessible par tous les autres modules.

schémas = {
    "étudiants": {
        "nom": "str",
        "âge": "int",
        "moyenne": "float"
    }
}


3. Validation de la structure des données :
Avant d’insérer ou de modifier une donnée, le système vérifie :

que toutes les colonnes obligatoires sont présentes

que chaque valeur est du bon type







 Pourquoi ce module est important ?

Il impose une cohérence et une rigueur dans le stockage des données. Grâce à lui :

Les données sont toujours bien formatées

On évite les erreurs dues à des colonnes manquantes ou mal typées

On prépare une base solide pour les opérations CRUD, les filtres, les tris
