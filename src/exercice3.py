fichierWarning=open('Input/warning.txt','r')
lignes=fichierWarning.readlines()
iplist=[]
for ligne in lignes:
    iplist.append(ligne.strip())
#print (iplist)
fichierCo=open('Input/connexion.log','r')
lignes=fichierCo.readlines()
suspect=[]

for ligne in lignes:
    ip=ligne.split(";")[0]
    print(ip)
    if ip in iplist: #si mon ip fait parti des ip suspectes
        login=ligne.split(";")[1] #id identifiant
        suspect.append(login)
        print(login)

set_suspect = set(suspect)   


fichierSuspect= open('Output/suspect.txt','w')  
for element in set_suspect:
    fichierSuspect.write(element+'; '+str(suspect.count(element))+"\n")
    #count c'est pour compter le nombre d'element dans la liste

fichierWarning.close()
fichierCo.close()
fichierSuspect.close()
        