fichier=open('Input/connexion.log','r')
lignes=fichier.readlines()
heuresAutorises = ['08','09','10','11','12','13','14','15','16','17','18','19']
for ligne in lignes:
    heure=ligne.split(";")[2].split(" ")[1].split(":")[0]
    if heure not in heuresAutorises:
        print (ligne.split(";")[1]+ ' '+ligne.split(";")[0]+' '+ligne.split(";")[2])
fichier.close()