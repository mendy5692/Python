def check_num():
    num = input("Enter a number: ")
    spacial = 0
    while num != "666":
        if num[0] != num[1] != num[2]:
            print(int(num))
            spacial += 1
        num = input("Enter a number: ")
    print(f"the num of spacials numbers is {spacial}.")

check_num()