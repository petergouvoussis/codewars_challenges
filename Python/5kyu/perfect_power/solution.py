def isPP(n):
    
    m = 2
    k = 2
    while True:
        if m>n:
            return None
        elif m**k == n:
            return [m,k]
        elif m**k < n:
            k += 1
        else:
            k = 2
            m += 1
