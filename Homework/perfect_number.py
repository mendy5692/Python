def perfect_num():
    for i in range(1, 1001):
        num = 0
        sum = i
        while sum > 0:
            num += sum % 10
            sum = sum // 10
        if i % num == 0:
            print(i)

perfect_num()