import re


# Python Test 1
def is_valid_string(s):
    if len(s) < 6:
        return False
    pattern = r'^(?=(?:[^0-9]*[0-9]){2,3}[^0-9]*$)(?=(?:[^0-9]*[0-9][^0-9]*){2,3}$).{6,}$'
    return bool(re.match(pattern, s))

# Example usage
print(is_valid_string("a1b2c3"))  # True
print(is_valid_string("a1b2c"))   # False (less than 6 characters)
print(is_valid_string("a1b2c3d4")) # False (more than 3 numbers)
print(is_valid_string("123456"))  # False (no non-numerical characters between numbers)
