'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - langage : python 3
 - GitHub  : github.com/pf4-DEV
 - Licence : GPL-3.0
--|~|--|~|--|~|--|~|--|~|--|~|--
'''
import time
version = "0.5"

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

    print(sup, type(sup))
    
    base = str(base - sup)[0:10]
    base = base + "0"*(10-len(base))
    
    return int(float(base))

def moonbreaker(txt, key = 2):
    return MakeKey(f"{TtoB(txt)}1", key)

if __name__ == "__main__":
    print("start")
    t = time.time()
    print(moonbreaker("Hello World!"*3, 100))
    print(f"end in {time.time() - t}s")