# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Get user input
user_entered_phrase = input("Enter any words: ")

# Create a list of characters from the input
original_chars = list(user_entered_phrase)

# Create a list to hold the interleaved characters
combined_chars = [None] * (2 * len(original_chars))  # Double length for interleaving

# Interleave characters from the original list into alternating positions
combined_chars[::2] = original_chars  # Fill even indices
combined_chars[1::2] = original_chars  # Fill odd indices

# Join the interleaved characters back into a string
combined_phrase = ''.join(combined_chars)

# Print the result
print(combined_phrase)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get user input for the letter range
user_range = input("Enter a range of letters (e.g., a-z): ")

# Extract start and end letters from the user input
start, end = user_range.split('-')

# Ensure both start and end letters are in lowercase
start = start.lower()
end = end.lower()

# Find the indices in the alphabet
start_index = alphabet.index(start)
end_index = alphabet.index(end)

# Create the result string by slicing the alphabet
result_string = alphabet[start_index:end_index + 1]

print(result_string)


