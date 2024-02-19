def get_weight(num):
    num_str = str(num)
    sum_of_weight_digit = 0

    for i in num_str[1:-1]:
        sum_of_weight_digit += int(i)
    return sum_of_weight_digit

def list_sorted_by_numbers(lst):
    num_weight = -1
    for i in lst:
        if get_weight(i) > num_weight:
            num_weight = get_weight(i)
        else:
            return False
    return True

def list_sorted_and_uniqe(lst1, lst2):
    weights = []
    uniqe_weight_num = []
    for num in lst1 + lst2:
        weights.append(get_weight(num))
    for weight in weights:
        if weights.count(weight) == 1:
            for num in lst1 + lst2:
                if get_weight(num) == weight:
                    uniqe_weight_num.append(num)

    return uniqe_weight_num


lst1 = [35,923,781,12349,1892]
lst2 = [2,358,181,5821,1742,36621,27731]
print(list_sorted_and_uniqe(lst1, lst2))




