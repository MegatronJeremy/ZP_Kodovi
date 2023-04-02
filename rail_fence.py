from collections import deque


def encrypt(a, n):
    c = ''
    for i in range(n):
        step1 = (n - i - 1) * 2
        step2 = i * 2
        j = i
        c += a[j]
        while j < len(a):
            if step1 > 0:
                j += step1
                if j < len(a):
                    c += a[j]
            if step2 > 0:
                j += step2
                if j < len(a):
                    c += a[j]
    return c


def decrypt(a, n):
    c = ['' for _ in range(len(a))]
    q = deque(a)
    for i in range(n):
        step1 = (n - i - 1) * 2
        step2 = i * 2
        j = i
        c[j] = q.popleft()
        while j < len(a):
            if step1 > 0:
                j += step1
                if j < len(a):
                    c[j] = q.popleft()
            if step2 > 0:
                j += step2
                if j < len(a):
                    c[j] = q.popleft()

    return ''.join(char for char in c)


def main():
    a = 'taguj tri crnje'
    a = a.replace(' ', 'x')

    n = 3

    c = encrypt(a, n)
    print(c)

    d = decrypt(c, n)
    print(d)


if __name__ == '__main__':
    main()
