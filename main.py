from stats import word_count, character_count, char_list
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path) 
    
    num_chars = character_count(book_text)
    print(char_list(num_chars))
    
    print("================ BOOKBOT ================\n")
    print(f"--- Analyzing book found at {book_path}... ---\n")
    print("-----------Word Count Report-----------\n")
    total_words = word_count(book_text)
    print(f"Found {total_words} total words.\n")
    print("------------Character Count------------")

    character_frequency = character_count(book_text)
    char_list(character_frequency)
    print("================ End report ================\n")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()    
        return file_contents

if __name__ == '__main__':
    main()
