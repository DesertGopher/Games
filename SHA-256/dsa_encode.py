import random
from sha_encode import *


def so_sign(phrase):
    hashed = custom_encode(phrase)
    q = pow(2, 159)
    p = pow(2, 511)
    h = 2
    g = pow(h, (p-1)/q) % p

    print(q)
    print(p)
    print(g)


message = input(str("Phrase to DSA: "))
so_sign(message)
