def check_balance_list(lst):
    length = len(lst)
    if length > 1 and length % 2 != 0:
        for i in range(length):
            if i < length // 2:
                if lst[i] < lst[length // 2]:
                    return False
            elif i > length // 2:
                if lst[i] > lst[length // 2]:
                    return False
        return True
    return False

print(check_balance_list([22,56,123,12,10,-4,2]))