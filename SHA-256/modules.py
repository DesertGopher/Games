import re
import time

from rich.progress import track
from rich.console import Console
from itertools import zip_longest

console = Console(highlight=False, color_system="windows")


def get_string_8(text, last_symbol=None):
    """Метод возвращения читабельной строки 8 бит"""
    if last_symbol:
        return ' '.join(text[i:i + 8] for i in range(0, len(text), 8))[:-1] + '[magenta]1' + "\n"
    else:
        return ' '.join(text[i:i + 8] for i in range(0, len(text), 8)) + "\n"


def get_string_32(text):
    """Метод возвращения читабельной строки 32 бита"""
    return ' '.join(text[i:i + 32] for i in range(0, len(text), 32)) + "\n"


def get_32_mass(text):
    new_string = ""
    for letter_index in range(0, 65):
        new_string += text[letter_index]

    shortened_text = text[65:]

    for letter_index in range(len(shortened_text)):

        if letter_index % 66 == 0:
            new_string += f"{shortened_text[letter_index]}\n"
        else:
            new_string += shortened_text[letter_index]
    return new_string


def console_output_8(message, text, last_symbol=None):
    console.print(str("[green]" + message))
    console.print(str("[blue]" + get_string_8(text, last_symbol)))


def get_code_mass_three(text):
    """Метод возвращения читабельного массива байт"""
    new_string = ""
    for letter_index in range(0, 71):
        new_string += text[letter_index]

    shortened_text = text[71:]

    for letter_index in range(len(shortened_text)):

        if letter_index % 72 == 0:
            new_string += f"{shortened_text[letter_index]}\n"
        else:
            new_string += shortened_text[letter_index]

    console.print(str("[green]1.3. Заполняем нулями до тех пор, пока данные не станут кратны 512 без последних 64 бит"))
    console.print(str("[blue]" + new_string[0:new_string.find(' 10000000 00000000 ')] +
                      "[magenta]" + new_string[new_string.find(' 10000000 '):new_string.find(' 10000000 ')+10] +
                      "[blue]" + new_string[new_string.find(' 10000000 ')+10:]
                      ))


def get_code_mass_four(text, sf_byte_num):
    """Метод возвращения читабельного массива байт"""
    new_string = ""
    for letter_index in range(0, 71):
        new_string += text[letter_index]

    shortened_text = text[71:]

    for letter_index in range(len(shortened_text)):

        if letter_index % 72 == 0:
            new_string += f"{shortened_text[letter_index]}\n"
        else:
            new_string += shortened_text[letter_index]

    console.print(
        str("[green]1.4. Добавим 64 бита в конец, где 64 бита — целое число с порядком байтов big-endian, \n"
            "     обозначающее длину входных данных в двоичном виде. \n"
            "     В нашем случае [magenta]" + str(int(sf_byte_num, 2)) +
            "[green], в двоичном виде — [magenta]«" + sf_byte_num + "»"))

    console.print(str("[blue]" + new_string[0:-73] + "[magenta]" + new_string[-73:]))


def first_step(text):
    console_output_8("1.1. Преобразуем текст в двоичный код.", text)


def second_step(text):
    console_output_8("1.2. Добавляем одну единицу.", text, last_symbol='magenta')


def third_step(text):
    get_code_mass_three(get_string_8(text))


def forth_step(text, sf):
    get_code_mass_four(get_string_8(text), sf)


def fifth_step(text):
    console.print(str("[green]2.1. Копируем входные "
                      "данные из шага 1 в новый массив, где каждая запись является 32-битным словом."))
    console.print(str("[blue]" + get_32_mass(get_string_32(text))))


def sixth_step_output(text):
    console.print(str("[green]2.2. Добавляем ещё 48 слов, инициализированных нулями, чтобы получить массив w[0…63]"))
    console.print(str("[blue]" + get_32_mass(get_string_32(text)) + "----------"))
    console.print(str("[blue]00000000000000000000000000000000 00000000000000000000000000000000\n"
                      "00000000000000000000000000000000 00000000000000000000000000000000"))


