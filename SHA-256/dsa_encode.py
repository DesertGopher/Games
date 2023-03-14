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
    # print(q)

    g = 4
    x = 10  # секретный ключ
    k = 5

    # Для проверки
    q = 11
    p = 23
    hash_len = 9
    x = 7
    k = 3

    y = pow(g, x) % p  # открытый ключ
    print(f'y = {y}')

    r = (pow(g, k) % p) % int(q)
    print(f'r = {r}')

    s = (euclid_ext(k, q)[1] * (hash_len + x * r)) % q
    print(f's = {s}')

    # проверка
    w = euclid_ext(s, q)[1]
    print(f'w = {w}')

    u1 = hash_len * w % q
    print(f'u1 = {u1}')

    u2 = r * w % q
    print(f'u2 = {u2}')

    v = (pow(g, u1) * pow(y, u2) % p) % q

    print(f'             Хэш : {custom_encode(phrase)}')
    print(f'         Подпись : ({r}, {s})')
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
