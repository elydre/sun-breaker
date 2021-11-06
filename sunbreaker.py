'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
.codé en : UTF-8
.langage : python 3
.version : v1.3
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

def pert(bina,ref):
    ref = list(ref)
    bina = list(bina)
    sort = ""
    passed = 0
    while len(ref) < len(bina): ref += ref
    for x in range(len(bina)):
        passed += 1
        if int(passed) > int(ref[x]): passed = 0
        else: sort += str(bina[x])
    return(sort)

def BtoC(bina):
    add = 1
    sort = ""
    bina = list(bina)
    for loop in range(len(bina)-1):
        if bina[loop] == bina[loop+1]: add += 1
        else: sort += str(add); add = 1
    return(sort)

def BtoN(bina):
    return(int(bina, 2))

def TtoB(text):
    return(''.join(format(ord(i), '08b') for i in text))

def bin_sunbreaker(var):
    var = TtoB(BtoC(TtoB(var)))
    return(pert(var,BtoC(var)))

def sunbreaker(var):
    return(BtoN(bin_sunbreaker(var)))

if __name__ == "__main__":
    mode = input("Mode (bin/int): ")
    if mode == "bin":
        while True:
            print(bin_sunbreaker(input("Texte: ")))
    elif mode == "int":
        while True:
            print(sunbreaker(input("Texte: ")))
    else:
        print("Mode non reconnu")