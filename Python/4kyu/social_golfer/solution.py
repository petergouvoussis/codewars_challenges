def valid(a)

    #Validation - 1
    check = lambda x: sorted(list(set(''.join(i for i in x))))
    day = check(a[0])
    for i in a:
        if check(i) != day:
            return False

    #Validation - 2
    day_length = len(a[0])
    group_length = len(a[0][0])
    for i in a:
        for j in i:
            if len(j) != group_length:
                return False
        if len(i) != day_length:
            return False
            
    #Validation - 3
    d = {x:[] for x in day}
    for i in a:
        for j in i:
            for ind,v in enumerate(j):
                d[v].extend(j[:ind] + j[ind+1:])
    for i in d:
        if len(d[i]) != len(set(d[i])):
            return False
    return True
