def info_num():
    dic_num = {}
    num = ""
    while len(str(num)) != 3:
        num = int(input("Enter a num: "))
        if len(str(num)) != 3:
            basic_num = num
            big = 0
            small = 9
            while num != 0:
                num_digit = num % 10
                if (num_digit > big):
                    big = num_digit
                if (num_digit < small):
                    small = num_digit
                num = num // 10
            dic_num[basic_num] = {"big": [big], "small": [small]}
    print(dic_num.items())

info_num()