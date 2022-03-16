from moonbreaker import moonbreaker
from moon_pre import moonbreaker as moonbreaker_pre
from os import cpu_count
from random import choice, randint
from multiprocessing import Pool

coef = 2
max_string_len = 20
min_key = 3
max_key = 45

def compare(l):
    try:
        txt, key = l
        pre = moonbreaker_pre(txt, key)
        res = moonbreaker(txt, key)
        if pre != res:
            print(f"[k{key}] - {txt}")
            print(f"\tpre : {pre}")
            print(f"\tres : {res}")
    except KeyboardInterrupt:
        return 1

if __name__ == "__main__":
    while True:
        liste = [
            ("".join(
                choice("abcdefghijklmnopqrstuvwxyz0123456789")
                for _ in range(randint(1, max_string_len))
            ), randint(min_key, max_key))
            for _ in range(cpu_count() * coef)
        ]

        with Pool(cpu_count()) as p:
            sortie = p.map(compare, liste)

        if all(sortie):
            break