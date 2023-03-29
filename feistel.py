pc1 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
rot1 = 1
rot2 = 1
pc2 = (6, 3, 7, 4, 8, 5, 10, 9)
ip = (2, 6, 3, 1, 4, 8, 5, 7)
ip_inv = (4, 1, 3, 5, 7, 2, 8, 6)
e = (4, 1, 2, 3, 2, 3, 4, 1)
s1 = ((1, 0, 3, 2), (3, 2, 1, 0), (0, 2, 1, 3), (3, 1, 0, 2))
s2 = ((0, 1, 2, 3), (2, 0, 1, 3), (3, 0, 1, 2), (2, 1, 0, 3))
p = (2, 4, 3, 1)


def key_round(k: list[int]):
    print("Key round")

    kls, krs = [], []
    for i in range(0, 5):
        kls.append(k[(i + rot1) % 5])
    for i in range(0, 5):
        krs.append(k[(i + rot1) % 5 + 5])

    kt = kls + krs
    print(kt)

    k1 = []
    for perm in pc2:
        k1.append(kt[perm - 1])

    print(k1)

    return k1, kt


def function_round(m: list[int], k: list[int]):
    print("Function round")

    ml = m[:4]
    mr = m[4:]

    print(ml, mr)

    r1 = []
    for exp in e:
        r1.append(mr[exp - 1])

    print(r1)

    for i in range(len(r1)):
        r1[i] = r1[i] ^ k[i]

    rl = r1[:4]
    rr = r1[4:]

    print(rl, rr)
    left = s1[(rl[0] << 1) + rl[3]][(rl[1] << 1) + rl[2]]
    right = s2[(rr[0] << 1) + rr[3]][(rr[1] << 1) + rr[2]]
    print(left, right)

    r1 = [int(x) for x in format(left, '#04b')[2:]]
    r1 += [int(x) for x in format(right, '#04b')[2:]]

    print(r1)

    rp = []
    for perm in p:
        rp.append(r1[perm - 1])

    print(rp)

    for i in range(len(rp)):
        rp[i] = rp[i] ^ ml[i]

    print(rp)

    return mr + rp


def feistel(m, k, inv: bool):
    kp = []

    for perm in pc1:
        kp.append(k[perm - 1])

    k1, kt = key_round(kp)
    k2, kt = key_round(kt)

    if inv:
        k1, k2 = k2, k1

    mp = []
    for perm in ip:
        mp.append(m[perm - 1])

    print(mp)

    c1 = function_round(mp, k1)
    c2 = function_round(c1, k2)
    c2 = c2[4:] + c2[:4]
    c = []

    for perm in ip_inv:
        c.append(c2[perm - 1])
    print(c)

    return c


def main():
    m = [1, 0, 1, 1, 1, 1, 0, 1]
    k = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]

    c = feistel(m, k, False)
    print()

    d = feistel(c, k, True)


if __name__ == '__main__':
    main()
