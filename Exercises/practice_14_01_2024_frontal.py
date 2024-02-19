def mult(a, b):
    res = 0
    while b > 0:
        res += a
        b -= 1
    return res

def divide(x, y):
    res = 0
    while x > 0:
        x -= y
        res += 1
    return res

def power(base, exponent):
    result = 1
    while exponent > 0:
        result = mult(result, base)
        exponent -= 1
    return result

def square_root(num):
    res = 1
    while mult(res,res) != num:
        res += 1
    return res


'''
from datetime import datetime

import pytz

timezone = pytz.timezone('Europe/Bucharest')
current_time = datetime.now(timezone)
# current_time = datetime.now( )

print(current_time)

formatted_time = current_time.strftime("%d.%m.%Y %H: %M: %S")
print(formatted_time)
'''
