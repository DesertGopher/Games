var1 = ''.join(format(x, '08b') for x in bytearray(str(88), 'utf-8'))

print(var1)
print(len(var1))

if len(var1) < 64:
    while len(var1) < 64:
        var1 = str("0" + var1)

print(var1)
print(len(var1))
print('001100010011001000110011000000000000000000000000000000000000000'.find('10000000'))


for i in range (1,10):
    print(i)