from mod.sunbreaker import *
from mod.ColorPrint import colorprint, Colors

while True:
    var = input("Texte: ")

    var = TtoB(var)

    colorprint("var = TtoB(var) -> ", color = Colors.blanc,end = False)
    colorprint(var, color = Colors.cyan)

    var = BtoC(var)

    colorprint("var = BtoC(var) -> ", color = Colors.blanc,end = False)
    colorprint(var, color = Colors.cyan)

    var = TtoB(var)

    old = var

    colorprint("var = TtoB(var) -> ", color = Colors.blanc,end = False)
    colorprint(var, color = Colors.cyan)

    clé = BtoC(var)

    colorprint("clé = BtoC(var) -> ", color = Colors.blanc,end = False)
    colorprint(clé, color = Colors.cyan)

    sort = ""
    passed = 0
    while len(clé) < len(var): clé += clé

    colorprint("var = pert(var) -> ", color = Colors.blanc,end = False)

    for x in range(len(var)):
        passed += 1

        # colorprint(f"[{passed}~{clé[x]}]", color = Colors.green, end = False)

        if int(passed) > int(clé[x]):
            colorprint(var[x], color = Colors.red, end = False)
            passed = 0

        else:
            sort += str(var[x])
            colorprint(var[x], color = Colors.cyan, end = False)

    var = sort

    colorprint("\n                -> ", color = Colors.blanc,end = False)
    colorprint(var, color = Colors.cyan)

    var = BtoN(var)

    colorprint("var = BtoN(var) -> ", color = Colors.blanc,end = False)
    colorprint(str(var), color = Colors.cyan)