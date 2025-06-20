

💾 Module 5 – Persistance des Données et Interface Utilisateur

🧩 Description générale

Le Module 5 permet d’enregistrer les données créées par le système dans un fichier externe (au format JSON) afin qu'elles puissent être retrouvées automatiquement au prochain lancement du programme.

Ce module intègre également une interface utilisateur en ligne de commande (CLI), qui permet à l’utilisateur d’interagir facilement avec le système via des menus textuels.




🔧 Fonctionnalités principales

1. Sauvegarde automatique des données :

Toutes les tables et leurs schémas sont enregistrés dans un fichier JSON (donnees.json).

Cela inclut à la fois la structure (schéma) et le contenu (enregistrements).



2. Chargement des données au démarrage :

Si un fichier donnees.json existe, il est automatiquement lu pour restaurer les données précédemment enregistrées.



3. Interface en ligne de commande (CLI) :

Affichage d’un menu interactif pour :

Consulter les données

Ajouter une entrée

Modifier ou supprimer une entrée (facultatif)

Sauvegarder et quitter


Interaction 100% textuelle, simple et intuitive



4. Gestion des erreurs :

Lecture sécurisée des fichiers JSON (gestion des fichiers manquants ou mal formatés)

Vérification de la conformité des données avec les schémas existants





💡 Pourquoi ce module est important ?

Il permet de :

Conserver les données entre plusieurs utilisations du programme (persistance)

Offrir une expérience utilisateur simple, sans avoir à interagir avec le code

Rendre le projet plus réaliste, comme une vraie base de données avec une interface de gestion