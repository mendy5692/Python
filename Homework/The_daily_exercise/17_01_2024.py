def check_char(words, get_char):
    for char in words:
        for i in char:
            if get_char == i:
                return True
    return False

def check_alpha(words):
    ascii = 97
    for i in range(25):
        if check_char(words, chr(ascii)) == False:
            return False
        ascii += 1
    return True

tuple_1 = ("abcd", "efghi", "jgklmnopqrstuvwxyz")

print(check_alpha(tuple_1))
if "a" in tuple_1:
    print("!!!")