def sort_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Sort the words
    words.sort()
    return words

# Input sentence
sentence = "Hello this is an example with cased letters"

# Sort the words
sorted_words = sort_words(sentence)

# Print the sorted words
print("The sorted words are:")
for word in sorted_words:
    print(word)
