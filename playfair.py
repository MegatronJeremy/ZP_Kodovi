def encrypt(a: str, key_dict, inv_dict):
    c = ""
    for i in range(len(a) // 2):
        ind1 = inv_dict[a[i * 2]]
        row1 = ind1 // 5
        col1 = ind1 % 5

        ind2 = inv_dict[a[i * 2 + 1]]
        row2 = ind2 // 5
        col2 = ind2 % 5

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        ind1 = row1 * 5 + col1
        ind2 = row2 * 5 + col2

        c += key_dict[ind1] + key_dict[ind2]

    return c


def decrypt(a: str, key_dict, inv_dict):
    d = ""
    for i in range(len(a) // 2):
        ind1 = inv_dict[a[i * 2]]
        row1 = ind1 // 5
        col1 = ind1 % 5

        ind2 = inv_dict[a[i * 2 + 1]]
        row2 = ind2 // 5
        col2 = ind2 % 5

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        ind1 = row1 * 5 + col1
        ind2 = row2 * 5 + col2

        d += key_dict[ind1] + key_dict[ind2]

    return d


def main():
    a = 'perangustaadaugusta'
    key = 'disleksija'

    a = a.upper()
    a = a.replace(' ', 'X')
    a = a.replace('J', 'I')

    for i in range(len(a) // 2):
        if a[i * 2] == a[i * 2 + 1]:
            a = a[:i * 2 + 1] + 'X' + a[2 * i + 1:]

    if len(a) % 2 != 0:
        a += 'X'

    print(a)

    key = key.upper()
    key = key.replace('J', 'I')

    key_set = set([i for i in range(0, 26)])
    key_set.remove(9)

    key_dict: dict = {}
    inv_dict: dict = {}

    i = 0
    for k in key:
        if (ord(k) - 65) not in key_set:
            continue
        key_dict[i] = k.upper()
        inv_dict[k.upper()] = i
        key_set.remove(ord(k) - 65)
        i += 1

    for j in range(0, 26):
        if j not in key_set:
            continue
        c = chr(j + 65)
        key_dict[i] = c
        inv_dict[c] = i
        key_set.remove(j)
        i += 1

    # encryption
    c = encrypt(a, key_dict, inv_dict)
    print(c)

    # decryption
    d = decrypt(c, key_dict, inv_dict)
    d = d.replace('X', ' ')
    print(d)


if __name__ == '__main__':
    main()
