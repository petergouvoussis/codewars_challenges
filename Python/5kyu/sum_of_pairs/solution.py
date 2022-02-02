def sum_pairs(ints, s):
    
    check = set()
    for i in ints:
        target = s - i
        if target in check:
            return [target, i]
        check.add(i)
    return None
