def validate_battlefield(field):

    if sum(sum(x) for x in field) != 20:
        return False

    diagonal = field[:]
    for i in diagonal:
        i.insert(0,0)
        i.append(0)
    diagonal.insert(0, 12*[0])
    diagonal.append(12*[0])

    for i,v in enumerate(diagonal):
        for i2, v2 in enumerate(v):
            if v2 == 1:

                up_left = diagonal[i - 1][i2 - 1]
                up_right = diagonal[i - 1][i2 + 1]
                bottom_left = diagonal[i + 1][i2 - 1]
                bottom_right = diagonal[i + 1][i2 + 1]

                if up_left == 1 or up_right == 1 or bottom_left == 1 or bottom_right == 1:
                    return False

            else:
                pass

    #d = {'battleship' : 1, 'cruiser': 2, 'destroyer': 3, 'submarine': 4}

    ships = []
    for row in field:

        count = 0
        for i,v in enumerate(row):

            if v == 1:
                count += 1
                if count > 4:
                    return False
                elif i == len(row)-1 and count > 1:
                    ships.append(count)
                    count = 0
                else:
                    pass

            elif v == 0 and count > 1:
                ships.append(count)
                count = 0

            else:
                count = 0

    for row in zip(*field):

        count = 0
        for i,v in enumerate(row):

            if v == 1:
                count += 1
                if count > 4:
                    return False
                elif i == len(row)-1 and count > 1:
                    ships.append(count)
                    count = 0
                else:
                    pass

            elif v == 0 and count > 1:
                ships.append(count)
                count = 0

            else:
                count = 0


    return True if ships.count(4) == 1 and ships.count(3) == 2 and ships.count(2) == 3 else False
