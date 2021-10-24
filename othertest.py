import os

print ("Avant de démarrer la configuration du serveur web, merci de répondre à ces questions: ")
sitewp = str(input("Quel sera le nom du site Wordpress ? "))
userwp = str(input("Quel sera le nom son administrateur ? "))
passwdwp = str(input("Quel sera le mot de passe de son administrateur ? "))

#print ("Vérification des données: ")
#print ("Le site est ",sitewp)
#print ("L'utilisateur est ",userwp)
#print ("Le mot de passe est ",passwdwp)

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
