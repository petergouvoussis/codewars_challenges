import string
def alphabet_position(text):
    
    abc = '0' + string.ascii_lowercase
    output = []
    for i in text:
        if i.isalpha():
            output.append(str(abc.index(i.lower())))
    return ' '.join(output)
