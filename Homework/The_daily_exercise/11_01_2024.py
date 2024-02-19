def sort_lst(lst):
    minus = 0
    plos = 0
    for i in lst:
        if i < 0:
            minus += 1
        else:
            plos += 1
    if plos == minus:
        print(sorted(lst))
    else:
        print(sorted(lst, reverse=True))

sort_lst([-1, -3, -2, 4, 5, 7])