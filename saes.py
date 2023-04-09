s_b = [[0x9, 0x4, 0xA, 0xB],
       [0xD, 0x1, 0x8, 0x5],
       [0x6, 0x2, 0x0, 0x3],
       [0xC, 0xE, 0xF, 0x7]]

def g(w, const):
    hi = w & 0xf
    lo = (w & 0xf0) >> 4
    w = s_b[(hi & 0b1100) >> 2][hi & 0b11] << 4
    w |= s_b[(lo & 0b1100) >> 2][lo & 0b11]
    w = w ^ const
    return w

def gen_key(k, const):
    hi = (k & 0xff00) >> 8
    lo = (k & 0xff)

    hi = hi ^ g(lo, const)
    lo = hi ^ lo

    return (hi << 8) | lo

def nibble_subs(m):
    r = 0
    k = 0
    while m > 0:
        r = r | (s_b[(m & 0b1100) >> 2][m & 0b11] << k)
        k += 4
        m >>= 4
    return r

def shift_row(m):
    return (m & 0xf0f0) | ((m & 0x0f00) >> 8) | ((m & 0x000f) << 8)

def gf_m2(a):
    b = a & 0x8
    a = (a << 1) & 0xf
    if b:
        a ^= 0x3
        
    b = a & 0x8
    a = (a << 1) & 0xf
    if b:
        a ^= 0x3

    return a

def gf_m4(a):
    return gf_m2(a)

def mix_column(m):
    a1 = (m & 0xf000) >> 12
    a2 = (m & 0x0f00) >> 8
    a3 = (m & 0x00f0) >> 4
    a4 = (m & 0x000f)

    b1 = a1 ^ gf_m4(a2)
    b2 = gf_m4(a1) ^ a2
    b3 = a3 ^ gf_m4(a4)
    b4 = gf_m4(a3) ^ a4

    return (b1 << 12) | (b2 << 8) | (b3 << 4) | b4

def add_key(k, m):
    return k ^ m

def main():
    k1 = 0x99D
    k2 = gen_key(k1, 0x80)
    k3 = gen_key(k2, 0x30)
    m = 0x24BB
    print(f'Keys: {hex(k1)}, {hex(k2)}, {hex(k3)}')

    m = add_key(k1, m)
    print(f'With key 0 added: {hex(m)}')

    m = nibble_subs(m)
    m = shift_row(m)
    print(f'Before mix columns: {hex(m)}')
    m = mix_column(m)
    print(f'After mix columns: {hex(m)}')
    m = add_key(k2, m)
    print(f'Round 1: {hex(m)}')

    m = nibble_subs(m)
    m = shift_row(m)
    m = add_key(k3, m)
    print(f'Round 2: {hex(m)}')
    

if __name__ == '__main__':
    main()
