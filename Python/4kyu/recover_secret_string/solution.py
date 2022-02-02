def recoverSecret(triplets):
    
    s = list({i for j in triplets for i in j})
    while True:
        temp = s[:]
        for i in triplets:
            for j in range(2):
                a = temp.index(i[j])
                b = temp.index(i[j+1])
                if a > b:
                    temp[a], temp[b] = temp[b], temp[a]
        if s == temp:
            return ''.join(s)
        else:
            s = temp[:]
