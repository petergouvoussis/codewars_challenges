def unique_in_order(iterable):
    
    output = []
    previous = ''
    for i in iterable:
        if i != previous:
            output.append(i)
            previous = i
        else:
            pass
    return output
