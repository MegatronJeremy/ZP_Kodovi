def main():
    k = "qwertzuiopasdfghjklyxcvbnm"

    key_dict = {}
    inv_dict = {}
    for i in range(26):
        key_dict[chr(97 + i)] = k[i]
        inv_dict[k[i]] = chr(97 + i)

    a = 'napadamo u podne ako ne bude vetra'
    a = a.replace(' ', 'x')

    # encrypt
    c = ''
    for char in a:
        c += key_dict[char]

    print(c)

    # decrypt
    d = ''
    for char in c:
        d += inv_dict[char]

    d = d.replace('x', ' ')
    print(d)


if __name__ == '__main__':
    main()
