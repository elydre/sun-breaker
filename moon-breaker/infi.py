from moonbreaker import moonbreaker
from multiprocessing import Pool
from random import choice

def check_loop(info):
    h = [info[0]]
    for i in range(10 ** 10):
        temp = str(moonbreaker(h[-1], info[1]))
        # print(temp)
        if temp not in h:
            h.append(temp)
        else:
            return [i, info[0], h.index(temp)]

if __name__ == "__main__":
    maxi, bs = 0, ""
    for sri in range(2, 500):
        s = ["".join(choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)) for _ in range(3000)]
        s = [[e, sri] for e in s]
        with Pool(processes=4) as pool:
            res = pool.map(check_loop, s)
        print(f"---- {sri} ----")
        for i in res:
            if i[0] >= maxi:
                maxi, bs = i[0], i[1]
                print(f"{bs} -> {maxi} = {i[2]}")