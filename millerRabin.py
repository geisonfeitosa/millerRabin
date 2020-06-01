def miller_rabin(n, a):
    nMenosUm = n - 1
    k = 0
    m = 0

    while nMenosUm % 2 == 0:
        m = int(nMenosUm / 2)
        nMenosUm = m
        k += 1

    b = int((a ** m) % n)

    print("K = ", k)
    print("M = ", m)
    print("B = ", b)

    if b % n == 1:
        return True
    
    for i in range(k):
        if b == -1 % n:
            return True
        else:
            b = (b ** 2) % n

    return False