def sixth_step(text):
    return get_32_mass(get_string_32(text))


def rotate_right(block, d):
    start = block[0: len(block)-d]
    end = block[len(block)-d:]
    return str(str(end) + str(start))


def shift_right(block, d):
    start = block[0: len(block)-d]
    end = ''
    for i in range(d):
        end += '0'
    return str(str(end) + str(start))


def bin_add(b1, b2):
    p = 0
    r = ''
    for i, j in zip_longest(b1[::-1], b2[::-1], fillvalue='0'):
        p, d = divmod(int(i) + int(j) + p, 2)
        r = str(d) + r
    if p:
        r = str(p) + r
    return r


def operate_xor(s01, s02, s03):
    a = 1

    st01 = []
    st02 = []
    st03 = []

    for i in range(0, len(s01), a):
        st01.append(int(s01[i: i + a]))
    for i in range(0, len(s02), a):
        st02.append(int(s02[i: i + a]))
    for i in range(0, len(s03), a):
        st03.append(int(s03[i: i + a]))

    st = ''

    for i in range(32):
        st += str(int(st01[i]) ^ int(st02[i]) ^ int(st03[i]))

    return st


def operate_xor_2(s01, s02):
    a = 1

    st01 = []
    st02 = []
    for i in range(0, len(s01), a):
        st01.append(int(s01[i: i + a]))
    for i in range(0, len(s02), a):
        st02.append(int(s02[i: i + a]))

    st = ''

    for i in range(32):
        st += str(int(st01[i]) ^ int(st02[i]))

    return st


def seventh_step(words):
    out = ''
    i = 1
    for word in words:
        i += 1
        if word.startswith('1'):
            out += str("[magenta]" + str(word) + " " if i % 2 == 0 else "[magenta]" + str(word) + "\n")
        else:
            out += str("[blue]" + str(word) + " " if i % 2 == 0 else "[blue]" + str(word) + "\n")

    console.print("\n\n[green]2.3. Изменяем нулевые индексы в конце массива, используя алгоритм со сдвигом вправо \n"
                  "     Это оставляет нам 64 слова в нашей очереди сообщений")
    console.print(out)


def operate_and(s01, s02):
    a = 1

    st01 = []
    st02 = []

    for i in range(0, len(s01), a):
        st01.append(int(s01[i: i + a]))
    for i in range(0, len(s02), a):
        st02.append(int(s02[i: i + a]))

    st = ''

    for i in range(32):
        if st01[i] == 1 and st02[i] == 1:
            st += '1'
        else:
            st += '0'
    return st


def operate_not(s01):
    a = 1

    st01 = []
    for i in range(0, len(s01), a):
        st01.append(int(s01[i: i + a]))

    st = ''

    for i in range(32):
        if st01[i] == 1:
            st += '0'
        else:
            st += '1'
    return st


def to_bin(h):
    word = str(bin(h))
    word = re.sub('b', '', word)
    len_shorten(word)
    len_lengthen(word)
    return str(word)


def to_bin_k(h):
    word = str(bin(h))
    word = re.sub('b', '', word)
    len_shorten(word)
    return str(word)


def len_shorten(word):
    if len(word) > 32:
        word = word[len(word) - 32:len(word)]
    return str(word)


def len_lengthen(word):
    if len(word) <= 32:
        while len(word) != 32:
            word = '0' + word
    return word


def shorten_32(word):
    if len(word) < 32:
        while len(word) != 32:
            word = '0' + word
    elif len(word) > 32:
        while len(word) != 32:
            word = word[1:]
    else:
        return word
    return word


