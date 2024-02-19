def cute_num(get_num):
    num = str(get_num)
    return int(num[-1]) % int(num[0]) == 0

def cute_arr(arr, column):
    for i in arr:
        if cute_num(i[column]) == False:
            return False
    return True

def honey_arr(arr):
    for i in range(len(arr[0])):
        if cute_arr(arr,i) == True:
            return True
    return False

arr = [[12, 24, 26], [39, 48, 36], [36, 17, 15]]
arr1 = [[12, 24, 26], [23, 23, 23], [23, 23, 23]]
arr2 = [[23, 24, 23], [23, 48, 23], [23, 17, 23]]
arr3 = [[1, 3, 5], [6, 7, 8], [9, 3, 2]]

print(f"{honey_arr(arr)} need to be => True.")
print(f"{honey_arr(arr1)} need to be => False.")
print(f"{honey_arr(arr2)} need to be => True.")
print(f"{honey_arr(arr3)} need to be => True.")
