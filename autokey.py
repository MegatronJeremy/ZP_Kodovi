def encrypt(a: str, k: str):
    c = ''
    a_lst = [ord(c) - 65 for c in a]
    k_lst = [ord(c) - 65 for c in k]
    n = len(a_lst)
    m = len(k_lst)
    for i in range(m):
        c += chr(65 + (a_lst[i] + k_lst[i]) % 26)
    for i in range(m, n):
        c += chr(65 + (a_lst[i] + a_lst[i - m]) % 26)
    return c


def decrypt(c: str, k: str):
    d = ''
    c_lst = [ord(c) - 65 for c in c]
    k_lst = [ord(c) - 65 for c in k]
    n = len(c_lst)
    m = len(k_lst)
    for i in range(m):
        d += chr(65 + (c_lst[i] - k_lst[i]) % 26)
    for i in range(m, n):
        d += chr(65 + (c_lst[i] - ord(d[i - m]) + 65) % 26)
    return d


def main():
    a = 'yoyoyoitshumpday'
    k = 'KLJUC'

    a = a.upper()
    k = k.upper()

    # c = encrypt(a, k)
    # print(d)

    c = 'CLJPCDOMKLLJABFDVZVCQIVJWOZOG'

    d = decrypt(c, k)
    print(d)


if __name__ == '__main__':
    main()
