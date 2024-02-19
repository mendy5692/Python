import math


def calculate_sum_in_base_3(num):
    total = 0

    p = 0

    for digit in reversed(num):
        digit = int(digit)

        term_result = digit * math.pow(3, p)

        print(f"{digit} * 3^{p} = {term_result}")

        total = total + term_result

        p = p + 1

    return total


# Example usage for the input '12012'

input_number = '11012'

result = calculate_sum_in_base_3(input_number)

print(f"Total sum for {input_number} in base-3 is: {result}")
