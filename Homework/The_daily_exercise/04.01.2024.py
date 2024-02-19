def check_str():
    cuont = 0
    str = "     "
    while len(str) >= 4:
        str = input("Enter a string: ")
        if "T" not in str:
            cuont += 1
    print(f"The num of sentences without \"t\" is {cuont}")

check_str()