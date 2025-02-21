import os
def main ():
    #await input for the book name to input 
    print("Welcome to Bookbot!\nThe book analysis bot to help you know if the word count is for you ;)\n")
    selected_book_path = ""
    try:
        book_files = os.listdir("books/")

        is_found = False
        while(not is_found):
            print("\n---Books Available---")
            for i in range(0, len(book_files)):
                print(f"{i}: {book_files[i]}")
            response = input("Please select a book number or specify a file location\n")
            if response.isnumeric():
                try:
                    selected_book_path = f"books/{book_files[int(response)]}" 
                    is_found = True
                except Exception as e:
                    print(f"Incorrect Input! Must be a number between 0 and {len(book_files)}")
            elif os.path.exists(response):
                selected_book_path = response
                is_found = True
            else:
                print(f"\t!!!Book does not exist : {response}")

    except:
        print("books/ Directory not found")
    
    print_report(selected_book_path)
    




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