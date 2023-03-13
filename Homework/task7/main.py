def main(hex_num: str):
    number = int(hex_num, 16)

    u5 = number >> 28
    number -= u5 << 28

    u4 = number >> 18
    number -= u4 << 18
    u3 = number >> 9
    number -= u3 << 9

    u2 = number >> 7
    number -= u2 << 7

    return [('U1', hex(number)), ('U2', hex(u2)),
            ('U3', hex(u3)), ('U4', hex(u4)), ('U5', hex(u5))]


print(main('0x13591364'))  # [('U1', '0x64'), ('U2', '0x2'), ('U3', '0x89'), ('U4', '0xd6'), ('U5', '0x1')]
print(main('0xb9a7d0ee'))  # [('U1', '0x6e'), ('U2', '0x1'), ('U3', '0x1e8'), ('U4', '0x269'), ('U5', '0xb')]
# print(main('0xa1b28039'))
# print(main('0x315da5ee'))