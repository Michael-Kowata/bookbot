def word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def character_count(text):
    char_count = {}
    text = text.lower()

    #Create frequency for every charcter in the text
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count


def char_list(input_char_count):
    char_list = []

    #Map each alphanumeric character and it's frequency to a corresponding string, and add to a list
    for char in input_char_count:
        if char not in char_list and char.isalpha():
            char_dict = {"char": char, "num": input_char_count[char]}
            char_list.append(char_dict)
    
    #Sort by highest frequency
    char_list.sort(reverse=True, key=sort_on)

    #Print out the frequency of alphanumeric characters in the list
    for char in char_list:
        print(f"{char['char']}: {char['num']}")