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
    print(st01)
    print(st02)
    print(st03)

    for i in range(32):
        st += str(st01[i] ^ st02[i] ^ st03[i])

    return st


def xor3(a, b, c):
    st = ''
    return int(a) ^ int(b) ^ int(c)

# print(operate_xor('11011110110111100100000011101110', '00011101110110111101101111001000', '00001101111001000000111011101101'))

sadf = '123456789'
print(sadf[0:4])
