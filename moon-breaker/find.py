from moonbreaker import moonbreaker
from random import choice, randint

lettres = "abcdefghijklmnopqrstuvwxyz"
best = 10**11

def random_string():
    length = randint(4, 6)
    return "".join(choice(lettres) for i in range(length))


while True:
    string = random_string()
    break_code = moonbreaker(string)
    if break_code < best:
        best = break_code
        print(best, "|" ,string)