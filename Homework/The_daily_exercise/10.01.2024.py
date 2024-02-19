def is_valid(s):
    return ((len(s) % 2) != 0) and (s[0] == s[-1] == s[len(s) // 2])

def check_str():
    valid = 0
    invalid = 0
    for i in range(10):
        if is_valid(input("Enter a string: ")) == True:
            valid += 1
        else:
            invalid +=1
    print(f"the number of 'valid' srings is '{valid}'.\nthe number of 'invalid' strings is '{invalid}'.")

check_str()