def eighth_step():
    console.print("\n\n[green]3.1. Инициализируем значения хэша:" + '\n'
"     [white]h0 [red]= [magenta]0x6a09e667" + '\n'
"     [white]h1 [red]= [magenta]0xbb67ae85" + '\n'
"     [white]h2 [red]= [magenta]0x3c6ef372" + '\n'
"     [white]h3 [red]= [magenta]0xa54ff53a" + '\n'
"     [white]h5 [red]= [magenta]0x9b05688c" + '\n'
"     [white]h4 [red]= [magenta]0x510e527f" + '\n'
"     [white]h6 [red]= [magenta]0x1f83d9ab" + '\n'
"     [white]h7 [red]= [magenta]0x5be0cd19" + '\n'
"     [white]K [red]= [[magenta]" + '\n'
"             0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5," + '\n'
"             0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174," + '\n'
"             0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da," + '\n'
"             0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967," + '\n'
"             0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85," + '\n'
"             0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070," + '\n'
"             0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3," + '\n'
"             0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2" + '\n'
"         [red]]\n\n")


def ninth_step(a, b, c, d, e, f, g, h, h0, h1, h2, h3, h4, h5, h6, h7):
    console.print("[green]3.2. Инициализируем переменные a, b, c, d, e, f, g, h и "
                  "установим их равными текущим значениям хеша соответственно. h0, h1, h2, h3, h4, h5, h6, h7.\n"
                  "     Запустим цикл сжатия, который будет изменять значения a…h. \n"
                  "     Расчеты выполняются 64 раза и в итоге получается следующее...")
    console.print("[white]h0" + " [red]= [magenta]" + hex(int(h0, 2))[2:] + " [red]= [magenta]" + h0 + '\n'
                  "[white]h1" + " [red]= [magenta]" + hex(int(h1, 2))[2:] + " [red]= [magenta]" + h1 + '\n'
                  "[white]h2" + " [red]= [magenta]" + hex(int(h2, 2))[2:] + " [red]= [magenta]" + h2 + '\n'
                  "[white]h3" + " [red]= [magenta]" + hex(int(h3, 2))[2:] + " [red]= [magenta]" + h3 + '\n'
                  "[white]h4" + " [red]= [magenta]" + hex(int(h4, 2))[2:] + " [red]= [magenta]" + h4 + '\n'
                  "[white]h5" + " [red]= [magenta]" + hex(int(h5, 2))[2:] + " [red]= [magenta]" + h5 + '\n'
                  "[white]h6" + " [red]= [magenta]" + hex(int(h6, 2))[2:] + " [red]= [magenta]" + h6 + '\n'
                  "[white]h7" + " [red]= [magenta]" + hex(int(h7, 2))[2:] + " [red]= [magenta]" + h7 + '\n\n'
                  "[white]a" + " [red]= [magenta]" + hex(int(a, 2))[2:] + " [red]= [magenta]" + a + '\n'
                  "[white]b" + " [red]= [magenta]" + hex(int(b, 2))[2:] + " [red]= [magenta]" + b + '\n'
                  "[white]c" + " [red]= [magenta]" + hex(int(c, 2))[2:] + " [red]= [magenta]" + c + '\n'
                  "[white]d" + " [red]= [magenta]" + hex(int(d, 2))[2:] + " [red]= [magenta]" + d + '\n'
                  "[white]e" + " [red]= [magenta]" + hex(int(e, 2))[2:] + " [red]= [magenta]" + e + '\n'
                  "[white]f" + " [red]= [magenta]" + hex(int(f, 2))[2:] + " [red]= [magenta]" + f + '\n'
                  "[white]g" + " [red]= [magenta]" + hex(int(g, 2))[2:] + " [red]= [magenta]" + g + '\n'
                  "[white]h" + " [red]= [magenta]" + hex(int(h, 2))[2:] + " [red]= [magenta]" + h + '\n')


def progress_display(secs):
    for i in track(range(secs), description="Calculating..."):
        time.sleep(0.005)
