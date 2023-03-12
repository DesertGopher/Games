import hashlib
import re

from rich.console import Console
import modules

console = Console(highlight=False, color_system="windows")

K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]


def custom_encode(phrase):
    """Метод с рукописной кодировкой SHA-256"""

    # 1.1. Переводим строку в двоичный код
    text = ''.join(format(x, '08b') for x in bytearray(phrase, 'utf-8'))
    # modules.first_step(text)

    # 1.2. Добавляем в конец одну единицу
    text = str(text + "1")
    # modules.second_step(text)

    # 1.3. Добавляем нули, чтобы длина стала кратна 512 без последних 64 символов
    while len(text) % 512 != 0:
        text = str(text + "0")
    text = text[:-64]
    # modules.third_step(text)

    # 1.4. Находим длину входных данных в двоичном коде и добавляем в конец в виде 64 битов
    sf_byte_num = bin(len(''.join(format(x, '08b') for x in bytearray(phrase, 'utf-8'))))[2:]
    sf_byte_num_code = sf_byte_num
    if len(sf_byte_num_code) < 64:
        while len(sf_byte_num_code) < 64:
            sf_byte_num_code = str("0" + sf_byte_num_code)
    text = str(text + sf_byte_num_code)
    # modules.forth_step(text, sf_byte_num)

    # 2.1. Делим входные данные на 32-битные слова (повторять для каждого 512-битного куска
    # modules.fifth_step(text)
    sub_text = text

    # 2.2. Добавляем еще 48 слов их нулей, чтобы было кратно 64
    for i in range(48):
        for j in range(32):
            text = text + "0"
    # modules.sixth_step_output(sub_text)
    text_block = modules.sixth_step(text)

    # Переводим строку в массив из 32-х битных слов
    words = []
    for i in range(64):
        words.append(re.compile(r'\w+').findall(text_block)[i])

    # 2.3. Изменяем нулевые индексы в конце массива, используя следующий алгоритм

    for i in range(16, 64):
        s01 = str(modules.rotate_right(str(words[i-15]), 7))
        s02 = str(modules.rotate_right(str(words[i-15]), 18))
        s03 = str(modules.shift_right(str(words[i-15]), 3))

        s0 = modules.operate_xor(s01, s02, s03)

        s11 = str(modules.rotate_right(str(words[i-2]), 17))
        s12 = str(modules.rotate_right(str(words[i-2]), 19))
        s13 = str(modules.shift_right(str(words[i-2]), 10))

        s1 = modules.operate_xor(s11, s12, s13)
        words[i] = modules.bin_add(modules.bin_add(str(words[i-16]), str(s0)),
                                   modules.bin_add(str(words[i-7]), str(s1)))
        if len(words[i]) > 32:
            words[i] = words[i][len(words[i])-32:len(words[i])]
    # modules.seventh_step(words)
    # modules.progress_display(40)

    # Инициализируем 8 значений хеша
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h5 = 0x9b05688c
    h4 = 0x510e527f
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
    # modules.eighth_step()
    # modules.progress_display(40)

    # Инициализируем рабочие переменные
    a = modules.shorten_32(modules.to_bin(h0))
    b = modules.shorten_32(modules.to_bin(h1))
    c = modules.shorten_32(modules.to_bin(h2))
    d = modules.shorten_32(modules.to_bin(h3))
    e = modules.shorten_32(modules.to_bin(h4))
    f = modules.shorten_32(modules.to_bin(h5))
    g = modules.shorten_32(modules.to_bin(h6))
    h = modules.shorten_32(modules.to_bin(h7))

    # 3.1. Запустим цикл сжатия, который будет изменять значения a…h

    for i in range(64):

        s11 = modules.rotate_right(str(e), 6)
        s12 = modules.rotate_right(str(e), 11)
        s13 = modules.rotate_right(str(e), 25)

        s1 = modules.operate_xor(s11, s12, s13)

        e_and_f = modules.operate_and(e, f)
        not_e = modules.operate_not(e)
        not_e_and_g = modules.operate_and(not_e, g)
        ch = modules.operate_xor_2(e_and_f, not_e_and_g)

        temp1 = modules.len_shorten(
            modules.bin_add(
                modules.bin_add(
                    modules.bin_add(h, s1), ch
                ),
                modules.bin_add(modules.to_bin(K[i]), words[i])))

        s01 = modules.rotate_right(str(a), 2)
        s02 = modules.rotate_right(str(a), 13)
        s03 = modules.rotate_right(str(a), 22)
        s0 = modules.operate_xor(s01, s02, s03)

        a_and_b = modules.operate_and(a, b)
        a_and_c = modules.operate_and(a, c)
        b_and_c = modules.operate_and(b, c)
        maj = modules.operate_xor(a_and_b, a_and_c, b_and_c)

        temp2 = modules.len_shorten(modules.bin_add(s0, maj))

        if i == 0:
            h0 = a
            h1 = b
            h2 = c
            h3 = d
            h4 = e
            h5 = f
            h6 = g
            h7 = h

        h = g
        g = f
        f = e
        e = modules.len_shorten(modules.bin_add(d, temp1))
        d = c
        c = b
        b = a
        a = modules.len_shorten(modules.bin_add(temp1, temp2))

    a = '0' + a
    b = '0' + b
    c = '0' + c
    d = '0' + d
    e = '0' + e
    f = '0' + f
    g = '0' + g
    h = '0' + h
    # modules.ninth_step(a, b, c, d, e, f, g, h, h0, h1, h2, h3, h4, h5, h6, h7)
    # modules.progress_display(40)

    h0 = modules.shorten_32(modules.bin_add(h0, a))
    h1 = modules.shorten_32(modules.bin_add(h1, b))
    h2 = modules.shorten_32(modules.bin_add(h2, c))
    h3 = modules.shorten_32(modules.bin_add(h3, d))
    h4 = modules.shorten_32(modules.bin_add(h4, e))
    h5 = modules.shorten_32(modules.bin_add(h5, f))
    h6 = modules.shorten_32(modules.bin_add(h6, g))
    h7 = modules.shorten_32(modules.bin_add(h7, h))

    result = str(hex(int(h0, 2))[2:]) + str(hex(int(h1, 2))[2:]) + str(hex(int(h2, 2))[2:]) + str(hex(int(h3, 2))[2:]) + \
             str(hex(int(h4, 2))[2:]) + str(hex(int(h5, 2))[2:]) + str(hex(int(h6, 2))[2:]) + str(hex(int(h7, 2))[2:])
    # console.print("[green]3.3. Складываем значения a..h и h0...h7 друг с другом и, "
    #               "совмещая в строку, получим результат.")
    return result


def encode_lib(phrase):
    """Метод со стандартной кодировкой SHA-256"""
    return hashlib.sha256(phrase.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    message = input(str("Phrase to hash: "))
    console.print("[green]Custom SHA-256    : " + "[red]" + custom_encode(message))
    console.print('[green]SHA-256 encoding  : ' + "[red]" + encode_lib(message))
