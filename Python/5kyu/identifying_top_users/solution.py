def id_best_users(*args):

    valid_id = list(set.intersection(*(set(x) for x in args)))

    d = {x:sum(month.count(x) for month in args) for x in valid_id}
    output = [[d[x], sorted([k for k,v in d.items() if v == d[x]])] for x in d.keys()]

    web_data = []
    for i in output:
        if i not in web_data:
            web_data.append(i)
    return sorted(web_data, key = lambda x: -x[0])
