import sys

from stats import get_num_words
from stats import get_char_count
from stats import sorted_char_count

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_content = f.read()
    return file_content

def main(filepath=None):
    if filepath is None:
        if len(sys.argv) == 2:
            filepath = sys.argv[1]
        
            # filepath = "books/frankenstein.txt"
            book_content = get_book_text(filepath)
            num_words = get_num_words(book_content)
            num_chars = get_char_count(book_content)
            
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {filepath}")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")  
            for key, value in sorted_char_count(num_chars):
                print(f"{key}: {value}")

        else: 
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

main()