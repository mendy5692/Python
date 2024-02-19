def first_num(num):
    while (num >= 10):
        num = int(num / 10)
    return num

def check_bro(num1, num2):
    return (((num1 % 10) == (num2 % 10)) and (first_num(num1) == (first_num(num2))))

print(check_bro(1234567,17))