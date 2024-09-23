# Method 1: Using the str() function
num = 123
num_str1 = str(num)
print(f"Using str(): {num_str1} (Type: {type(num_str1)})")

# Method 2: Using f-strings (Python 3.6+)
num_str2 = f"{num}"
print(f"Using f-strings: {num_str2} (Type: {type(num_str2)})")

# Method 3: Using the format() method
num_str3 = "{}".format(num)
print(f"Using format(): {num_str3} (Type: {type(num_str3)})")

# Method 4: Using the __str__() method
num_str4 = num.__str__()
print(f"Using __str__(): {num_str4} (Type: {type(num_str4)})")
