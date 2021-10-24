config_nginx
=========

Ce rôle va servir à activer l'option server tokens dans le fichier de configuration de Nginx sur le serveur web.
Dans un second temps il va copier le vhost (template présent dans le sous-dossier files de ce rôle) dans le dossier sites-available de Nginx et modifier toutes les variables correspondantes au nom du site.
Et enfin il va créer un lien symbolique vers le dossier sites-enabled.

Pré-requis
------------

Nginx devra être installé sur le serveur web

Variables
--------------

La variable "varnomsite" est récupérée via le script python qui va demander de saisir un nom pour le site web.

Example Playbook
----------------

    - hosts: serverweb
      roles:
        - config_nginx

Licence
-------

GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

Auteur : AL12TreLoin
------------------
