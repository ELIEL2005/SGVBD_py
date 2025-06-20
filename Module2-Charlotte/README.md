Module 2 : Opérations CRUD sur les Enregistrements (crud_operations.py)*

Ce module implémente les fonctions de base nécessaires pour gérer dynamiquement des données sous forme de liste de dictionnaires. Il suit le modèle CRUD (Créer, Lire, Mettre à jour, Supprimer).

Fonctionnalités incluses :

1. Création d’un enregistrement
   - Ajoute un nouveau dictionnaire à une table (liste).
   - Un identifiant unique est automatiquement généré et assigné à l’enregistrement.

2. Lecture/Récupération d’enregistrements
   - Permet d’accéder à un ou plusieurs enregistrements.
   - Recherche possible par identifiant ou en retournant toute la table.

3. Mise à jour d’un enregistrement
   - Modifie les champs d’un enregistrement existant sans altérer son ID.

4. Suppression d’un enregistrement
   - Supprime définitivement un enregistrement de la table selon son ID.

5. Auto-apprentissage (bonus)
   - Implémente une logique simple de gestion d’identifiants uniques, utile si plusieurs ajouts sont faits.

