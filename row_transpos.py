def encrypt(c: str, key: list[int]):
    n = len(key)
    res = ['' for _ in range(len(c))]

    m = len(c) // n
    for i in range(len(c)):
        j = (key[i % n] - 1) * m + i // n
        res[j] = c[i]

    return ''.join(res)


def decrypt(c: str, key: list[int]):
    res = ''
    n = len(key)
    m = len(c) // n
    for i in range(len(c)):
        j = (key[i % n] - 1) * m + i // n
        res += c[j]

    return res


def main():
    a = 'GLASSOFJUICE'
    k = [4, 3, 1, 2, 5, 6, 7]

    while len(a) % len(k) != 0:
        a += 'X'

    c = encrypt(a, k)
    print(c)

    c = encrypt(c, k)
    print(c)

    d = decrypt(c, k)
    print(d)

    d = decrypt(d, k)
    print(d)


if __name__ == '__main__':
    main()
