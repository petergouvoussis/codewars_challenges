def prime(n):

    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            divs.update([i, int(n/i)])
    return len(divs) == 2


def gap(g, m, n):
    
    temp = 0
    for i in range(m, n+1):
        if prime(i):
            if temp == 0:
                temp = i
            elif temp>0 and i-temp == g:
                return [temp, i]
            else:
                temp = i
    return None
