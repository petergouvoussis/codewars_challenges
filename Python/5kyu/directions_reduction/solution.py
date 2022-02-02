def dirReduc(arr):
    
    short_cuts = [['WEST', 'EAST'], ['EAST', 'WEST'], ['NORTH', 'SOUTH'], ['SOUTH', 'NORTH']]
    while True:
        temp = []
        i = 0
        while i < len(arr):
            if i == len(arr) - 1:
                temp.append(arr[i])
                break
            elif arr[i:i+2] not in short_cuts:
                temp.append(arr[i])
                i += 1
            else:
                i += 2
        if arr == temp:
            break
        else:
            arr = temp[:]
    return arr
