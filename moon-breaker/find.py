'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - codé en : UTF-8
 - langage : python 3
 - GitHub  : github.com/pf4-DEV
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

# placez mooonbreaker.py dans meme dossier que find.py
from moonbreaker import moonbreaker
from multiprocessing import Pool
from os import cpu_count

def calcul(txt):
    return (txt, moonbreaker(txt))

if __name__ == "__main__":
    # nombre de strings à generer et tester
    maxi = 50000000

    def nombre_en_lettres(nombre):
        sortie = ""
        lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while nombre > 0:
            reste = nombre % len(lettres)
            sortie += lettres[reste]
            nombre = (nombre - reste) // len(lettres)

        return sortie[::-1]

    print(f"generation des {maxi} strings")
    totest = [nombre_en_lettres(s) for s in range(maxi)]
    print(f"{totest[-1]} est le dernier")
    
    print("test en pool")

    # nombre de processus (cpu_count() pour le meme nombre que de coeurs)
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(calcul, totest)

    # plus gros break possible
    mini = 10**11

    for txt, key in result:
        if key < mini:
            mini = key
            print(f"{txt} -> {key}")