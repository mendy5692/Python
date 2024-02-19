import random
# def list_order(lst):
#     even =[]
#     odd = []
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even + odd == lst

# print(list_order([3,0,5,6,8,9,1,56,78,97,9]))
# print( list_order([2,4,6,8,3,1,5,9]))
#----------------------------------------------------
def creat_list_order(lst):
    even =[]
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd
def creat_list(x,y,size):
    list = []
    for i in range(size):
        list.append(random.randint(x,y))
    print(creat_list_order(list))


creat_list(10,20,10)




