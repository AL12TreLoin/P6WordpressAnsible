import os
import getpass
import subprocess

print ("Avant de démarrer la configuration du serveur web, merci de répondre à ces questions: ")
nomsite = str(input("Saisir le nom du site WordPress :"))
adminbdd = str(input("Saisir le nom de l'administrateur de la base de données :"))
passwdbdd = getpass.getpass(prompt='Saisir un mot de passe pour cette base de données et valider par Entrée :')

variables = 'varnomsite=' + nomsite + ' varadminbdd=' + adminbdd + ' varpasswdbd=' + passwdbdd

print ("***LANCEMENT DU PLAYBOOK POUR LA CONFIGURATION DU SERVEUR WEB***")

pbinv = "-i inventaire.ini"
pbnom = " playbook_multisite_wordpress.yml"
pbextravar = " --extra-vars"
pbvars = " " + "\"" + variables + "\""
pbuser = " -u user"
pbbecome = " --become"
pbask = " --ask-become-pass"
#pbdebug = " -vvv"
os.system('ansible-playbook {}'.format(pbinv + pbnom + pbextravar + pbvars + pbuser + pbbecome + pbask))

commandehost = "echo " + "192.168.106.2 " + nomsite + ".serverweb " + ">> /etc/hosts"
subprocess.run(['sudo', 'bash', '-c', commandehost])

print ("\nl'adresse de votre site sera: ", nomsite + ".serverweb")
