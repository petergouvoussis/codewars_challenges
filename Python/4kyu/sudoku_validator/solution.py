def done_or_not(board):
    
    #Validate rows
    for i in board:
        if len(set(i)) != 9:
            return 'Try again!'
    #Validate cols
    for i in list(zip(*board)):
        if len(set(i)) != 9:
            return 'Try again!'
    #Validate regions
    chunks = [list(zip(*board[i:i+3])) for i in range(0,9,3)]
    chunks2 = [list(x[i:i+3]) for i in range(0,9,3) for x in chunks]
    regions = []
    for i in chunks2:
        temp = []
        for j in i:
            for k in j:
                temp.append(k)
    regions.append(temp)
    for i in regions:
        if len(set(i)) != 9:
            return 'Try again!'
    return 'Finished!'
