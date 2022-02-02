import string
def rot13(message):
    
    abc = string.ascii_lowercase
    output = ''
    for i in message:
        if i.isalpha():
            try:
                output += abc[abc.index(i.lower())+13]
            except:
                output += abc[12-(25-abc.index(i.lower()))]
        else:
            output += i
    return ''.join(v.upper() if message[i].isupper() else v for i,v in enumerate(output))
