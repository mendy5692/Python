def get_next_letter(x):
    if ord(x) == 122:
        return chr(97)
    else:
        return chr(ord(x) + 1)

def get_next_string(x):
    y = 0
    new = ''
    for i in x:
        new += get_next_letter(i)
    return new

print(get_next_string("abcdefg"))