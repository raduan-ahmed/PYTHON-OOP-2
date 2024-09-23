import random
import string

# Function to generate a random string
def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Specify the length of the random string
length_of_string = 12

# Generate and print the random string
random_str = generate_random_string(length_of_string)
print("Random String:", random_str)
