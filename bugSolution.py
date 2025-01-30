def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return 0 # Or raise an exception: raise ZeroDivisionError("Both a and b are zero")
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        result = a / b
        return result

# Example usage:
print(function_with_uncommon_error_solution(10, 2))  # Output: 5.0
print(function_with_uncommon_error_solution(0, 5))  # Output: 5
print(function_with_uncommon_error_solution(5, 0))  # Output: 5
print(function_with_uncommon_error_solution(0,0)) # Output: 0