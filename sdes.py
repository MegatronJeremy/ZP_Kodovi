pc1 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 7]
pc2 = [6, 3, 7, 4, 8, 5, 10, 9]
ip = [2, 6, 3, 1, 4, 8, 5, 7]
ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
e = [4, 1, 2, 3, 2, 3, 4, 1]
s1 = [[1, 0, 3, 2],[3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
s2 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 2], [2, 1, 0, 3]]
p = [2, 4, 3, 1]

def key_iter(k, rot):
    k_e = [0 for _ in range(8)]
    k_lf = [0 for _ in range(5)]
    k_rf = [0 for _ in range(5)]

    k_lf = k[0:5]
    k_rf = k[5:10]

    k_lf = k_lf[rot:] + k_lf[0:rot]
    k_rf = k_rf[rot:] + k_rf[0:rot]

    k = k_lf + k_rf

    k1 = k_e[:]
    for i in range(8):
        k1[i] = k[pc2[i]-1]

    return k, k1

def func(m, k):
    l0 = m[0:4]
    r0 = m[4:]
    
    r_e = [0 for _ in range(8)]
    for i in range(8):
        r_e[i] = r0[e[i]-1]
        r_e[i] = r_e[i] ^ k[i]

    r1 = r0[:]
    t1 = (r_e[0] << 1) | r_e[3]
    t2 = (r_e[1] << 1) | r_e[2]

    v = s1[t1][t2]
    
    r1[0] = (v & 0b10) >> 1
    r1[1] = v & 0b1

    t1 = (r_e[4] << 1) | r_e[7]
    t2 = (r_e[5] << 1) | r_e[6]

    v = s2[t1][t2]

    r1[2] = (v & 0b10) >> 1
    r1[3] = v & 0b1

    r2 = r1[:]
    for i in range(4):
        r2[i] = r1[p[i]-1]

    for i in range(4):
        l0[i] = l0[i] ^ r2[i]
    
    return l0 + r0


k = [0,0,1,1,0,0,1,1,0,0]
m = [0,0,1,1,1,1,0,0]

k_t = [0 for _ in range(10)]
for i in range(len(k)):
    k_t[i] = k[pc1[i]-1]
k = k_t

k, k1 = key_iter(k, 1)

print(k1)

k, k2 = key_iter(k, 2)

print(k2)

m_t = [0 for _ in range(8)]
for i in range(8):
    m_t[i] = m[ip[i]-1]
m = m_t

print(m)

m1 = func(m, k1)
print(m1)
m1 = m1[4:] + m1[0:4]
print(m1)

m2 = func(m1, k2)

for i in range(8):
    m_t[i] = m2[ip_inv[i]-1]
m = m_t
print(m)



