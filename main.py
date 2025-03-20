import sys
from stats import get_book_word_count, count_char, sort_counts


def get_book_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    file_path = sys.argv[1]
    word_count = get_book_word_count(file_path)
    text = get_book_text(file_path)
    char_count = count_char(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in sort_counts(char_count):
        print(f"{c['character']}: {c['count']}")
    print("============= END ===============")


main()
