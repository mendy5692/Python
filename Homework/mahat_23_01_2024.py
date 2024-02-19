def what(a):
    length = len(a)
    for i in range(2, length - 1, 2):
        if a[i] < a[i - 2]:
            return False
        i += 1
        if a[i] > a[i - 2]:
            return False
    return True

def bigest_num(list):
    if list[1] > list[-2]:
        return list[1]
    else:
        return list[-2]


list = [1, 2222, 111, 22, 1111, 2]
print(what(list))
print(bigest_num(list))

