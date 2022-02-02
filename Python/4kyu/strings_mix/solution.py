def mix(s1, s2):

    s1 = ''.join(x for x in ''.join(s1.split()) if x.isalpha() and x.islower())
    s2 = ''.join(x for x in ''.join(s2.split()) if x.isalpha() and x.islower())
    letters = set(s1+s2)
    output = []

    for i in letters:
        if s1.count(i) > 1 and s1.count(i) > s2.count(i):
            output.append(f'1:{s1.count(i)*i}')
        elif s2.count(i) > 1 and s2.count(i) > s1.count(i):
            output.append(f'2:{s2.count(i)*i}')
        elif s1.count(i) > 1 and s1.count(i) == s2.count(i):
            output.append(f'=:{s2.count(i)*i}')
            
    output.sort()
    output.sort(key = len, reverse = True)
    return '/'.join(output)
