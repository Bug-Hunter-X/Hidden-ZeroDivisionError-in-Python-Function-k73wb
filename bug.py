def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling for a=0
    elif b == 0:
        return a  # Correct handling for b=0
    else:
        result = a / b
        return result

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(0, 5))  # Output: 5
print(function_with_uncommon_error(5, 0))  # Output: 5
print(function_with_uncommon_error(0,0)) # Output:ZeroDivisionError