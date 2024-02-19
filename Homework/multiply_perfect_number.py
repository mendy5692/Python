def multiply_perfect_number(num):
    result = 0

    for i in range(1,num):
        if num % i == 0:
            result += i

    return num == result

# print(multiply_perfect_number(0))

def mpn_numbers(num):
    i = 1
    counter = 0
    mpn_list = []
    while counter != num:
        if multiply_perfect_number(i):
            mpn_list.append(i)
            counter += 1
        i += 1
    print(mpn_list)

mpn_numbers(4)