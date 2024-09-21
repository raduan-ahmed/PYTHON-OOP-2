sentence = "Learning Python is fun and rewarding."

#a_Extract the substring "Python is fun" using negative slicing
substring = sentence[-27:-14]
print(" ")
print(f"Extracted substring: '{substring}'")

#b_Modify the original string by replacing "rewarding" with "exciting"
modified_sentence = sentence.replace("rewarding", "exciting")
print(f"Modified sentence: '{modified_sentence}'")

#c_Insert the phrase " Keep practicing!" after "exciting" in the modified string
insert_position = modified_sentence.find("exciting") + len("exciting")
final_sentence = modified_sentence[:insert_position] + " Keep practicing!" + modified_sentence[insert_position:]
print(f"Final sentence after insertion: '{final_sentence}'")

#c_Capitalize the first letter of each word in the final output
final_output = final_sentence.title()
print(f"Final output: '{final_output}'")
print(" ")
