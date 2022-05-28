# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # converting word and anagram to lists
    word_to_List = list(word.lower())
    anagram_to_List = list(anagram.lower())
    # sorting them
    word_Sorted = word_to_List.sort()
    anagram_Sorted = anagram_to_List.sort()
    # conditionals
    if word_to_List == anagram_to_List:
        print(True)
    else:
        print(False)


find_anagram("hello", "check")

find_anagram("below", "elbow")

find_anagram("ReScUe", "secure")  # I used .lower() method to make it valid

find_anagram("mouse", "house")
