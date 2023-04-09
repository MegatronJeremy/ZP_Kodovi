from sympy import Matrix


def decrypt(m, a):
    n = len(m)
    p = len(a)
    c = []
    for i in range(0, n, p):
        for j in range(0, p):
            t = 0
            for k in range(0, p):
                t = (t + m[i+k] * a[k][j]) % 26
            c.append(t)
    return c

m = [[3, 25, 4], [23, 6, 15], [13, 17, 21]]

a = Matrix(m)
a = a.inv_mod(26).tolist()
print(a)

m = "EKYIMBHKXVNAZYUELMVPBJVS"

m = [ord(c) - 65 for c in m]

c = decrypt(m, a)
c = ''.join([chr(m+65) for m in c])
print(c)


