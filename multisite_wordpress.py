#import des bibliothèques python
import os
import getpass
import subprocess

#saisie des informations nécessaire à la création du site et de la base de données
print ("Avant de démarrer la configuration du serveur web, merci de répondre à ces questions: ")
nomsite = str(input("Saisir le nom du site WordPress :"))
adminbdd = str(input("Saisir le nom de l'administrateur de la base de données :"))
passwdbdd = getpass.getpass(prompt='Saisir un mot de passe pour cette base de données et valider par Entrée :')

#déclaration des variables qui vont être passées en extra_vars
variables = 'varnomsite=' + nomsite + ' varadminbdd=' + adminbdd + ' varpasswdbd=' + passwdbdd

#message de lancement du playbook ansible
print ("***LANCEMENT DU PLAYBOOK POUR LA CONFIGURATION DU SERVEUR WEB***")

#déclaration des variables de lancement du playbook ansible
pbinv = "-i inventaire.ini"
pbnom = " playbook_multisite_wordpress.yml"
pbextravar = " --extra-vars"
pbvars = " " + "\"" + variables + "\""
pbuser = " -u user"
pbbecome = " --become"
pbask = " --ask-become-pass"

#pour activer les messages de debug
#décommenter la ligne ci-dessous et ajouter la variable à la fin de la fonction os.system
#pbdebug = " -vvv"

#lancement du playbook
os.system('ansible-playbook {}'.format(pbinv + pbnom + pbextravar + pbvars + pbuser + pbbecome + pbask))

#déclaration de la commande à passer en mode sudo pour ajouter l'alias du site web dans le fichier hosts
commandehost = "echo " + "192.168.106.2 " + nomsite + ".serverweb " + ">> /etc/hosts"

#lancement de la commande d'ajout de l'alias du site web dans le fichier host
subprocess.run(['sudo', 'bash', '-c', commandehost])

#affichage du nom complet du site web créé, à copier et coller dans la barre d'adresse du navigateur
print ("\nl'adresse de votre site sera: ", nomsite + ".serverweb")
