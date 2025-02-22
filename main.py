import os
import sys
from stats import count_chars, count_words

def main ():
    #await input for the book name to input 
    print("""
  ____              _    ____        _   
 |  _ \            | |  |  _ \      | |  
 | |_) | ___   ___ | | _| |_) | ___ | |_ 
 |  _ < / _ \ / _ \| |/ /  _ < / _ \| __|
 | |_) | (_) | (_) |   <| |_) | (_) | |_ 
 |____/ \___/ \___/|_|\_\____/ \___/ \__|                                      
""")
    print("The book analysis bot to help you know if the word count is for you ;)\n")
    selected_book_path = None
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            selected_book_path = sys.argv[1]
        else:
            print(f"!!!Path not found!!!\n{sys.argv[1]}")
    else:
        selected_book_path = get_book()
    
    if selected_book_path != None:
        print_report(selected_book_path)
    

def get_book():
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

    except Exception as e:
        print(f"Error: {e}")

    return selected_book_path


def print_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        word_num = count_words(file_contents)
        char_counts = count_chars(file_contents)
        #converts to a list of tuples that then are converted back into a dictionary 
        sorted_dict = dict(sorted(char_counts.items()))
        #Print char counts iterating through the dictionary

        # Print a report
        print(f"\n--- Begin report of {file_path} ---")
        print(f"{word_num} words found in the document\n")
        for key in sorted_dict.keys():
            if key.isalpha():
                print(f"{key}: {sorted_dict[key]}")
        print("--- End report ---")

    
main()