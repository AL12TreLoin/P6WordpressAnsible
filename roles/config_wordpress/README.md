config_wordpress
=========

Ce rôle va servir à copier le dossier Wordpress présent dans le dossier /var/tmp à la racine du dossier /var/www en le renommant avec le nom du site désiré.
Il va ensuite modifier le propriétaire de ce dossier par l'utilisateur www-data et supprimer les droits pour tous les autres utilisateurs.

Pré-requis
------------

Wordpress devra être présent dans le fichier /var/tmp/

Variables
--------------

La variable "varnomsite" est récupérée via le script python qui va demander de saisir un nom pour le site web.

Example Playbook
----------------

    - hosts: serverweb
      roles:
        - config_wordpress

Licence
-------

GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

Auteur : AL12TreLoin
------------------
