'''Euler's Totient'''

def divisors(n):
    
    divs = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divs.update([i, int(n/i)])
    return divs

def proper_fractions(n):

    if n == 1: return 0
    output = n
    for i in divisors(n):
        if len(divisors(i)) == 2:
            output *= (1-(1/i))

    return int(output)

'''Brute force attempt'''

# def divisors(n):
#     divs = set()
#     for i in range(1, int(n**0.5)+1):
#         if n%i == 0:
#             divs.update([i, int(n/i)])
#     return divs

# def proper_fractions(n):
#     denom = divisors(n) - {1}
#     count = 0
#     for i in range(1,n):
#         nume = divisors(i) - {1}
#         if denom.isdisjoint(nume):
#             count += 1
#     return count

'''Euclidean Algorithm'''

# def proper_fractions(n):
#     if n == 1: return 0
#     count = 0
#     for nume in range(n):
#         denom = n
#         while nume > 0:
#             temp = nume
#             nume = denom%nume
#             denom = temp
#         if denom == 1:
#             count += 1
#     return count
