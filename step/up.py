from mod.sunbreaker import *

to_find = "0010010110001101"

original = "22312221322"

clé = BtoC(to_find)

clé = "".join(str(int(c)+1) for c in clé)

print(clé)
print(original)

'''


11011 -> 212
1111  -> 4


'''