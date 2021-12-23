from moonbreaker import moonbreaker

# Break de 8 chiffres -> 0.0001 MoonCoin
# Break de 7 chiffres -> 0.001  MoonCoin
# Break de 6 chiffres -> 0.01   MoonCoin
# Break de 5 chiffres -> 0.1    MoonCoin
# Break de 4 chiffres -> 1      MoonCoin
# Break de 3 chiffres -> 10     MoonCoin

def nombre_en_lettres(nombre):
    sortie = ""
    lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    while nombre > 0:
        reste = nombre % len(lettres)
        sortie += lettres[reste]
        nombre = (nombre - reste) // len(lettres)

    return sortie[::-1]

acc = 0
wallet = 0
while True:
    string = nombre_en_lettres(acc)
    str_break = moonbreaker(string)
    if len(str(str_break)) < 10:
        wallet = round(wallet + 10 ** (10 - len(str(str_break))) / 1000000, 4)
        print(f"Wallet : {wallet} MoonCoins  |   {string} => {str_break} ({len(str(str_break))})")

    acc += 1