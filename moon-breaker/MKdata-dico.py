from mod.cytron import *
from mod.moonbreaker import moonbreaker
from multiprocessing import Pool
from os import cpu_count

def sb(m):
    return(f"{moonbreaker(m)}\n{m}" if m != "" else "")

if __name__ == '__main__':
    name = input("nom de la basse de donné a créé: ")
    db_name = input("nom de la basse de donné d'entrée: ")

    print("lecture")

    mot = rfil_rela("/",db_name).split("\n")

    print("calcul")

    with Pool(cpu_count()) as p:
        sortie = p.map(sb,mot)

    print("mise en page")

    s = "".join(so + "\n" for so in sortie)

    print("ecriture")

    mkfil("/",name,s)
    input("fin ^^")