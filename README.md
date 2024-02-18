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
- Authentification des utilisateurs : Permettez aux utilisateurs de s'inscrire, de se connecter et de se déconnecter.
- Dark mode

## Ressenti sur le projet
C'était assez sympathique à faire, pas trop de galères en dehors du fait que je ne suis pas très familière avec Django, 
donc c'est plutôt se rappeler comme ça fonctionne avec ce framework et Python en général qui est compliqué, sans 
mélanger avec les autres technos qu'on est en train d'apprendre. 
Un peu déçue de pas avoir pu passer plus de temps dessus parce que c'était marrant !


## Commandes Utiles
Création des migrations :
```sh
python manage.py makemigrations password_manager
```

Application des migrations:

```sh
python manage.py migrate

```
