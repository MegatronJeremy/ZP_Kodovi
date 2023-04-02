def gen_key(k):
    s = []
    t = []
    for i in range(256):
        s.append(i)
        t.append(k[i % len(k)])
    j = 0
    for i in range(256):
        j = (j + s[i] + t[i]) % 256
        s[i], s[j] = s[j], s[i]
    print(f'State vector: {s}')
    return ''.join([chr(c) for c in s])

def encrypt(m, s):
    m = [ord(c) for c in m]
    s = [ord(c) for c in s]
    e = []
    i, j = 0, 0
    for k in range(len(m)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        e.append(s[t] ^ m[k])

    return ''.join([chr(c) for c in e])

k = "symptomsofparanoia"
print(f'Key: {k}')

m = "are you sure you want to lose your life from a witch who has caused you nothing but strife"
k = [ord(c) for c in k]

s = gen_key(k)
c = encrypt(m, s)
print(f'Encrypted message: {c}')

d = encrypt(c, s)
print(f'Decrypted message: {d}')

    
