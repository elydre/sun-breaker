from time import time
from moonbreaker import moonbreaker

def test_moonbreaker(txt, key, result, nom):
    debut = time()
    true_res = moonbreaker(txt, key)
    temps = round(time() - debut + 0.0001, 4)
    if true_res == result:
        print(f"OK: ({temps}s) [k{key}] - {nom}")
    else:
        print(f"FAIL: ({temps}s) [k{key}] - {nom}")
        print(f"\tResult : {true_res}")
        print(f"\tExpected : {result}")

tests = [
    ("a", 2, 5305600000, "car"),
    ("a", 1000, 2731977983, "car"),
    ("4", 2, 5881600000, "number"),
    ("4", 1000, 3028573904, "number"),
    ("00P", 2, 259051, "small break"),
    ("Hello World!", 2, 5442031631, "basic string"),
    ("Hello World!", 500, 5381480021, "basic string"),
    ("Les chaussettes de l'archiduchesse sont trop longues.", 2, 21832282, "sentence"),
    ("Les chaussettes de l'archiduchesse sont trop longues.", 150, 2923866834, "sentence"),
]

for t in tests:
    test_moonbreaker(*t)