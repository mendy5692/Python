def get_num():
    num = int(input("Enter a number: "))
    sum_odd = 0
    num_odd = num
    sum = 0
    num_of_digit = 0
    while True:
        if num % 2 != 0:
            while num_odd != 0:
                sum_odd += num_odd % 10
                num_odd = num_odd // 10
            print(f"the sum of {num} is {sum_odd}.")
        num_of_digit += 1
        sum += num
        if num == 500:
            break
        num = int(input("Enter a number: "))
    print(f"the avarge is {sum / num_of_digit}")

get_num()