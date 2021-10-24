import os
import getpass
import subprocess

print ("Avant de démarrer la configuration du serveur web, merci de répondre à ces questions: ")
sitewp = str(input("Saisir le nom du site WordPress :"))
userwp = str(input("Saisir le nom de l'administrateur de la base de données :"))
passwdwp = getpass.getpass(prompt='Saisir un mot de passe pour cette base de données et valider par Entrée :')

extras = 'extra1=' + sitewp + ' extra2=' + userwp + ' extra3=' + passwdwp

print ("***LANCEMENT DU PLAYBOOK POUR LA CONFIGURATION DU SERVEUR WEB***")

str1 = "-i inventaire.ini"
str2 = " playbook_config_serveur_web.yml"
str3 = " --extra-vars"
str4 = " " + "\"" + extras + "\""
str5 = " -u user"
str6 = " --become"
str7 = " --ask-become-pass"
str8 = " -vvv"
os.system('ansible-playbook {}'.format(str1 + str2 + str3 + str4 + str5 + str6 + str7))

cmd = "echo " + "192.168.106.2 " + sitewp + ".serverweb " + ">> /etc/hosts"
subprocess.run(['sudo', 'bash', '-c', cmd])

print ("\nl'adresse de votre site sera: ", sitewp + ".serverweb")
