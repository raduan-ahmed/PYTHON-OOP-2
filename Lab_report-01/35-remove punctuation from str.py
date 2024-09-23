import string

# Function to remove punctuation from a string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

# Input string
input_string = "Hello!!!, he said ---and went."

# Remove punctuation
cleaned_string = remove_punctuation(input_string)

# Print the result
print("Original String:", input_string)
print("String without Punctuation:", cleaned_string)
