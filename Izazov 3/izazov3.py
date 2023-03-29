import matplotlib.image as img
import numpy as np

def lkg():
    m = 2**32
    a = 22695477
    c = 1
    x0 = 17369
    for i in range(91):
        x1 = (a * x0 + c) % m
        x0 = x1
    
    return x0

def dec_vig(c: str, k: str):
    d = ''
    c_lst = [int(c, 16) for c in c]
    k_lst = [int(c, 16) for c in k]
    n = len(c_lst)
    m = len(k_lst)
    for i in range(m):
        i = (c_lst[i] - k_lst[i]) % 16
        d += f'{i:x}'
    for i in range(m, n):
        i = (c_lst[i] - int(d[i-m], 16)) % 16
        d += f'{i:x}'
    return d

def cbc_dec(iv, c, k):
    i = dec_vig(c, k)
    p = int(i, 16) ^ int(iv, 16)
    return f'{p:x}'

k = "2A8"
iv = hex(lkg())[-6:]

file = open('ciphertext.txt', 'r')
fileW = open('plaintext.txt', 'w')

mtx = []
for _i in range(402):
    row = []
    for _j in range(270):
        rgb = file.readline().rstrip()
        old_c = rgb
        rgb = cbc_dec(iv, rgb, k)
        iv = old_c
        
        if len(rgb) < 6:
            for _k in range(6 - len(rgb)):
                rgb = "0" + rgb

        fileW.write(rgb + '\n')
        
        row.append([int(rgb[0:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16)])
    mtx.append(row)

file.close()
fileW.close()

img.imsave('secretlocation.jpg', np.uint8(mtx))

print("ok")
