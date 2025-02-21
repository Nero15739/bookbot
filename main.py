def main ():
    path_to_file = "Books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        num = countWords(file_contents)
        print(f"Word Count : {num}")
        charCounts = countChars(file_contents)
        #Print char counts iterating through the dictionary
        print(charCounts)


# Counts the individual words that are separated by any white space or new line, tab etc..
def countWords(words):
    arr = words.split()
    return len(arr)

#Counts the chars in the alphabet after being lowered. then returns the dictionary
#ARGS: string file_contents
#RETURNS: Dictionary char counts
def countChars(file_contents) :
    charCounts = {}
    for char in file_contents:
        lowerChar = char.lower()
        if lowerChar in charCounts.keys():
            charCounts[lowerChar] = charCounts[lowerChar] + 1
        else:
            charCounts[lowerChar] = 1
            # print(lowerChar)

    return charCounts
    

    
    
main()