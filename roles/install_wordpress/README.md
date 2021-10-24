install_wordpress
=========

Ce rôle va servir à télécharger l'archive Wordpress si cela n'est pas déjà fait puis à la décompresser de manière à créer le dossier du site wordpress dans le dossier /var/tmp/.

Pré-requis
------------

Le serveur web devra avoir accès à internet pour télécharger l'archive Wordpress si besoin.

Example Playbook
----------------

    - hosts: serverweb
      roles:
        - install_wordpress

Licence
-------

GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

Auteur : AL12TreLoin
------------------
