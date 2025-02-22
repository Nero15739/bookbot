# Counts the individual words that are separated by any white space or new line, tab etc..
def count_words(words):
    arr = words.split()
    return len(arr)

#Counts the chars in the alphabet after being lowered. then returns the dictionary
#ARGS: string file_contents
#RETURNS: Dictionary char counts
def count_chars(file_contents) :
    char_counts = {}
    for char in file_contents:
        lower_char = char.lower()
        if lower_char in char_counts.keys():
            char_counts[lower_char] = char_counts[lower_char] + 1
        else:
            char_counts[lower_char] = 1
            # print(lowerChar)

    return char_counts