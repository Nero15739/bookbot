def main ():
    
    path_to_file = "Books/frankenstein.txt"
    print_report(path_to_file)
    




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

def print_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        word_num = count_words(file_contents)
        char_counts = count_chars(file_contents)
        #converts to a list of tuples that then are converted back into a dictionary 
        sorted_dict = dict(sorted(char_counts.items()))
        #Print char counts iterating through the dictionary

        # Print a report
        print(f"--- Begin report of {file_path} ---")
        print(f"{word_num} words found in the document\n")
        for key in sorted_dict.keys():
            if key.isalpha():
                print(f"The '{key}' character was found {sorted_dict[key]} times")
        print("--- End report ---")


        

    
    
main()