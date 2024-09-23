def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    return (x * y) // compute_gcd(x, y)

num1 = 54
num2 = 24

lcm = compute_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
