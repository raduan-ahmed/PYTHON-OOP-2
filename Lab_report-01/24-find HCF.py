def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


num1 = 54
num2 = 24

hcf = compute_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf}")
