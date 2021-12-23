from moonbreaker import moonbreaker
from multiprocessing import Pool
from os import cpu_count

def nombre_en_lettres(nombre):
    sortie = ""
    lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    while nombre > 0:
        reste = nombre % len(lettres)
        sortie += lettres[reste]
        nombre = (nombre - reste) // len(lettres)

    return sortie[::-1]

def calcul(x):
    string = nombre_en_lettres(x)
    return (string, len(str(moonbreaker(string))))


if __name__ == "__main__":
    # longueur d'une serie de calculs
    cps = 100000 * cpu_count()
    wallet = 0

    i = 0
    while True:
        i += 1

        print(f"calcul de la serrie n°{i}, de '{nombre_en_lettres(cps*(i-1))}' à '{nombre_en_lettres(i * cps)}'")

        with Pool(cpu_count()) as pool:
            result = pool.map(calcul, list(range(cps*(i-1), i * cps)))

        for string, longeur in result:
            if longeur < 10:
                wallet = round(wallet + 10 ** (10 - longeur) / 1000000, 4)
        print(f"Wallet : {wallet} MoonCoins")