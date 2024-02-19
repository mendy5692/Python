def find_fibonacci(get_num):
    num1 = 1
    num2 = 1
    num3 = 0

    while num2 <= get_num:
        num3 = num2
        num2 = num1 + num2
        num1 = num3

    if num2 - get_num > get_num - num1:
        print(num3)
    else:
        print(num2)

def sort_find_fibonacci(get_num):
    num1, num2 = 1 , 1

    while num2 <= get_num:
        num1, num2 = num2, num1 + num2

    if num2 - get_num > get_num - num1:
        print(num1)
    else:
        print(num2)

find_fibonacci(10)
sort_find_fibonacci(10)