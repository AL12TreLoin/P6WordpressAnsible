config_php
=========

Ce rôle va servir à copier le template correspondant au pool du module PHP-FPM (présent dans le sous dossier files de ce rôle).
Dans un second temps il va  modifier toutes les variables correspondantes au nom du site.
Et enfin il va copier le template wp-config.php dans le dossier correspondant au site Wordpress renommé selon la variable nomsite et qui permettra l'asoiciation avec une future base de données MariaDb pour Wordpress.

Pré-requis
------------

PHP version 7.3 devra être installé sur le serveur web, ainsi que les modules suivants :
php-cli php-mysql php-curl php-gd php-intl php-fpm

Variables
--------------

La variable "varnomsite" est récupérée via le script python qui va demander de saisir un nom pour le site web.

Example Playbook
----------------

    - hosts: serverweb
      roles:
        - config_php

Licence
-------

GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

Auteur : AL12TreLoin
------------------
