def main ():
    path_to_file = "Books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

main()