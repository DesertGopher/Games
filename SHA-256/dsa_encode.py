from sha_encode import *


def dsa(phrase):
    hashed = custom_encode(phrase)
    hashed = (convert_to(int(hashed, 16), 2))
    hash_len = len(str(hashed))

    q = "1"
    for i in range(hash_len-1):
        q += "0"
    q = int(q, 2)
    p = int(q) + 1

    g = 4
    x = 10  # секретный ключ
    k = 5

    # Для проверки
    # q = 11
    # p = 23
    # hash_len = 9
    # x = 7
    # k = 3

    y = pow(g, x) % p  # открытый ключ
    r = (pow(g, k) % p) % int(q)
    s = (euclid_ext(k, q)[1] * (hash_len + x * r)) % q

    w = euclid_ext(s, q)[1]
    u1 = hash_len * w % q
    u2 = r * w % q
    v = (pow(g, u1) * pow(y, u2) % p) % q

    print(f'Хэш : {custom_encode(phrase)}')
    print(f'Подпись : ({r}, {s})')
    print(f'Проверка подписи : v = {v}')
    if v == r:
        print('                   v = r ---> Подпись верна')
    else:
        print('loh')


def euclid_ext(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclid_ext(b, a % b)
        return d, y, x - y * (a // b)


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


message = input(str("Phrase to DSA: "))
dsa(message)
