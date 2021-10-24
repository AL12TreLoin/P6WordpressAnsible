# Objectifs de ce projet
Installation multisite de WordPress avec comme :
- serveur web : Nginx
- environnement PHP : PHP-FPM
- serveur de base de données : MariaDB
- outil de déploiement : Ansible
- script dynamique de lancement : Python

A la fin de l'éxecution du script python (et du playbook ansible), un nom de site web apparaitra (sous la forme : nomdusite.serverweb)
Et pour la dernière étape, manuelle celle-ci via le navigateur web, il ne restera plus qu'à renseigner le titre du site WordPress et de choisir un nom d'administrateur pour ce dernier.

Il sera possible de créer plusieurs sites sur ce même serveur.
Chacun de ses sites aura sa propre base de données hébergé sur le serveur dédié à MariaDB.

# Description des différents fichier
# inventaire.ini
Dans le fichier inventaire.ini sont déclarées les deux hosts :
- un serveur web ayant pour nom serverweb et pour adresse ip 192.168.106.2
- un serveur de base de données ayant pour nom database et ip 192.168.106.3

Pour information le Node Manager, sur lequel sera installé Ansible, à quant a lui l'adresse ip 192.168.106.1

# ansible.cfg
Dans le fichier de configuration de Ansible sont déclarés :
- le chemin vers le fichier de log du playbook ansible
- le fichier d'inventaire
- le nom de l'utilisateur ansible pour les deux machines distantes

# multisite_wordpress.py
Script Python qui dans un premier temps va récupérer :
- le nom du site que l'on veut créé
- le nom de l'administrateur de la base de données MariaDb pour WordPress
- le mot de passe de ce compte administrateur
Ces 3 variables seront utilisées dans les différents rôles pour personnalisé chaque création de site WordPress

Ensuite le script va lancer le Playbook playbook_multisite_wordpress.yml.
Il sera possible de modifier cette variable si besoin :
- pbuser : variable correspondant au nom d'utilisateur linux de chaque machine    distante, ce nom devra être le même pour les deux serveurs

Une fois le Playbook terminé, le script va ajouter le nom du site dans le fichiers hosts du Node Manager et l'afficher, il sera possible de le copier et de le coller dans la barre d'adresse du navigateur web pour lancer l'installation de config_wordpress

# playbook_mulitisite_wordpress.yml
Ce fichier yaml est le playbook qui va lancer l'un après l'autre les différents rôles pour chacun des deux serveurs :

- étape 1 : configuration du serveur web :
  - installation de wordpress (téléchargement et décompression de l'archive)
  - configuration de Nginx (dont la création des virtual host / 1 par site web créé)
  - configuration de Wordpress (modification du dossier dans var en fonction du nom de site et attribution des droits)
  - configuration de PHP (création du pool PHP et copie du fichier wp_config.php pour communiquer avec la future base de données)

- étape 2 : création de la base de données

- étape 3 : modification du fichier wp_config.php avec toutes les données nécessaires à la communication avec la base de données pour WordPress

# Pré-requis obligatoires pour le bon fonctionnement de ce déploiement :
# Sur le node manager :
- création d'un utilisateur dédié avec les droits SUDO et qui sera propriétaire du dossier /etc/ansible
- installation de ansible (au minimum version 2.9.6)
- installation via ansible-galaxy de la collection community.mysql
- installation de python3 (au minimum version 3.8.5)
- installation du client OpenSSH : génération et copie des clés publiques vers les machines distantes
- configuration réseau, adresse ipv4 : 192.168.106.1 pour pouvoir communiquer avec les deux serveurs
- activation du routage ipv4
- accès à internet + ajout d'une règle firewall de type NAT pour que les deux serveurs puissent aussi communiquer avec internet
- déclaration des deux serveurs dans le fichier /etc/hosts :
  - 192.168.106.2 serverweb
  - 192.168.106.3 database

# Sur le serveur web :
- installation de Nginx
- installation de python3
- installation de PHP 7.3 et de ses modules : php-cli php-mysql php-curl php-gd php-intl php-fpm
- installation du serveur OpenSSH : configurer en mode échange de clés  (avec un accès unique pour l'utilisateur dédié user)
- création d'un utilisateur dédié "user" avec les droits SUDO
- configuration réseau ipv4 : 192.168.106.2 avec comme passerelle le node manager 192.168.106.1
- le hostname sera serverweb

# Sur le serveur de base de données :
- installation de MariaDB Server (configuration de l'adresse de bind à 0.0.0.0 dans le fichier 50-server.cnf)
- installation de python3
- installation de python-pymysql et python3-mysqldb pour que les modules ansible fonctionnent
- installation du serveur OpenSSH : configurer en mode échange de clés  (avec un accès unique pour l'utilisateur dédié user)
- création d'un utilisateur dédié "user" avec les droits SUDO
- configuration réseau ipv4 : 192.168.106.3 avec comme passerelle le node manager 192.168.106.1
- le hostname sera database
