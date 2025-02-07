def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        total_words = word_count(file_contents)
        print(f"--- Begin report of {book_path} ---")
        print(f"The total number of words in this text is {total_words}.")
        print("\n")
        character_frequency = character_count(file_contents)
        char_list(character_frequency)
        print("--- End report ---")

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
        print(f"The {char['char']} charcter appears {char['num']} times.")


if __name__ == '__main__':
    main()