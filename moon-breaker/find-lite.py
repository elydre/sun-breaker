from moonbreaker import moonbreaker

def nombre_en_lettres(nombre):
    sortie = ""
    lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    while nombre > 0:
        reste = nombre % len(lettres)
        sortie += lettres[reste]
        nombre = (nombre - reste) // len(lettres)

    return sortie[::-1]

acc = 0
mini = 10**11
while True:
    string = nombre_en_lettres(acc)
    str_break = moonbreaker(string)
    if str_break < mini:
        mini = str_break
        print(f"{string} -> {str_break}")
    acc += 1