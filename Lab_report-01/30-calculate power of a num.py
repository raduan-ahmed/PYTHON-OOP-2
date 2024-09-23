def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def power_builtin(base, exponent):
    return pow(base, exponent)


base = 3
exponent = 4


custom_result = power(base, exponent)
print(f"{base} raised to the power of {exponent} using custom function is: {custom_result}")


builtin_result = power_builtin(base, exponent)
print(f"{base} raised to the power of {exponent} using built-in function is: {builtin_result}")
