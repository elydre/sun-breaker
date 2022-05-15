from moonbreaker import moonbreaker
from multiprocessing import Pool
from random import choice

def check_loop(string):
    h = [string]
    for i in range(10 ** 10):
        temp = str(moonbreaker(h[-1], 42))
        # print(temp)
        if temp not in h:
            h.append(temp)
        else:
            return [i, string, h.index(temp)]

if __name__ == "__main__":
    maxi, bs, sri = 0, "", 0
    while True:
        s = ["".join(choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)) for _ in range(10000)]
        with Pool(processes=47) as pool:
            res = pool.map(check_loop, s)
        sri += 1
        print(f"---- {sri} ----")
        for i in res:
            if i[0] >= maxi:
                maxi, bs = i[0], i[1]
                print(f"{bs} -> {maxi} = {i[2]}")