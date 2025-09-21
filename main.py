
import sys
from stats import count_words, char_count, sort_char_counts


def get_book_text(path):
    with open(path) as f:
        return f.read()
   
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    characters = char_count(text)
    sorted_chars = sort_char_counts(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("------- Character Count ---------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    
main()