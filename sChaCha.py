m = "D274EAA0926C5FD31972DD8605CA034C"
k = [[0xAB, 0xCD, 0xEF, 0x01],
     [0x12, 0x34, 0x56, 0x78],
     [0x76, 0x54, 0x32, 0x10],
     [0, 0, 0xBA, 0xBA]]

b = [row[:] for row in k]

def get_k(a):
    return k[a//4][a%4]

def get_b(a):
    return b[a//4][a%4]

def set_k(c, a):
    k[c//4][c%4] = a & 0xff

def qr(ac, bc, cc, dc):
    a = get_k(ac)
    b = get_k(bc)
    c = get_k(cc)
    d = get_k(dc)

    a = a + b
    d = d ^ a
    d = (d << 4) | ((d & 0xf0) >> 4)
    c = d + c
    b = b ^ c
    b = (b << 3) | ((b & 0xe0) >> 5)
    set_k(ac, a)
    set_k(bc, b)
    set_k(cc, c)
    set_k(dc, d)

def round(m, j):
    if j % 2:
        for i in range(0, 4):
            qr(i, i+1*4, i+2*4, i+3*4)
            i+=1
    else:
        for i in range(0, 4):
            qr(i, (i+1*4+1)%16, (i+2*4+2)%16, (i+3*4+3)%16)
            i+=1    

    for i in range(16):
        set_k(i, get_k(i)+get_b(i))

    c = ""
    for i in range(0, 16):
        c += f'{(int(m[i*2:i*2+2], 16) ^ get_k(i)):x}'

    c = c.upper()

    print(c)


round(m, 1)
