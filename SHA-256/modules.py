from rich.console import Console

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


def sixth_step(text):
    console.print(str("[green]2.2. Добавляем ещё 48 слов, инициализированных нулями, чтобы получить массив w[0…63]"))
    console.print(str("[blue]" + get_32_mass(get_string_32(text)) + "----------"))
    console.print(str("[blue]00000000000000000000000000000000 00000000000000000000000000000000\n"
                      "00000000000000000000000000000000 00000000000000000000000000000000"))


