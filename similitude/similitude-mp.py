import mod.sunbreaker as sunbreaker
from multiprocessing import Pool

entree = 3013562719773290005728648248254793
lvl = 70

#convertie un nombre en binaire
def bin_convert(n):
    n = int(n)
    if n == 0: return "0"
    else: return bin_convert(n//2) + str(n%2)

entree = f"0{bin_convert(entree)}"

def testeur(p):
    p_breaked = sunbreaker.bin_sunbreaker(p)

    sim = 0

    for i in range(len(p_breaked)):
        if len(entree) == i:
            break

        if p_breaked[i] == entree[i]:
            sim += 1
    sim = round(sim / len(p_breaked) * 100, 1)

    if p_breaked == entree:
        print("TROUVÉ "+p)
        return "§find§"

    if sim > lvl:
        return p


# sourcery skip: use-assigned-variable
if __name__ == "__main__":
    car = list("abcdefghijklmnopqrstuvwxyz")
    paire_edit = car
    while True:
        print("contruction des paires")
        paire = []
        for x in paire_edit:
            if x != None:
                for y in car:
                    paire.append(x + y)

        garde = round((len(paire)/len(paire_edit))/len(car)*100,1)
        
        print(f"test de {len(paire[0])} long, {garde}% gardé, {len(paire)} éléments")
        
        paire_edit = []

        print("calculs en POOL")
        with Pool(48) as pl:
            paire_edit = (pl.map(testeur, paire))

        if "§find§" in paire_edit: break