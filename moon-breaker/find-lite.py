from moonbreaker import moonbreaker

def nombre_en_lettres(nombre):
    sortie = ""
    lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    while nombre > 0:
        reste = nombre % len(lettres)
        sortie += lettres[reste]
        nombre = (nombre - reste) // len(lettres)

    return sortie[::-1]

def afficher_resultat(coups, mini):
    print(f"{coups} - {nombre_en_lettres(coups)} | {mini[1]} -> {mini[0]}")

acc = 0
mini = [10**11, ""]
while True:
    string = nombre_en_lettres(acc)
    str_break = moonbreaker(string)
    if str_break < mini[0]:
        mini = [str_break, string]
        afficher_resultat(acc, mini)
    elif acc % 100000 == 0:
        afficher_resultat(acc, mini)
    acc += 1