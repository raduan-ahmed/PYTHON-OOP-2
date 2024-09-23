def find_substring_occurrences(main_string, substring):
    count = main_string.count(substring)
    return count


main_string = "This is a test string. This string is for testing."
substring = "is"

occurrences = find_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' occurs {occurrences} times in the main string.")
