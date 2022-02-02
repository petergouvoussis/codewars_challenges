def snail(array):
    
    output = []
    while array:
        if not output:
            output.extend(array[0])
            array.remove(array[0])
        else:
            array = list(map(list, zip(*array)))[::-1]
            output.extend(array[0])
            array.remove(array[0])

    return output
