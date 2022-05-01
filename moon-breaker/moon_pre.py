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

version = "0.8pre"

TtoB = lambda text: "".join(format(ord(i), "08b") for i in text)

def MakeKey(bina,key):
    base = 1
    sup = int(bina, 2)
    for x in range(2, len(bina) * key + 20):
        base *= int(bina[x % (len(bina))]) + 1

    while True:
        if sup > base: sup /= 2
        elif sup * 10 < base: sup *= 2
        else: break

    base = str(base - sup)[:10]
    base = base + "0"*(10-len(base))

    return int(float(base))

def moonbreaker(txt, key = 2):
    return MakeKey(f"{TtoB(txt)}1", key)

if __name__ == "__main__":
    print(moonbreaker(input("Texte (str) : "), int(input("Key   (int) : "))))