# The function should accept two variables.
# The first one will have to be a string.
# And the second will have to be an integer.
# The exercise will have to return that the first is really a string and the second is really an integer.
# In the event that one of the conditions is not met, we will pop an error with an appropriate caption.
def get_str_and_int(a, b):
    assert isinstance(a, str), "x cannot be a int or a float"
    assert isinstance(b, int), "y cannot be a srting"
    return f"the first argument is a string"\
           f"\nthe second argument is a int"

print(get_str_and_int("10", 10))