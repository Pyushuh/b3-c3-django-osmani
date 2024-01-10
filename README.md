# Password Manager
## Description du Projet
Bienvenue dans le projet Password Manager ! L'objectif est de créer une application web de carnet d'adresses permettant aux utilisateurs de gérer leurs sites, identifiants et mots de passe de manière sécurisée.

## Consigne
Créez une application web de carnet d'adresses. Les utilisateurs pourront s'inscrire, se connecter, et ajouter, éditer et supprimer des contacts.

## Fonctionnalités Attendues

- Liste des Sites: Affichez tous les sites avec leur nom, URL, identifiant et mot de passe.
- Ajout de Sites: Permettez aux utilisateurs d'ajouter de nouveaux sites via un formulaire.
- Modification de Site: Autorisez la modification des informations d'un site existant.
- Suppression de Site: Permettez aux utilisateurs de supprimer leurs propres sites.
- Interface Utilisateur Conviviale: Créez une interface simple et intuitive à l'aide de templates Django.

## Fonctionnalités Optionnelles (car projet fait en solo)
- Exporter ses mots de passe au format csv
- Importer des mots de passe au format csv

## Bonus
Authentification des utilisateurs : Permettez aux utilisateurs de s'inscrire, de se connecter et de se déconnecter.
Cryptage du mot de passe
Génération de mots de passe aléatoires
Dark mode


## Commandes Utiles
Création des migrations:
```sh
python manage.py makemigrations password_manager
```

Application des migrations:

```sh
python manage.py migrate

```
