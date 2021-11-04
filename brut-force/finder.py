from mod.cytron import *
from time import time

fichier = None

while fichier == None:
    name = input("nom de la basse de donnée: ")
    debut = time()
    print(round(time()-debut,1),"s - lecture de la base de donnée")
    fichier = cy_rfil_rela("/",name)

    if fichier is None: print(round(time()-debut,1),"s - basse de donnée vide ou inexistante\n")
    else:
        print(round(time()-debut,1),"s - decoupage...")
        lignes = str(fichier).split("\n")
        print(round(time()-debut,1),"s - optimisation...")
        fichier = "" #on gagne de la ram
        print(round(time()-debut,1),"s - fin,",len(lignes),"lignes!")

while True:
    bk = True
    rt = False
    tf = input("\nbreak a trouvé: ")
    debut = time()
    print(round(time()-debut,1),"s - recherche...")
    for ligne in lignes:
        if bk:
            bk = False
            if ligne == tf:
                rt = True
        else:
            if rt:
                print(round(time()-debut,1),"s - texte en clair:", ligne)
                rt = False
            bk = True
    print(round(time()-debut,1),"s - fin")