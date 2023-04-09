def encrypt(a, key):
    c = ''
    m = len(key)
    while len(a) % m != 0:
        a += 'X'

    a_lst = [ord(c) - 65 for c in a]

    n = len(a)
    p = 0
    while p < n:
        for j in range(m):
            t = 0
            for k in range(m):
                t = (t + key[k][j] * a_lst[p + k]) % 37
            c += chr(t + 65)
        p += m

    return c


def determinant(a: list[list[int]]):
    n = len(a)
    if n == 1:
        return a[0][0]
    elif n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    det = 0
    a_sub = [a[i] for i in range(1, n)]
    for j in range(n):
        b_sub = []
        for i in range(n - 1):
            b_sub.append(a_sub[i][:j] + a_sub[i][j + 1:])
        det += pow(-1, j) * a[0][j] * determinant(b_sub)

    return det


def cofactor(a: list[list[int]]):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a_sub = a[:]
        a_sub.remove(a[i])
        for j in range(n):
            b_sub = []
            for k in range(len(a_sub)):
                b_sub.append(a_sub[k][:j] + a_sub[k][j + 1:])
            c[i][j] = pow(-1, i + j) * determinant(b_sub) % 37

    return c


def transpose(a: list[list[int]]):
    n = len(a)
    for i in range(n):
        for j in range(i + 1):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


def mul(a: list[list[int]], k):
    n = len(a)
    for i in range(n):
        for j in range(n):
            a[i][j] = (a[i][j] * k) % 37
    return a


def decrypt(c, key):
    det = determinant(key) % 37
    inv_det = pow(det, -1, 37)

    cof = cofactor(key)

    adj = transpose(cof)

    inv_k = mul(adj, inv_det)
    print(inv_k)

    d = encrypt(c, inv_k)
    return d


def main():
    #k = [[3, 25, 4], [23, 6, 15], [13, 17, 21]]
    k = [[11, 24], [13, 8]]
    #a = "ahauflakjfhdasflkjh"
    #a = a.upper()

    #c = encrypt(a, k)
   # print(c)

    c = "1KVO3K"

    d = decrypt(c, k)
    print(d)


if __name__ == '__main__':
    main()
