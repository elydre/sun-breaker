from mod.sunbreaker import *
from mod.ColorPrint import colorprint, Colors
import random

var = "".join(random.choice("1234") for _ in range(random.randint(1, 4)))

print("Texte:",var)

var = TtoB(var)

old = var

clé = BtoC(var)


sort = ""
passed = 0
while len(clé) < len(var): clé += clé

for x in range(len(var)):
    passed += 1
    if int(passed) > int(clé[x]): passed = 0
    else:  sort += str(var[x])

var = sort
var = BtoN(var)

colorprint("var = BtoN(var) -> ", color = Colors.blanc,end = False)
colorprint(str(var), color = Colors.cyan)