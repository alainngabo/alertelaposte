fichier=open('Input/connexion.log','r')
#print ('bonjour') #juste pour vérifier si mon terminal fonctionne
lignes=fichier.readlines()
liste_utilisateurs=[]
fichierUser=open('Output/utilisateurs.txt','w')

for ligne in lignes:
    user=ligne.split(";")[1]
    if user not in liste_utilisateurs:
        liste_utilisateurs.append(user)
        fichierUser.write(user+'\n')
    

heuresAutorises = ['08','09','10','11','12','13','14','15','16','17','18']
for ligne in lignes:
    heure=ligne.split(";")[2].split(" ")[1].split(":")[0]
    if heure not in heuresAutorises:
        print (ligne.split(";")[1]+ ' '+ligne.split(";")[0])

fichier.close()
fichierUser.close()
   





