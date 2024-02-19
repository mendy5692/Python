def recursion(num):
    if num > 0:
        recursion(num - 1)
        print("*" * num)


recursion(4)
