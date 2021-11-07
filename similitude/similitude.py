import mod.sunbreaker as sunbreaker

entree = "001001011010010010100001001010100100101110011001010110101101101001001010010110100100101100001010010000100011010010100100101110011000010010110101101"

clair = "copilot"

#pourcentage mininum de similitude
lvl = [73,75,82,71,80,75]

#diminution de pourcentage pour la longeur

car = list("abcdefghijklmnopqrstuvwxyz")

#fonction qui calcule la similitude entre 2 suite de bits
def similitude(suite1, suite2):
    # sourcery skip: inline-immediately-returned-variable, simplify-constant-sum, sum-comprehension
    similitude = 0
    #on parcours les deux suites de bits
    for i in range(len(suite1)):
        if len(suite2) == i:
            break
        #si les deux bits sont égaux, on incrémente la variable similitude
        if suite1[i] == suite2[i]:
            similitude += 1
    similitude = round(similitude / len(suite1) * 100, 1)
    return similitude

#liste avec tout les paire de car possibles
paire_edit = car
for rank in range(6):
    paire = [x+y for x in paire_edit for y in car]
    paire_edit = []

    partie = "".join(clair[0:rank+2])

    #teter le similitude entre chaque caractère et l'entrée
    for p in paire:
        p_breaked = sunbreaker.bin_sunbreaker(p)

        sim = similitude(p_breaked, entree)
        
        if p == partie:
            print("PARTIE -> " + p + ": " + str(sim) + "%")

        if p_breaked == entree:
            print(f"TROUVÉ: {p}")
            break

        if sim > lvl[rank]:
            print(p + ": " + str(sim) + "%")
            paire_edit.append(p)
        
    if p_breaked == entree: break