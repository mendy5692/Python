def avarage_list(lst1, lst2):
    lst3 = []
    for i in lst1:
        if (i not in lst2) and (i not in lst3):
            lst3.append(i)
    return lst3

def two_num_list(lst1, lst2):
    lst3 = avarage_list(lst1, lst2) + lst2
    lst4 = []
    for i in range(10,100):
        if i not in lst3:
            lst4.append(i)
    return lst4

lst1 = [12, 15, 40, 21, 17, 15, 80, 21]
lst2 = [12, 25, 21, 86, 12, 17]

print(avarage_list(lst1, lst2))
print(two_num_list(lst1, lst2))