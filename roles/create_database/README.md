create_database
=========

Ce rôle va servir à créer la base de données sur serveur MariaDb.
Il créera aussi un compte administrateur avec un mot de passe dédié.

Pré-requis
------------

MariaDb server devra être installé sur le serveur de base de données.
Il faudra aussi modifier de l'adresse de bind à 0.0.0.0 dans le fichier 50-server.cnf

Variables
--------------

La variable "varnomsite" est récupérée via le script python qui va demander de saisir un nom pour le site web qui correspondra au nom de la base de données.
La variable "adminbdd" est récupérée via le script python qui va demander de saisir un nom pour le compte administrateur de cette base de données.
La variable "passwdbdd" est récupérée via le script python qui va demander de saisir un mot de passe pour ce compte administrateur.


Example Playbook
----------------

    - hosts: database
      roles:
        - create_database

Licence
-------

GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

Auteur : AL12TreLoin
------------------
