'''    _             _
  ___ | | _   _   __| | _ __   ___
 / _ \| || | | | / _` || '__| / _ |
|  __/| || |_| || (_| || |   |  __/
 \___||_| \__, | \__,_||_|    \___|
          |___/
___________________________________

 - codé en : UTF-8
 - langage : python3
 - GitHub  : github.com/elydre
 - Licence : GNU GPL v3
'''

version = "0.5"

BtoI = lambda bina: int(bina, 2)
TtoB = lambda text: "".join(format(ord(i), "08b") for i in text)

def MakeKey(bina,key):
    basse = 1
    sup = BtoI(bina)
    for x in range(2, len(bina) * key + 20):
        basse *= int(bina[x % (len(bina))]) + 1

    while True:
        if sup > basse: sup /= 2
        elif sup * 10 < basse: sup *= 2
        else: break
    
    basse -= sup
    
    while True:
        if len(str(basse)) > 10: basse //= 10
        elif len(str(basse)) < 10: basse *= 10
        else: break
    
    return int(basse)


def moonbreaker(txt, key = 2):
    return MakeKey(f"{TtoB(txt)}1", key)

if __name__ == "__main__":
    print(moonbreaker(input("Texte (str) : "), int(input("Key   (int) : "))))