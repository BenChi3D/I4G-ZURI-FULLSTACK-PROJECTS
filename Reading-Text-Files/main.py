# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    # opening the file and closing it at once after reading.
    with open(filename) as file:
        # reading the file and storing in contents
        contents = file.read()
        # printing the contents of the file
        print(contents)


def count_words():
    count = 0
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    read_text = text.read()
    woord = set(read_text.split())
    for word in woord:
        count ++ 1
    return {"as": 10, "would": 20}


read_file_content('story.txt')
count_words()