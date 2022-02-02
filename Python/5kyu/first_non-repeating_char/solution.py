def first_non_repeating_letter(string):
    
    output = ''
    for i in string:
        if string.lower().count(i.lower()) == 1:
            output += i
    return '' if not output else output[0]
