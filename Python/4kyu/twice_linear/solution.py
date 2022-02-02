def dbl_linear(n):
    
    u = [1]
    pointer_a = 0
    pointer_b = 0
    while len(u) - 1 < n:
        a = u[pointer_a] * 2 + 1
        b = u[pointer_b] * 3 + 1
        if a < b:
            u.append(a)
            pointer_a += 1
        elif a > b:
            u.append(b)
            pointer_b += 1
        elif a == b:
            u.append(a)
            pointer_a += 1
            pointer_b += 1
    return u[n]
