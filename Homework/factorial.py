import time
def check_factorial(num):
    x = 1
    y = 2
    while x <= num:
        if x == num:
            return f"Yes: {y-1}"
        x = x * y
        y += 1
    return f"No!"

print(check_factorial(3))

