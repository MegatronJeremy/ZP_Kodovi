def main():
    # a = "X NROLNR VDWL MH QDSDG"
    a = "IXFN QLJJHUV"
    for j in range(1, 26):  # offset from 1 to 25
        print(j, ':', end='')
        for i in a:
            if i.isalpha():
                c = chr(65 + (ord(i) - 65 - j) % 26)
            else:
                c = i
            print(c, end='')
        print('\n')


if __name__ == '__main__':
    main()
