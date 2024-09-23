# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove any spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input string
input_string = "A man a plan a canal Panama"

# Check and print whether the string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
