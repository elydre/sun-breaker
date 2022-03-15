from moonbreaker import moonbreaker

seed = "Les chaussettes de l'archi du chesse son't elles molles ou archi moolles"
cle = 2
liste = [str(moonbreaker(seed, cle)), ]

while True:
    temporaire = str(moonbreaker(str(liste[-1]), cle))
    liste.append(temporaire)
    if temporaire in liste[0:-1]:
        break
    print(len(liste), liste)


print(liste)