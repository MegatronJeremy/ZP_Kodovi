import random

die = random.SystemRandom()  # A single dice


def single_test(n, a):
    # n - test for primeness, a - witness
    exp = n - 1  # start from Fermat's little theorem
    while not exp & 1:  # while even
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:  # equal to negative one
            return True

        exp <<= 1

    return False


def miller_rabin(n, k=40):
    for i in range(k):
        a = die.randrange(2, n - 1)
        if not single_test(n, a):
            return False

    return True


#print(miller_rabin(561))
print(single_test(91, 9))
print(single_test(91, 11))
