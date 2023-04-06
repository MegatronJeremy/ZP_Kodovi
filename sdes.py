pc1 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
rot1 = 1
rot2 = 2
pc2 = [6, 3, 7, 4, 8, 5, 10, 9]
ip = [2, 6, 3, 1, 4, 8, 5, 7]
ip_i = [4, 1, 3, 5, 7, 2, 8, 6]
e = [4, 1, 2, 3, 2, 3, 4, 1]
s1 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
s2 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 2], [2, 1, 0, 3]]
p = [2, 4, 3, 1]


def permute(m, p):
    m_ret = []
    for i in range(len(p)):
        m_ret.append(m[p[i]-1])
    return m_ret


def gen_key(k, rot):
    m = len(k)
    n = m//2
    k_l = k[rot:n] + k[0:rot]
    k_r = k[n+rot:m] + k[n:n+rot]
    k = k_l + k_r
    return permute(k, pc2), k

def f_iter(m, k):
    m = permute(m, e)
    for i in range(len(m)):
        m[i] = m[i] ^ k[i]

    i1 = (m[0] << 1) + m[3]
    j1 = (m[1] << 1) + m[2] 
    i2 = (m[4] << 1) + m[7]
    j2 = (m[5] << 1) + m[6] 

    c1 = s1[i1][j1]
    c2 = s2[i2][j2]

    m = [(c1 & 0b10) >> 1, c1 & 0b1]
    m += [(c2 & 0b10) >> 1, c2 & 0b1]

    m = permute(m, p)
    return m

def round(t, k):
    m = len(k)
    n = m//2
    
    l0 = t[0:n]
    r0 = t[n:m]

    r1 = f_iter(r0, k)
    print('m after function:', ''.join([str(c) for c in r1]))

    for i in range(len(r1)):
        r1[i] = r1[i] ^ l0[i]

    return r0 + r1



k = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
k = permute(k, pc1)
k1, k = gen_key(k, rot1)
k2, k = gen_key(k, rot2)

print('k1:', ''.join([str(c) for c in k1]))
print('k2:', ''.join([str(c) for c in k2]))

m = [1, 0, 1, 1, 1, 1, 0, 1]
m = permute(m, ip)

print('m after ip:', ''.join([str(c) for c in m]))

m = round(m, k1)
print('m after round 1:', ''.join([str(c) for c in m]))

m = round(m, k2)
print('m after round 2:', ''.join([str(c) for c in m]))

m = m[len(m)//2: len(m)] + m[0:len(m)//2]
m = permute(m, ip_i)
print('final message:', ''.join([str(c) for c in m]))









    
