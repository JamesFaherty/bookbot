import sys

from stats import count_words
from stats import count_characters
from stats import sort_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        f = f.read()
        return f

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    print    (f"{word_count} words found in the document")
    char_count = count_characters(text)
    sorted_chars = sort_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------") 
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
if __name__ == "__main__":
    main()
