from cytron import *

def save():
    global tp
    temp = cy_rfil_rela("/",name) + tp
    cy_mkfil("/",name,temp)
    tp = ""

global sort, car, tp
tp = ""
dp = 0
name = "s.txt"
name2 = "b2.txt"
fichier = cy_rfil_rela("/",name2)
lignes = str(fichier).split("\n")
fichier = ""
for l in range(0,len(lignes)-1,2):
    tp += str(lignes[l]) + "\n"
    dp += 1
    if dp == 10000:
        save()
        dp = 0

save()
input("fin ^^")