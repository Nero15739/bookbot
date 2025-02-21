def main ():
    path_to_file = "Books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        num = countWords(file_contents)
        print(f"Word Count : {num}")



def countWords(words):
    arr = words.split(' ')
    # for str in arr:
    #     print(str)
    return len(arr)
    
main()