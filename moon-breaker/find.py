from moonbreaker import moonbreaker
from multiprocessing import Pool

def calcul(txt):
    return (txt, moonbreaker(txt))

if __name__ == "__main__":
    maxi = 10000000
    # transformé un nombre en suite de lettres
    def nombre_en_lettres(nombre):
        # 1 -> a
        # 2 -> b
        # 26 -> z
        # 27 -> aa

        sortie = ""
        lettres = "abcdefghijklmnopqrstuvwxyz"

        while nombre > 0:
            reste = nombre % 26
            sortie += lettres[reste]
            nombre = (nombre - reste) // 26

        return sortie[::-1]

    print(f"generation des {maxi} strings")
    totest = [nombre_en_lettres(s) for s in range(maxi)]
    print(f"{totest[-1]} est le dernier")
    
    print("test en pool")

    with Pool(processes=48) as pool:
        result = pool.map(calcul, totest)

    mini = 10**11

    for txt, key in result:
        if key < mini:
            mini = key
            print(f"{txt} -> {key}")